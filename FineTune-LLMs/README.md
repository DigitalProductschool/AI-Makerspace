# FineTuning Large Language Models (LLMs) Workshop

This repository contains two notebooks that guide you through the process of fine-tuning a large language model (LLM) and deploying it using AWS SageMaker.

## Getting Started

### Step 1: Fine-Tuning the Model

**Notebook**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DigitalProductschool/AI-Makerspace/blob/master/FineTune-LLMs/FineTune-LLAMA2-with-QLORA.ipynb)

#### Instructions

- This notebook is adapted from this repository: [LLM-Finetuning](https://github.com/ashishpatel26/LLM-Finetuning).
- Fine-tune the model based on a domain-specific dataset.

#### Dataset

The dataset used for fine-tuning is sourced from Hugging Face and focuses on Articles of the Constitution. This dataset contains instruction-input-output pairs on Indian Constitutional Law, specifically addressing Articles 12, 14, 19, 21, and 15. It's designed to assist AI models, researchers, and learners in understanding and generating responses to complex legal questions related to the Indian Constitution. You can view the dataset [here](https://huggingface.co/datasets/nisaar/Articles_Constitution_3300_Instruction_Set/viewer/nisaar--Articles_Constitution_3300_Instruction_Set/train).

### Step 2: Deploying the Model

1. **Create a SageMaker Instance**: Navigate to AWS SageMaker and create a new notebook instance. Choose the instance type as `ml.g4dn.2xlarge` which comes with 1 Tesla T4 GPU.

2. **Access the Instance**: Once the instance is ready, open it to access the Jupyter Notebook interface.

3. **Upload Notebook and Outputs Folder**: Use the Jupyter Notebook interface to upload the `FineTune-LLMs/Deploy-LLAMA2-on-SageMaker.ipynb` notebook and the `outputs` folder created in the first step.

4. **Run the Notebook**: Open the uploaded notebook and run all the cells to deploy the model.
