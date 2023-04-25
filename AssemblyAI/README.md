# Assembly AI
Assembly AI is a tool which provides APIs to play around with audio, video and transcriptions. I'll be using some of these APIs in this project.

For this repo, I have added the features of Summarization, Entity Detection and Sentiment Analysis. You can check out more in the Assembly AI documentation.

## Requirements

```console
$ pip install requests
```

### Assembly AI Installation
If you have Homebrew
```console
$ brew tap assemblyai/assemblyai
$ brew install assemblyai
```

If you don't have Homebrew
```console
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/AssemblyAI/assemblyai-cli/main/install.sh)"
```

## How to Run

Set API Key as an environment variable
```console
$ export AAI_API_KEY=<YOUR_API_KEY>
```

`NOTE` You can get your API Key after signing in to your Assembly AI account and viewing the Dashboard

If your AssemblyAI API key is stored as an environment variable called `AAI_API_KEY` file, then you can omit the optional `--api_key` argument.

```console
$ python transcribe.py audio_file [--local] [--api_key=<YOUR-API-KEY>]
```

Example for hosted file:

```console
$ python transcribe.py https://bit.ly/3qDXLG8 [--api_key=<YOUR-API-KEY>]
```

Example for local file:

```console
$ python transcribe.py audio.mp3 --local [--api_key=<YOUR-API-KEY>]
```

## Sample Output
As mentioned above, this program only gives output for the Summarization, Entity Detection and Sentiment Analysis features of Assembly AI.

```
Here is the summary for the input transcript:
AssemblyAI is a deep learning company that builds powerful APIs to help you transcribe and understand audio. The most common use case for the API is to automatically convert prerecorded audio and video files into text transcriptions. Every day, developers are using these features to build really exciting applications.

The following table represents all entities present in the transcript:
    entity_type                        text  count
0         event          State of the Union      1
1         event  State of the Union address      4
2    occupation                        deep      1
3    occupation                  developers      1
4  organization                          AI      1
5  organization                  AssemblyAI      3
6  organization          team of developers      1
7   person_name                       Biden      2
8   person_name                   Joe Biden      1

The following represents a count of sentences in the transcript with a sentiment:
  sentiment  count
0  NEGATIVE      1
1   NEUTRAL     12
2  POSITIVE      9
```
