- Have Python installed on your machine

- Install all the dependencies

```bash
pip install -r requirements.txt
```

- Download and save the huggingface model

```bash
python save-t5.py
```

- Start the server(running a single process.)

```bash
uvicorn inference:app --host 0.0.0.0 --port 80 --reload
```

- When deploying application you will probably want to have some replication of processes to take advantage of multiple cores and to be able to handle more requests.

```bash
gunicorn inference:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80
```

the colon in **"inference:app"** would be equivalent to the Python import part in `from main import app`.

**--workers:** The number of worker processes to use, each will run a Uvicorn worker, in this case, 4 workers.

**--worker-class:** The Gunicorn-compatible worker class to use in the worker processes.

- Server started on PORT: 80
- Read and test API documentation at **"http://localhost:80/docs/"**

## Build and run the docker image

```bash
docker build -t inference .
```

```bash
docker run -d -p 80:80 inference
```

**Note**: In the container you are using port 80 and you are forwarding that port to host machine's 80 port
