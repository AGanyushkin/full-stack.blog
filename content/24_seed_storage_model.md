Title: SEED storage model
Date: 2022-06-11 21:00
Category: SEED Project
Tags: postgresql, logical schema, physical schema
Author: Andrey G
Status: published
Summary: PostgreSQL storage model. concept, logical schema, physical schema
Lang: en
---

In this post I'm going to describe database schema which I will use in my pet project  "SEED".

[GitHub, all sources are available here](https://github.com/AGanyushkin/seed-storage)

### Storage should contains / describe the following data entities:

Main entities

- `plant` - plant, images for plant, plant-set, text for plant
- `plant-property` - structured view for plant properties

Optional entities

- `account` - account tracking. will be used with OpenID and external providers
- `favorite` - track favorite entries
- `message` - user should be able to coment plants and plant-sets

### Some reasons
- I'm going to put all data in one PostgreSQL datastore because:

    - Reducing the complexity of the solution
    - Documentation and strict data schema which reduces the number of errors and reduces the time to remember what I did

- Plant properties was designed in relation model (not in json)
because it's important for me to have strict schema and avoid additional documentation.


# Consept

It is high level concept schema to illustrate my needs.

![seed plant storage concept](/images/plant_storage_concept.png){: .image-process-big-article-image}

I've used different colors to split different subject areas on schema.


# Logical model

[seed storage logical schema
    ![seed storage logical schema](/images/plant_storage_logic.png){: .image-process-big-article-image}
](/images/plant_storage_logic.png)

In this model I've splitted important and service properties (for example in `account` & `account_profile`) to
increase performance for SQL requests which are used `account`.

A lot of tables was used to describe `plant-properties`. Maybe JSON will be more compact.


# Physical model

This model was implemented for PostgreSQL. There is nothing unique in this implementation and you can find whole code in [GitHub](https://github.com/AGanyushkin/seed-storage).

Sadly, but table inheritance can't be used because we will miss all keys and relations in child tables from parent. [more details](/postgresql-table-inheritance.html)

Some examples:
```SQL
CREATE TABLE IF NOT EXISTS language (
    id              SMALLSERIAL PRIMARY KEY,
    name            VARCHAR(13) NOT NULL UNIQUE CHECK ( char_length(name) > 1 ),
    tag             VARCHAR(3) NOT NULL UNIQUE CHECK ( char_length(tag) > 1 )
);

CREATE TABLE IF NOT EXISTS plant (
    id              SERIAL PRIMARY KEY,
    global_id       UUID NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS plant_name (
    language_id     SMALLINT NOT NULL REFERENCES language(id),
    text            VARCHAR(255) NOT NULL,
    plant_id        INTEGER NOT NULL REFERENCES plant(id),
    PRIMARY KEY (language_id, plant_id)
);

CREATE TABLE IF NOT EXISTS plant_name_alias (
    id              BIGSERIAL PRIMARY KEY,
    language_id     SMALLINT NOT NULL REFERENCES language(id),
    text            VARCHAR(255) NOT NULL,
    plant_id        INTEGER NOT NULL REFERENCES plant(id),
    UNIQUE (language_id, text)
);
```

<br />
# Conclusion

This schema can be used in project, but there is still some bugs can exists in it.

Also, good idea to add test-data for this schema description. It can make it easy to use in dev and investigations.
