# Use the official Python image as the base image
FROM python:3.10

# Set the working directory to the location of your application files
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the dependencies in the container
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files to the container
COPY . .

# Expose the port that your application is running on
EXPOSE 5000

# Define the command to run when the container starts
CMD ["python", "fastapi_app.py", "-c", "assistant_config.ini"]
