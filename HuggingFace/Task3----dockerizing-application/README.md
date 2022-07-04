# Dockerizing the application

- Make sure you have **Docker Desktop** installed and running.

- Build the Docker image

```bash
docker build -t inference .
```

- Run the Docker container

```bash
docker run -d -p 80:80 inference
```
