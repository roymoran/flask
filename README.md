# Quick Flask
Bare minimum production ready flask app built on docker image, uwsgi configuration, azure devops build templates, and basic dependencies.

## Requirements.txt
- Flask v1.1.2
- SQLAlchemy v1.3.18
- Pylint v2.5.3
- Pytest v5.4.3
- And their dependencies

## Build and Run
```bash
# build docker image
$ docker build -t quick-flask -f ci/flask.Dockerfile .

# run container (provide your environment variables)
$ docker run -d --name quick-flask -p 5000:80 -e DB_CONNECTION_STRING="mysql+mysqldb://username:password@host:3306/pub_workspaces?ssl=true" -e APP_ENV="development" quick-flask

# Confirm running by visitng
$ open http://localhost:5000

# Stop and remove container
$ docker rm -f quick-flask
```

## Deploy

## References 
- [MySQL SQLAlchemy Docs](https://docs.sqlalchemy.org/en/13/dialects/mysql.html)