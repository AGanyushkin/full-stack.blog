Title: PostgreSQL table inheritance
Date: 2022-08-27 00:01
Category: overview
Tags: PostgreSQL
Author: Andrey G
Status: published
---

[docs](https://www.postgresql.org/docs/current/ddl-inherit.html)

# Table inheritance

In PostgreSQL we can reduce number of code which required to describe db schema with "table inheritance".

This approach seems like inheritance in other languages :)

### For example:
we have structures which described names of some entities (`plant`, `plant_property`)

Each name contains text, language and can be assigned for different entities.

To avoid code duplication we can create parent object which contains common field
and individual child tables for each entity type as in code below

```sql
-- language - it's table which was not described here
-- plant - it's table which was not described here
-- plant_property - it's table which was not described here

CREATE TABLE IF NOT EXISTS base_entity_name (
    id              SERIAL PRIMARY KEY,
    language_id     SMALLINT NOT NULL REFERENCES language(id),
    text            CHARACTER VARYING[107]
);

CREATE TABLE IF NOT EXISTS plant_name (
    plant_id            INTEGER NOT NULL REFERENCES plant(id)
) INHERITS (base_entity_name);

CREATE TABLE IF NOT EXISTS plant_property_name (
    plant_property_id   INTEGER NOT NULL REFERENCES plant_property(id)
) INHERITS (base_entity_name);
```

So simple example but it can illustrate this simple but powerful idea with inheritance in PostgreSQL.

# Problems

Inheritance can't add forigen keys from parent to child.

As result in our example we will hava table without forigen keys for language_id field and primary key for id field.


<br />
# Conclusion

So interesting approach to organzie schemas.
