# Persistence
Database tables correspond to a `*_entity.py` class in [entities directory](./entities). To add, remove, or modify a table you can create, delete, or update the corresponding `*_entity.py` file. Database versioning is managed with alembic. I only included 2 key migration commands for modifying the db schema. Please review alembic migration for an in depth explanation of what the commands do.

Ensure the db connection string is set and accessible via `os.environ['DB_CONNECTION_STRING']`. Format should match `sqlalchemy.url` found in [alembic.ini](./migrations/alembic.ini).
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