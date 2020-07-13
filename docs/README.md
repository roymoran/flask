# Additional notes

## Create database schemas
Set DB_CONNECTION_STRING as system environment variable so that it is read via `os.environ['DB_CONNECTION_STRING']`. Then run schema.py as module by running `python3 -m src.app.persistence.schema schema.py`. Alternativly update DB_CONNECTION_STRING inside launch.json and run config via VS Code debug tab. 

Logic in schema.py can be updated to perform other actions on db.