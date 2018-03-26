# C# Coding Guidelines
As used in "Pro C# 7 by Andrew Troelsen and Philip Japiske"

# Database Naming Conventions
### Tablenames start with Capital, subwords Capital as well
Ex: Use "FirstName"

### column_names 
Column names that are comprised of multiple words should be separated by underscores (ie. snake_case)
Ex: Use word_count or team_member_id, not wordcount or wordCount

### Full words, not abbreviations
Object names should be full English words. In general avoid abbreviations, especially if they're just the type that removes vowels. Most SQL databases support at least 30-character names which should be more than enough for a couple English words. PostgreSQL supports up to 63-character for identifiers.

### Singular Relations
Tables, views, and other relations that hold data should have singular names, not plural. This means our tables and views would be named team, not teams.

### Key Fields
Primary Keys: always "id"
Foreign key : fields should be a combination of the name of the referenced table and the name of the referenced fields. For single column foreign keys (by far the most common case) this will be something like foo_id.

### Indexes
Indexes should be explicitly named and include both the table name and the column name(s) indexed. Including the column names make it much easier to read through SQL explain plans. If an index is named foobar_ix1 then you would need to look up what columns that index covers to understand if it is being used correctly.

## Examples
CREATE TABLE Person (
  id            bigint PRIMARY KEY,
  full_name     text NOT NULL,
  birth_date    date NOT NULL);

CREATE TABLE TeamMember (
  id       bigint NOT NULL REFERENCES team(id),
  person_id     bigint NOT NULL REFERENCES person(id),
  CONSTRAINT team_member_pkey PRIMARY KEY (team_id, person_id));


