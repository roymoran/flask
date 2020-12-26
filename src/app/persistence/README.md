# Persistence
Before following these notes - make sure you have access to an up and running [MySQL server](https://dev.mysql.com/).

For the application to have access to the database, DB_CONNECTION_STRING must be set on your system. You can set the variable for the current shell session with `export` keyword. Build your connection string using the format shown.

```bash
# set DB_CONNECTION_STRING
$ export DB_CONNECTION_STRING=mysql+mysqldb://root:password@localhost:3306/example_db?ssl=true
```

All database tables correspond to a `*_entity.py` class in [entities directory](./entities). To add, remove, or modify a table you can create, delete, or update the corresponding `*_entity.py` file. Database versioning is managed with alembic. I only included 2 key migration commands for modifying the db schema. Please review alembic migration for an in depth explanation of what the commands do.
## Migration Commands

```bash
# from repo root
# create new migration
$ python3 -m alembic.config -c src/app/persistence/migrations/alembic.ini revision --autogenerate -m "comment for revision"
# update database
$ python3 -m alembic.config -c src/persistence/migrations/alembic.ini upgrade head

```

---
**NOTES**

- [alembic documentation](https://alembic.sqlalchemy.org/en/latest/)

---