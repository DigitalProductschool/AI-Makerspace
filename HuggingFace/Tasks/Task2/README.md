
In this task, we would learning how can we write a python script which will download and save the desired model in local storage.(In our case we would be using t5-small model) 

- Go to the [huggingface.co/models](https://huggingface.co/models?sort=downloads)

- Filter and choose model for your use case.

- From the model's page we'll get the code from the docs to use it in transformer. 

- Writing a small python script to download and save the model locally. 

- - Within the script we would be using "save_pretrained("dir_name")" function to store the model in the specified directory.

Ex: **save-t5.py**. I am using this file to download and save the "t5-small" model which would be used for text summarization.

- Run the script to download and save the "t5-small" model
```bash
python save-t5.py
```