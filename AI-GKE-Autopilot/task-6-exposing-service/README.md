# Exposing Service
In task-7, we are going to follow these steps:

1. Expose the application using:
```bash
k create -f $WORKING_DIR/task-6-exposing-service/service.yaml
```
2. Watch the service status using:
```bash
k get svc --watch
```