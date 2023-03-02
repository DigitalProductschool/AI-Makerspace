"""Preprocess and convert CSV data to JSON format for use in fine-tuning a GPT model.

This script contains a class that can be used to convert CSV files to JSON files, by reading data from a CSV file,
converting each row to a dictionary, and writing the dictionaries to a JSON file as separate lines. The resulting
JSON file can then be used to fine-tune a GPT model.
"""

import configargparse
import os
import csv
import json
import subprocess
#import openai

class CSVConverter:
    def __init__(self, csv_file, prompt_column, completion_column):
        self.csv_file = csv_file
        self.prompt_column = prompt_column
        self.completion_column = completion_column

    def read_csv(self):
        """Read data from a CSV file and return a list of dictionaries.

        Each dictionary represents a row in the CSV file, with the keys being the column names
        and the values being the cell values.
        """
        with open(self.csv_file, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = []
            for row in csv_reader:
                data.append({
                    "prompt": row[self.prompt_column] + " ->",
                    "completion": " " + row[self.completion_column] + "."
                })
        return data

    def write_json(self, data, file_path):
        """Write a list of dictionaries to a JSON file.

        Each dictionary is written as a separate line in the JSON file.

        Parameters:
        data (list): A list of dictionaries to write to the file.
        file_path (str): The path to the JSON file.
        """
        with open(file_path, 'w') as json_file:
            for item in data:
                json.dump(item, json_file)
                json_file.write('\n')

    def convert(self):
        """Convert a CSV file to a JSON file.

        The JSON file will contain a list of dictionaries, where each dictionary represents a row
        in the CSV file, with the keys being the column names and the values being the cell values.
        """
        file_name, file_extension = os.path.splitext(os.path.basename(self.csv_file))
        dir_name = os.path.dirname(self.csv_file)
        json_file = os.path.join(dir_name, "converted_" + file_name + ".json")
        data = self.read_csv()
        self.write_json(data, json_file)
        return json_file

def prepare_data(json_file):
    cmd = ["openai", "tools", "fine_tunes.prepare_data", "-f", json_file]
    subprocess.run(cmd)           

if __name__ == "__main__":
    p = configargparse.ArgumentParser(description="Preprocess data", default_config_files=['config.ini'])
    p.add_argument("-c", "--config", is_config_file=True, help="Config file path")
    p.add_argument("--csv-file", required=True, help="Path to the CSV file")
    p.add_argument("--prompt-column", required=True, help="Name of the column containing the prompts")
    p.add_argument("--completion-column", required=True, help="Name of the column containing the completions")
    args = p.parse_args()

    # Example usage
    converter = CSVConverter(args.csv_file, args.prompt_column, args.completion_column)
    json_file = converter.convert()
    prepare_data(json_file)