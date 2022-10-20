import pandas as pd
import yaml
import os 
import io

#loading the yaml file
params = yaml.safe_load(open("params.yaml"))['filter']

#reading the CSV
df = pd.read_csv("kaggle-merged-data/GlobalLand-MainTemperatures.csv", parse_dates=["Formatted Date"])

#I want all records where temp > value
df = df[df['Land Max Temperature (C)'] > params['value']]

#selecting 2 columns, priniting that by saving it in df
df = df[['Formatted Date', 'Land Max Temperature (C)', 'Country']]
print(df)

#saving the output in a file
os.makedirs(os.path.join("output", "filter"), exist_ok=True)
df.to_csv("output/filter/out.csv")
