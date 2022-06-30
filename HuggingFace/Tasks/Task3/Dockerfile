FROM python:3.9.13-slim-bullseye

EXPOSE 80
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Define the working directory
WORKDIR /app

# Copy requirements.txt to the Docker container
COPY requirements.txt .

# Install the dependencies
RUN python -m pip install --no-cache-dir -r requirements.txt

# Copy all the files to the container
COPY . /app

# Download and save the model inside the container
RUN python save-t5.py

# Run the application server
CMD gunicorn inference:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80 --timeout 120
