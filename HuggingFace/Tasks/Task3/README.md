- Create the Dockerfile

- And run the python script in it, inorder to install the model inside your Docker image

- Build the docker image and test it out locally

```bash
docker build -t inference .
```

```bash
docker run -d -p 80:80 -e **CHOKIDAR_USEPOLLING**=true inference:latest
```
