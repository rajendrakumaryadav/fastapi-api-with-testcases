### FastAPI Project

This is a FastAPI project that uses the following technologies:
- FastAPI - for the API framework
- SQLAlchemy - for ORM
- SQLite - for in-memory database
- Starlette TestClient - for testing API endpoints

### How to run the project
```bash
uvicorn main:app --reload
```


### How to run the tests
```bash
pytest  -v **/tests*.py
```
* Remove the -v flag to run the tests without the verbose mode
#### OR
```bash
nose2 -v
```
* Remove the -v flag to run the tests without the verbose mode