Title: PostgreSQL transaction isolation
Date: 2022-05-07 21:00
Category: PostgreSQL
Tags: postgresql, transaction isolation level
Author: Andrey G
Status: published
Summary: transaction isolation in PostgreSQL database
Lang: en
---

[TOC]

[PostgreSQL basics](/inside-postgresql.html)

[Book to read: PostgreSQL 14 изнутри, Егор Рогов](https://edu.postgrespro.ru/postgresql_internals-14.pdf)

A bit more details about transaction isolation in PostgreSQL database.

# Transaction isolation anomalies

Different levels of "Transaction isolation" differ from each other by the presence or absence of anomalies.

## lost update

Two transactions read one row and update this row independently (with original data) and commit one by one.
As result we can see only result from last commited transaction which was allied to original data.

## dirty read

Appears when the transaction (t2) reads uncommitted data from other transaction (t1).
But there is no guarantee that (t1) will be commited successfully.

## non-repeatable read

Transaction (t1) can read different data in two different read operations if
between first and second reads some any changes will be commited from other (t2) transaction.

## phantom read

Same like "non-repeatable read" but in row lavel.

Transaction (t1) can find different set of rows in two different searches if
between first and second search (read rows, select, find by selectoror or without), insert or delete operations will be commited from other (t2) transaction.

## read skew

note: `Read Uncommitted` is not possible in postgreSQL.

Transaction (t1) works and update some fields. Transaction (t2) read the same fields.
(t2) can read some fields when (t1) is working and get old (not updated) version and read some fields after (t1 commit) and it will be new (updated versions).
As result (t2) will work with not updated and updated versions. It will cause the inconsistency.

## write skew

Two transactions (t1) and (t2) can read one field, make some desition and write results in other fields.
Each of this result fields can be valid but both results together can broke consistency.

The main cause here it is parallel decision which was based on one original value and complex constraint.

## reading transcription only

If we have three parallel transactions: (t1 write) (t2 write), (t3 read).

(t3 read) can get inconsistency data because (t1 write) & (t2 write) in parallel can update this data and for (t1) & (t2) it is ok,
because they are working with original values and they can be aligned as sequence.
But for (t3) we can't guarantee which data will be available for this transaction.


# Snapshot Isolation, SI

Modern approach to organize isolation between transactions without locks.

A special version of SI is implemented in PostgreSQL - [MVCC](/inside-postgresql.html) (Multiversion Concurrency Control).

In snapshot isolation we can have only two types of anomalies: `write skew` and `reading transcription only`


# Transaction isolation

##  Read Uncommitted

anomalies: `dirty read`, `non-repeatable read`, `phantom read`, other

In this transaction we will read uncommitted data from other transactions.

In PostgreSQL this isolation can be selected but works like `Read Committed`

## Read Committed

anomalies: `non-repeatable read`, `phantom read`, other

In transaction we will read changes from other transactions only if this changes was committed. But it may cause `non-repeatable read`.

## Repeatable Read

anomalies: `phantom read`, other

There is no effects by `non-repeatable read` but `phantom read` still can happens.

## Serializable

This mode should avoid any anomalies. But your application must be ready to retry transactions.


<br />
# Conclusion

We must be careful to use databases... :(
