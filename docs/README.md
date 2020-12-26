## Start Development Server on Host Machine

```bash
# initialize and activate virtual environment, initialization only needs to be run once.
$ python3 -m venv venv
$ . venv/bin/activate
# install packages
$ pip install -r src/app/requirements.txt
# Set environment variables for current session, DB_CONNECTION_STRING is optional
$ export FLASK_APP=src/app/app.py; export FLASK_ENV=development; export FLASK_DEBUG=0; export APP_ENV=development; export DB_CONNECTION_STRING=mysql+mysqldb://root:password@localhost:3306/example_db?ssl=true;
# Start flask app
$ flask run
```

## Start Development Server in Docker Container

```bash
# build docker image
$ docker build -t flask-app -f ci/flask.Dockerfile .

# run container (provide your environment variables)
$ docker run -d --name flask-app -p 5000:80 -e APP_ENV="development" -e FLASK_ENV="development" -e DB_CONNECTION_STRING="mysql+mysqldb://username:password@host:3306/pub_workspaces?ssl=true" flask-app

# Confirm running by visitng
$ open http://localhost:5000

# Stop and remove container
$ docker rm -f flask-app
```

## Managing MySQL Database Schema

This template project can be run and deployed without connecting it to a MySQL instance. If you won't be persisting data just ignore this part and don't worry about setting `DB_CONNECTION_STRING`. If you will connect the application to a MySQL instance notes can be found under the persistence directory [README.md](../src/app/persistence/README.md).

## Deploy

TODO: Add deployment notes

## Additional Resources
[Creating a virtual environment (flask)](https://flask.palletsprojects.com/en/1.1.x/installation/#create-an-environment)

[More info on virtual environments and packages](https://docs.python.org/3.8/tutorial/venv.html)

[Flask docs](https://flask.palletsprojects.com/en/1.1.x/)