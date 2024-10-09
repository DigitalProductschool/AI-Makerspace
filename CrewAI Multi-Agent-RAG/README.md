# Multi-Agent RAG System Using Crew AI for PDF and Tutorial Question Answering

This repository demonstrates the use of a Multi-Agent Retrieval-Augmented Generation (RAG) system leveraging Crew AI to streamline the process of answering tutorial-based queries across various online resources such as YouTube, GitHub, documentation websites, and PDFs. It is designed to help users quickly extract and compile relevant information from different sources to answer questions, thereby enhancing the learning experience and making it more efficient.

The repository includes two primary components:

1.	PDF Question Answering (QA): A multi-agent system to answer user queries from the document.

2.	Multi-Agent RAG System for Tutorial QA: A multi-agent system that retrieves information from multiple sources (YouTube, GitHub, documentation, and web search) and combines it to answer tutorial-related questions.

The repository requires several libraries to function. These can be installed from the `requirements.txt` file. This can be done using:

``````
pip install -r requirements.txt
``````

The repository is organised as follows:
``````
.
├── pdf_qa.ipynb          
├── tutorial_qa.ipynb     
├── requirements.txt   
├── .env              
└── README.md                   
``````

The `.env` file is used to store sensitive information such as API keys. It is not included in the repository for security reasons. However a template is provided `.

You will require a Github token and OpenAI API key to run the notebooks.

To generate the Github token, follow these steps:
1. Go to your GitHub settings.
2. Click on Developer settings.
3. Click on Personal access tokens.
4. Click on Generate new token.
5. Give your token a name and select the repo scope.
6. Click on Generate token.

To generate the OpenAI API key, follow these steps:
1. Go to the OpenAI website.
2. Click on the API section.
3. Click on Create new secret key.
4. Give your key a name and click on Create secret key.

Add these keys to the `.env` file.

### License:
This project is licensed under the MIT License. See the LICENSE file for details.