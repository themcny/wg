# Flask File System API

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
