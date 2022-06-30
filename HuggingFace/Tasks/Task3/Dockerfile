FROM python:3.9.13-slim-bullseye

EXPOSE 80
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .

RUN python -m pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY . /app

RUN python save-t5.py

CMD gunicorn inference:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80 --timeout 120
