Title: PostgreSQL indexes
Date: 2022-05-21 21:00
Category: PostgreSQL
Tags: postgresql, indexes
Author: Andrey G
Status: published
Summary: indexes in PostgreSQL database
Lang: en
---

[TOC]

[docs](https://www.postgresql.org/docs/current/indexes-types.html)

# Hash

Hash table by index key. Minimum bucket count = 2.
Only hash value and version are stored in bucket, without key value.

This index used 4 times of pages:
-meta page - index header
-bucket page - bucket storage
-overflow page - used if there is no more space in bucket
-bitmap page - bitmask, which "overflow page" can be reused

```
# supported operators
=
```

Keys are not stored in hash index - it means this index can't be used without processing data from table.

# B-tree

This index is for ordinal data only. Data that can be compared and sorted.

> a B-tree is a self-balancing tree data structure that maintains sorted data and allows searches,
> sequential access, insertions, and deletions in logarithmic time.

Key values are stored in index data.

```
# supported operators
<   <=   =   >=   >
```

Deduplication - process which executed to drop key value and replace it with row version id.
It can reduce size of index data.

> The B-tree generalizes the binary search tree, allowing for nodes with more than two children.

# GiST and SP-GiST

GiST - Generalized Search Tree. generalized self-balancing search tree

This index base on b-tree but _not only_ for sortable data.

In GiST we can implement "adapter" for out custom data type class and this type will supported by GiST index.

```
# supported operators
<<   &<   &>   >>   <<|   &<|   |&>   |>>   @>   <@   ~=   &&
```

GiST supports:
- geometric data

- range data

- ordinal types

- network addresses

- integer arrays

- label tree

- key-value

- trigrams

SP-GiST - space partitioning generalized Search Tree. This index very similar for GiST.
The basic idea is to divide the search space into non-overlapping regions, each of which, in turn, can also be
recursively divided into subdomains.

# GIN

GIN - Generalized Inverted Index.

The main area for GIN index - full text search.

> A GIN index stores a set of (key, posting list) pairs, where a posting list is a set of row
> IDs in which the key occurs. The same row ID can appear in multiple posting lists,
> since an item can contain more than one key. Each key value is stored only once,
> so a GIN index is very compact for cases where the same key appears many times.

GIN also supports:

- intarray

- key-value

- json query language

```
# supported operators
@> @? @@
```

# BRIN

BRIN - Block Range Index

block - page in PostgreSQL, 8kB of data.

this index was designed not to quickly search for the necessary lines,
but in order to avoid viewing obviously unnecessary ones.

> BRIN is incredibly helpful in efficiently searching over large time-series data and has the
> benefit of taking up significantly less space on disk than a standard B-TREE index.

> BRIN is designed for handling very large tables in which certain columns have some natural
> correlation with their physical location within the table.


# How to create index
```sql
-- To create a unique B-tree index on the column title in the table films
CREATE UNIQUE INDEX title_idx ON films (title);
```

# Partial index
```sql
CREATE INDEX orders_unbilled_index ON orders (order_nr)
WHERE billed is not true;
```

# Functional indexes or indexes by expression
```sql
-- To create an index on the expression lower(title), allowing efficient case-insensitive searches:
CREATE INDEX ON films ((lower(title)));
```

# For more than one column
```sql
CREATE INDEX idx_people_names
ON people (last_name, first_name);
```

# Index by JSONB column
```sql
CREATE INDEX animal_index ON farm (((animal ->> 'cow')::int))
WHERE (animal ->> 'cow') IS NOT NULL;
```

# INCLUDE index
the idea - include all required data for search into index but not to create index by all these columns
```sql
-- To create a unique B-tree index on the column title with included columns director and rating in the table films:
CREATE UNIQUE INDEX title_idx ON films (title) INCLUDE (director, rating);
```


<br />
# Conclusion

It is important to have right and useful indexes in the project.
