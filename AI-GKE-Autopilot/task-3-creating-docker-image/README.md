# Creating `Docker-Image`

In this task, we are going to follow these steps:

1. Set the `PROJECT_ID` environment variable using:
```bash
export PROJECT_ID=<enter-your-project-id>
```
2. Change directory to `testing-app-locally` directory, using:
```bash
cd task-2-testing-app-locally/
```
2. Move Dockerfile from `creating-docker-image` to `testing-app-locally` directory, using:
```bash
mv ../task-3-creating-docker-image/Dockerfile .
```
3. Build the project's docker image using:
```bash
gcloud builds submit --tag gcr.io/$PROJECT_ID/foodclassifier .
```
4. Change back the directory to main using:
```bash
cd ../
```
