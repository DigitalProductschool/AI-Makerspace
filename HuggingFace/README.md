# Abstractive Text Summarization using HuggingFace🤗

Abstractive summarizers are so-called because they do not select sentences from the originally given text passage to create the summary. Instead, they produce a paraphrasing of the main contents of the given text, using a vocabulary set different from the original document. 

### Goal
In this project we are building Abstractive Text Summarization app using HuggingFace, a data science platform that provides tools that enable users to build, train and deploy ML models based on open source (OS) code and technologies.

### Deployed App
After completing all the tasks your deployed text summarizing **API** will look like this: [Click here for live demo](http://35.242.170.185/docs)

### Project Structure

- inference.py
- models.py
- save-t5.py
- Dockerfile
- requirements.txt
- deployment.yaml
- .github/workflows
  - ai.yml
  - build-and-deploy.yml
  
### Project Requirements 
- Python3
- git
- Docker desktop

### Project Steps

- `Step 1`: Cloning the repo

```bash
git clone https://github.com/DigitalProductschool/AI-Makerspace.git
```

 
- `Step 2`: Changing working directory to HuggingFace

```bash
cd AI-Makerspace/HuggingFace/
```
 
- `Step 3`: Installing dependencies using pip3
 
```bash
pip3 install -r requirements.txt
```
 
- `Step 4`: Downloading the HuggingFace model
 
```bash
python3 save-t5.py
```
 
- `Step 5`: Running uvicorn server

```bash
python3 -m uvicorn inference:app --host 0.0.0.0 --port 80 --reload
```

Go to "/docs" route to test the api. 
 
 
 - `Step 6`(Optional): Running the server with multiple worker processess.

```bash
python3 -m gunicorn inference:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80
```

- `Step 7`: Building the Docker image

```bash
docker build -t inference .
```

- `Step 8`: Running the Docker container

```bash
docker run -d -p 80:80 inference
```

- `Step 9`: Update YAML manifests according to your project

### Sample I/O 
- Test input:
```bash
The US has passed the peak on new coronavirus cases, President Donald Trump said and predicted that some states would reopen this month.The US has over 637,000 confirmed Covid-19 cases and over 30,826 deaths, the highest for any country in the world.At the daily White House coronavirus briefing on Wednesday, Trump said new guidelines to reopen the country would be announced on Thursday after he speaks to governors.We’ll be the comeback kids, all of us,he said. We want to get our country back.The Trump administration has previously fixed May 1 as a possible date to reopen the world’s largest economy, but the president said some states may be able to return to normalcy earlier than that.
```

- Test output: 
```bash
the president predicts some states will reopen this month . the country has over 637,000 confirmed cases and over 30,826 deaths . he said new guidelines will be announced on Thursday .
```
