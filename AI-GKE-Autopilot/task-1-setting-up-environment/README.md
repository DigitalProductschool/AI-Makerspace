# Setting-up Environment

In this task, we are going to set up a working environment for our project using the following steps:

1. Open Google Cloud Console using this [link](https://console.cloud.google.com/)

2. Activate Cloud Shell using:
```bash
gcloud auth list
```

3. Confirm the project ID using:
```bash
gcloud config list project
```

3. Enable the `Google Kubernetes Engine (GKE) API` using:
```bash
gcloud services enable container.googleapis.com
```

4. Installing `subversion` linux package using:
```bash
sudo apt-get install -qq subversion
```

5. Fetching the AI-GKE-Autopilot dir from AI-Makerspace Repository using:
```bash
svn -q checkout "https://github.com/alihussainia/AI-Makerspace/trunk/AI-GKE-Autopilot"
```

6. Change to the `AI-GKE-Autopilot` directory using:
```bash
cd AI-GKE-Autopilot
```

7. Set the `WORKING_DIR` environment variable using:
```bash
export WORKING_DIR=$(pwd)
```