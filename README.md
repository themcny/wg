# Flask File System API
Total Time Spent: 4 hours

### How to Run the Application

You can set the `WORK_DIR` environment variable (where `WORK_DIR` is the path to the file system):
```
WORK_DIR='path/to/file/system/' flask --app 'api:create_app("")' run
```

You can also pass the path to the file system as an argument to `create_app`
```
flask --app 'api:create_app("/path/to/file/system/")' run
```


### How to Test the Application

```
curl http://127.0.0.1:5000/
```


### How to Format the Application

```
yapf -i filename.py
```

### With More Time...
- Better testing
  - Figure out how to stub the `subprocess` module behavior to get more test coverage on logic in the parsing methods
  - Figure out how to properly stub HTTP requests/responses to write end-to-end tests on the endpoint
  - Figure out the best way to organize tests in the flask app. With more time I'd have a `tests/` directory with more tests in it.
- More robust error handling. It just handles a "Bad Request" type error when a user tries to GET a file/directory that doesn't exist. There are likely other errors that can/will pop up that should also be handled gracefully
