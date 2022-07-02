- Run the script to download and save the huggingface model.(t5 model will be used in this case)

```bash
python save-t5.py
```

- Start the FastApi server

```bash
uvicorn inference:app --host 0.0.0.0 --port 80 --reload
```

- Read the docs and test out the application at: **0.0.0.0/docs**

#

**Bonus:**
When deploying application you will probably want to have some replication of processes to take advantage of multiple cores and to be **able to handle more requests.**

- Start the server with multiple worker processess.

```bash
gunicorn inference:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80
```
