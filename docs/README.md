## Start Development Server
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
## Managing MySQL Database Schema
This template project can be run and deployed without connecting it to a MySQL instance. If you won't be persisting data just ignore this part and don't worry about setting `DB_CONNECTION_STRING`. If you will connect the application to a MySQL instance notes can be found under the persistence directory [README.md](../src/app/persistance/README.md).

## Additional Resources
(Creating a virtual environment (flask))[https://flask.palletsprojects.com/en/1.1.x/installation/#create-an-environment ]
(Virtual Environments and Packages)[https://docs.python.org/3.8/tutorial/venv.html]