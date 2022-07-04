# Downloading the large pretrained ai model for summarisation

- Run the script to download and save the huggingface model.(t5 model will be used in this case)

```bash
python save-t5.py
```

- Start the FastApi server

```bash
uvicorn inference:app --host 0.0.0.0 --port 80 --reload
```

- Read the docs and test out the application at: **0.0.0.0/docs**

- **Test input:** "The US has passed the peak on new coronavirus cases, President Donald Trump said and predicted that some states would reopen this month.The US has over 637,000 confirmed Covid-19 cases and over 30,826 deaths, the highest for any country in the world.At the daily White House coronavirus briefing on Wednesday, Trump said new guidelines to reopen the country would be announced on Thursday after he speaks to governors.We’ll be the comeback kids, all of us,he said. We want to get our country back.The Trump administration has previously fixed May 1 as a possible date to reopen the world’s largest economy, but the president said some states may be able to return to normalcy earlier than that."

- **Test output:** "the president predicts some states will reopen this month . the country has over 637,000 confirmed cases and over 30,826 deaths . he said new guidelines will be announced on Thursday ."

#

**Bonus:**
When deploying application you will probably want to have some replication of processes to take advantage of multiple cores and to be **able to handle more requests.**

- Start the server with multiple worker processess.

```bash
gunicorn inference:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80
```
