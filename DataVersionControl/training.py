import pandas as pd
import yaml
import os
import io
import sys


params = yaml.safe_load(open("params.yaml"))['training']  

data_path = sys.argv[1]+"/out.csv"

df = pd.read_csv(data_path, parse_dates=["Formatted Date"])

#will pick only a few rows, based on what is defined in params file
df = df.head(params['num_rows'])  
print(df)

#mean global warming temp
mean = df['Land Max Temperature (C)'].mean()
print(mean)

os.makedirs(os.path.join("output", "training"), exist_ok=True)
output_training = os.path.join("output", "training", "out.tsv")
with io.open(output_training, "w", encoding="utf8") as fd_out_training:
    fd_out_training.write(str(mean))





