Title: Full-text search in PostgreSQL
Date: 2022-06-04 21:00
Category: PostgreSQL
Tags: postgresql, full-text search
Author: Andrey G
Status: published
Summary: Full-text search in PostgreSQL
Lang: en
---

[TOC]

It is short note how we can use full-text search in PostgreSQL.

More details, as usual, in [documentation](https://www.postgresql.org/docs/current/textsearch.html) ;)

Yes :), I would like to have full-text search but directly in database without Elasticsearch, etc.

Here, we have table with text/ plant names, and we would like to do search and find plants by names.

```sql
CREATE TABLE IF NOT EXISTS plant_name (
    language_id     SMALLINT NOT NULL REFERENCES language(id),
    text            VARCHAR(255) NOT NULL,
    plant_id        INTEGER NOT NULL REFERENCES plant(id),
    PRIMARY KEY (language_id, plant_id)
);
```

it is our data, next we need search query and it can be implemented as below

```sql
SELECT *
FROM plant_name
WHERE
    to_tsvector('russian', "text") @@ plainto_tsquery('russian', 'Ель ''Хупс''')
    OR
    to_tsvector('english', "text") @@ plainto_tsquery('english', 'Ель ''Хупс''')
;
```

`to_tsvector` - parse and normalize a document string

`plainto_tsquery` - converting user-written text into a proper tsquery, alternative to_tsquery

`tsquery` - contains search terms, which must be already-normalized lexemes, and may combine multiple terms using AND, OR, NOT, and FOLLOWED BY operators

Also, we can specify language 'russian','english',... to indicate a more correct way to understand the data

## Increace performance with GIN index

For full-text search we can use [GIN, Generalized Inverted Index](https://www.postgresql.org/docs/current/gin-intro.html).

for "ru" names in the table we can create [partial](https://www.postgresql.org/docs/current/indexes-partial.html)
[expression](https://www.postgresql.org/docs/current/indexes-expressional.html)
[GIN](https://www.postgresql.org/docs/current/gin-intro.html) index

```sql
CREATE INDEX plant_name_idx_gin_text_ru
ON plant_name
USING GIN (to_tsvector('russian', "text"))
WHERE language_id = 1
;
```

and we should adjust our search query to use index:

```sql
SELECT *
FROM plant_name
WHERE
    (language_id = 1 AND
     to_tsvector('russian', "text") @@ plainto_tsquery('russian', 'Ель ''Хупс'''))
    OR
    ((language_id = 2 OR language_id = 3) AND
     to_tsvector('english', "text") @@ plainto_tsquery('english', 'Ель ''Хупс'''))
;
```

__Note__: Here we should use `language_id = 1`,`language_id = 1`,etc..., because we have only one table for all ru/en/la names
and we created our GIN intex as partial index and split data in tree indexes by `language_id` field.
Same partitionaing approach should be used in query to activate indexes.

# Limitations

I'm not sure what it is so good idea to keep full-text search in PostgreSQL when you have a lot of data.
But with limited amount of data and knowing that it's can't increase significantly it is useful approach.

# Conclusion

So simple, right?

Cool ability to have full-text search in database without external tools, without Elasticsearch, etc...

It works very fast for plant database. There'is not much data in this database,
we can keep these data/indexes completely in memory and have very fast search queries.
