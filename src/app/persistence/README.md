# Persistence
Before following these notes - make sure you have access to an up and running [MySQL server](https://dev.mysql.com/) (running the project using docker automatically starts mysql server via docker). For the application to have access to the database in a development or production environment, DB_CONNECTION_STRING must be set on your system. You can set the variable for the current shell session with the `export` keyword. Build your connection string using the format shown.

```bash
# set DB_CONNECTION_STRING
$ export DB_CONNECTION_STRING=mysql+mysqldb://root:password@localhost:3306/flask?ssl=true&charset=utf8mb4
```

This flask app uses SQLAlchemy to manage access to the database tables and its records with the sqlalchemy orm. It also uses alembic to generate and version the database schema. The app is setup with an `example_entity.py` to display the usage of programmatically setting up a database table and its columns so the file should be deleted. More usage info can be found in the [object relational tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html) on SQLAlchemy documentation.

Each database table corresponds to a `*_entity.py` class in [entities directory](./entities). To add, remove, or modify a table you can create, delete, or update the corresponding `*_entity.py` file. Once you've made changes to these files you must use alembic commmands to generate migration files. These files are used to make changes to the database schema. Please review alembic migration for an in depth explanation of what the commands do, below are only commands to generate a new migration and upgrade the db schema.

For the --autogenerate flag to work, each individual entity must be imported into [env.py](./migrations/env.py). Otherwise an empty migration is generated and you must fill in the details.
## Migration Commands
If application is running in docker container prepend commands with `docker exec -it flask-app`
```bash
# from repo root
# create new migration
$ python3 -m alembic.config -c src/app/persistence/migrations/alembic.ini revision --autogenerate -m "delete me"
# update database
$ python3 -m alembic.config -c src/app/persistence/migrations/alembic.ini upgrade head

```

---
**NOTES**

If referencing the docs - ensure you are viewing correct version.

- [sqlalchemy documentation](https://www.sqlalchemy.org/)
- [alembic documentation](https://alembic.sqlalchemy.org/en/latest/)

---