# Finetuned GPT-3 Virtual Assistants

"Finetuned GPT-3 Virtual Assistants" is an open-source project that enables the creation of virtual assistants for websites or applications using GPT-3. The project includes a script for fine-tuning GPT-3 on a dataset, as well as a web interface for integrating the finetuned model into applications. By using this project, a virtual assistant with the ability to understand and respond to natural language queries can be created.

## Requirements

* Python 3.6 or higher
* OpenAI API key (sign up for one at https://beta.openai.com/)
* The following Python packages:
    ```bash
    - openai
    - configargparse
    - flask
    ```

## File Structure

```bash
finetuned_gpt3_virtual_assistants/
├── datasets/
│   └── Mental_Health_FAQ/
│       └── Mental_Health_FAQ.csv
├── templates/
│   └── index.html
├── .gitignore
├── assistant_config.ini
├── config.ini
├── flask_app.py
├── LICENSE
├── pre_process.py
├── README.md
└── requirements.txt
```

## API Key

To use the OpenAI API, you will need an API key. You can sign up for a free API key at https://beta.openai.com/.

## Usage:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/mahmoudfazeli/finetuned_gpt3_virtual_assistants.git
```

2. Navigate to the project directory:

```bash
cd finetuned_gpt3_virtual_assistants
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. (Optional) Create a `config.ini` file in the root directory with the following structure:

```bash
[preprocess]
csv-file = <path to csv file>
prompt-column = <name of column containing prompts>
completion-column = <name of column containing completions>
```

5. If you created the `config.ini` file, you can run:

```bash
python pre_process.py -c config.ini
```

alternatively, you can run:

```bash
python pre_process.py --csv-file <path to csv file> --prompt-column <name of column containing prompts> --completion-column <name of column containing completions
```

The script will create a JSON file called `converted_<original file name>.json` in the same directory as the CSV file. This JSON file will contain a list of dictionaries, where each dictionary represents a row in the CSV file, with the keys being the column names and the values being the cell values. This JSON file can then be used to fine-tune a GPT model.

6. The following assumes you've already prepared training data following the above instructions.
Start your fine-tuning job using the OpenAI CLI:

```bash
openai api fine_tunes.create -t <TRAIN_FILE_ID_OR_PATH> -m <BASE_MODEL>
```

7. Create a config file named `assistant_config.ini` and specify the assistant's name and identity. For example:

```bash
[ASSISTANT]
model_name = davinci:ft-personal-2023-01-11-15-48-39
assistant_name = Dr. Bot
description = Dr. Bot is a friendly and helpful virtual mental health assistant Bot who can always offer support and guidance. Dr. Bot is non-judgmental and patient, providing comfort and understanding to anyone who seeks his help. Dr. Bot is knowledgeable and understanding, and strives to provide the best advice and support possible.
```

8. Run the following script to start the Flask web server:

```bash
python flask_app.py -c assistant_config.ini
```

10. Open a web browser and go to http://localhost:5000 to access the chatbot interface.


## Contact

If you have any questions or suggestions about this project, please don't hesitate to send an email to mahmoudfazeli89@gmail.com.