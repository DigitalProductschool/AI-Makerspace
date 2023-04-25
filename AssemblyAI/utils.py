import requests
import time
import pandas as pd


upload_endpoint = "https://api.assemblyai.com/v2/upload"
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"


# Helper for `upload_file()`
def _read_file(filename, chunk_size=5242880):
    with open(filename, "rb") as f:
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            yield data


# Uploads a file to AAI servers
def upload_file(audio_file, header):
    upload_response = requests.post(
        upload_endpoint,
        headers=header, data=_read_file(audio_file)
    )
    return upload_response.json()


# Request transcript for file uploaded to AAI servers
def request_transcript(upload_url, header):
    transcript_request = {
        'audio_url': upload_url['upload_url'],
        # 'auto_chapters': True,
        "summarization": True,
        "summary_model": "informative",
        "summary_type": "paragraph",
        "entity_detection": True,
        "sentiment_analysis": True
    }
    transcript_response = requests.post(
        transcript_endpoint,
        json=transcript_request,
        headers=header
    )
    return transcript_response.json()


# Make a polling endpoint
def make_polling_endpoint(transcript_response):
    polling_endpoint = "https://api.assemblyai.com/v2/transcript/"
    polling_endpoint += transcript_response['id']
    return polling_endpoint


# Wait for the transcript to finish
def wait_for_completion(polling_endpoint, header):
    while True:
        polling_response = requests.get(polling_endpoint, headers=header)
        polling_response = polling_response.json()

        if polling_response['status'] == 'completed':
            return polling_response

        time.sleep(5)


# Get the paragraphs of the transcript
def get_paragraphs(polling_endpoint, header):
    paragraphs_response = requests.get(polling_endpoint + "/paragraphs", headers=header)
    paragraphs_response = paragraphs_response.json()

    paragraphs = []
    for para in paragraphs_response['paragraphs']:
        paragraphs.append(para)

    return paragraphs


# Print the chapters of the transcript
def get_chapters(polling_response):
    return polling_response['chapters']


# Print the summary of the transcript
def get_summary(polling_response):
    summary = polling_response['summary']
    print('Here is the summary for the input transcript:')
    print(summary)
    print()


# Print the entities of the transcript
def get_entities(polling_response):
    entities = polling_response['entities']
    df = pd.DataFrame(entities)
    df = df[['entity_type','text']]
    df = df.groupby(['entity_type','text']).text.agg('count').to_frame('count').reset_index()
    print('The following table represents all entities present in the transcript:')
    print(df)
    print()


# Print the sentiment statistics of the transcript
def get_sentiments(polling_response):
    sentiments = polling_response['sentiment_analysis_results']
    df = pd.DataFrame(sentiments)
    df = df[['sentiment']]
    df = df.groupby(['sentiment']).sentiment.agg('count').to_frame('count').reset_index()
    print('The following represents a count of sentences in the transcript with a sentiment:')
    print(df)
    print()