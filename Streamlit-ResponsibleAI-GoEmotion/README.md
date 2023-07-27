---
license: apache-2.0
title: GoEmotions Dashboard
sdk: streamlit
sdk_version: "1.22.0"
app_file: app.py
---

# GoEmotions Dashboard - Analyzing Emotions in Text

This is a Python script that uses Streamlit, Plotly, and the Hugging Face Inference API to create a web-based dashboard for analyzing emotions in text. Finally this dashboard is deployed on Hugging Face Spaces using GitHub Actions.

## Pre-requisites:

- Python 3.7 or higher

## Project Structure:
```dir
GoEmotions/
├── app.py
├── requirements.txt
├── .env
├── README.md
├── assets/
└── .github/workflows
```

## Setup

`Step 1` - Clone this repository to your local machine using the following command, or open the repository in GitHub Codespaces.

```bash
git clone https://github.com/devansh-srivastav/GoEmotions.git
```

`Step 2` - Navigate to the root directory of the project.

```bash
cd GoEmotions
```

`Step 3` - Create and activate a new python virtual environment: (This step can be skipped if working on GitHub Codespaces!)

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

`Step 4` - Install the required packages using pip: (This step can be skipped if working on GitHub Codespaces as it automatically installs the requirements!)

```bash
pip install -r requirements.txt
```

`Step 5`- Create a free account on the [Hugging Face website](https://huggingface.co/) and generate an API key (read).

`Step 6`

- Create a `.env` file in the root directory of the project and add your
- Hugging Face API key like this: `HF_API_KEY=<your_api_key_here>`

`Step 7` - Run the Streamlit app.

```bash
streamlit run app.py
```

or 

```bash
python -m streamlit run app.py
```

- If you want to run this application on GitHub Codespaces, you will need to add the following flags to the `streamlit run` command:

```bash
python -m streamlit run app.py --server.enableCORS false --server.enableXsrfProtection false
```

## Deployment to Spaces (CI/CD)

`Step 1`
Commit your code and push it to your GitHub repository

`Step 2`
Create a new Space on Hugging Face, add it as an additional remote to git and force push your code on Spaces:

```bash
git remote add space https://huggingface.co/spaces/HF_USERNAME/SPACE_NAME
```

```bash
git push --force space main
```

`Step 3`
In the main.yml, add your Hugging Face username and Space name to the variables 'HF_username' and 'HF_space_name'

`Step 4`
Create a new API key on Hugging Face (write) and add it as a secret to your GitHub Repository naming it as 'HF_TOKEN'.

`Step 5`
Trigger the CI/CD pipeline by a push or a pull request to your main branch.

## Usage:

- A web-based dashboard will open in your default browser.
- Type or paste a text input in the text box provided.
- The dashboard will visualise the detected emotions in a set of gauges, with each gauge representing the intensity of a specific emotion category. The gauge colors are based on a predefined color map for each emotion category.
- Moreover, the dashboard will display the results from Hate Speech Analysis and Sexism Detection models. 
