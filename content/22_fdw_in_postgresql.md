Title: FDW in PostgreSQL
Date: 2022-05-28 21:00
Category: PostgreSQL
Tags: postgresql, fdw, foreign-data wrapper
Author: Andrey G
Status: published
Summary: Foreign-data wrapper in PostgreSQL
Lang: en
---

[TOC]

The goal for this post:

1. Quick overview for foreign-data wrapper in PostgreSQL
2. Example of using FDW (foreign-data wrapper) between different database inside the same PostgreSQL instance

[documentation](https://www.postgresql.org/docs/current/postgres-fdw.html)

__postgres_fdw, foreign-data wrapper, FDW__ - it is ability to connect schema from external
database and interact with data from this schema like this data are in different schema in your database.

This feature can be used for:

- Consolidate data from different databases and exeecute queries over all database.
But this approach have performance penalty. May be critical for OLTP systems.

- In OLAP systems it is simple way to make analitics with all data from multiple sources without ELT/ETL processes.

- Transfer data from source to target without external tools, just write SQL.

__Note__: postgres_fdw module suppots __Push-down__ technology but not for all queries.

# How it works

Quick overview can be described in one sql script, which you can see below
```sql
--- Activate FDW ability. We must activate it if we would like to use FDW in PostgreSQL
CREATE EXTENSION postgres_fdw;

--- Next step - we described connection to "external" / "source" database.
--- Here we providing host, port, dbname to connect
--- name which we provided `source_server` we can use in our scripts to reffer to this connection
CREATE SERVER source_server
FOREIGN DATA WRAPPER postgres_fdw
OPTIONS (host '127.0.0.1', port '5432', dbname 'mimir_plants');

--- Mapping between local and remote PostgreSQL users are required
CREATE USER MAPPING FOR localUsername
SERVER source_server
OPTIONS (user 'sourceUsername', password 'pwd');

--- We sould create local schema which will be used to mount schema from remote database
create schema fwd_mimir_plants_public;
alter schema fwd_mimir_plants_public owner to progg;

--- And here, we are trying to mount remote schema to local "placeholder" schema
IMPORT FOREIGN SCHEMA public
FROM SERVER source_server INTO fwd_mimir_plants_public;

--- done, enjoi
```

To show information about fdw connection we can use this query
```sql
SELECT * FROM postgres_fdw_get_connections() ORDER BY 1;
```

To close, remove connection we can use this query
```sql
DROP SERVER IF EXISTS source_server CASCADE;
```

# Example of using FDW

When, we are configured FDW in PostgreSQL and now we can execute queries across local and remote data.

#### for what?
it is right time to discuss _"for what?"_, _"how we can use it?"_ ;)

There is no access between different databases inside PostgreSQL instance.
We can make a queries for different schemas in database but not between different databases.

Yes, it can seems so strage but sometime we would like to move data from one database
to enother inside same PostgreSQL instance or between different instances.

__Note__: FDW can be used in analitics systems (in DWH for example) to organize,
collect data and have access and ability to execute queries over all data.
But in this article we are talking about PostgreSQL as about OLTP engine.

### Example 1. Simple query

This simple query illustrates how we can get data from remote source and store it in local schema.

```sql
INSERT INTO "public"."plant" (global_id)
SELECT id as global_id
FROM "fwd_mimir_plants_public"."bio_graph_plant"
;
```

### Example 2. Query with JOIN

A slightly more complicated example with JOIN between local and remote schemas

```sql
INSERT INTO "public"."plant_name" (language_id, text, plant_id)
SELECT 1, sourceT.ru, newplant.id
FROM "fwd_mimir_plants_public"."bio_graph_plant" as sourceT
LEFT JOIN "public"."plant" newplant on sourceT.id = newplant.global_id
WHERE sourceT.ru is not null
;
```

# Conclusion

This feature in PostgreSQL saves me a lot of time.
It helps me to create database from some source data without any external tools like python,
i'm just writing SQLs to transfer and transform data from source to target schema.
