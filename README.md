# Flask
Bare minimum production ready flask app built on docker image, uwsgi configuration, azure devops build templates, and basic dependencies.

## Requirements.txt
- Flask v1.1.2
- SQLAlchemy v1.3.18
- Pylint v2.5.3
- Pytest v5.4.3
- mysqlclient v2.0.1
- pytest-cov v2.10.0
- And their dependencies

## Build and Run
```bash
# build docker image
$ docker build -t flask-app -f ci/flask.Dockerfile .

# run container (provide your environment variables)
$ docker run -d --name flask-app -p 5000:80 -e DB_CONNECTION_STRING="mysql+mysqldb://username:password@host:3306/pub_workspaces?ssl=true" -e APP_ENV="development" -e FLASK_ENV="development" flask-app

# Confirm running by visitng
$ open http://localhost:5000

# Stop and remove container
$ docker rm -f flask-app
```

## Deploy

## References 
- [Flask Docs](https://flask.palletsprojects.com/en/1.1.x/)
- [MySQL SQLAlchemy Docs](https://docs.sqlalchemy.org/en/13/dialects/mysql.html)
