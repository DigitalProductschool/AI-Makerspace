from fastapi import FastAPI, Request, Response
from fastapi.responses import PlainTextResponse
import json
import openai
import os
import configargparse
import uvicorn
from jinja2 import Template

app = FastAPI()
openai.api_key = os.environ["OPENAI_API_KEY"]
if not openai.api_key:
    raise ValueError("Please provide an API key in the environment variable OPENAI_API_KEY")

def load_config():
    parser = configargparse.ArgParser(default_config_files=['assistant_config.ini'])
    parser.add('-c', '--config', is_config_file=True, help='config file path')
    parser.add('--model_name', default=None, help='OpenAI Model Name')
    parser.add('--assistant_name', default=None, help='Name of the assistant')
    parser.add('--description', default=None, help='description of the assistant')
    return parser.parse_args()

@app.get("/")
async def index(request: Request):
    with open("templates/index.html") as file:
        content = file.read()
    template = Template(content)
    rendered_content = template.render(assistant_name=config.assistant_name)
    return Response(content=rendered_content, media_type='text/html')


@app.post("/send_prompt", response_class=PlainTextResponse)
async def send_prompt(request: Request):
    assistant_name = config.assistant_name
    description = config.description
    introduction = "The following is a conversation between a user and a virtual mental assistant called "+assistant_name+". "
    start_sequence = "\n"+assistant_name+":"
    restart_sequence = "\nUser: "
    conversation_history = introduction + description + restart_sequence + "Hello, who are you?->" + start_sequence + " I am a virtual mental assistant chatbot.  How can I help you today?\n\nUser: "
    prompt = (await request.json())['prompt'] + "->"
    conversation_history += prompt + start_sequence
    response = openai.Completion.create(
        model=config.model_name,        
        prompt=conversation_history,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        presence_penalty=0,
        frequency_penalty=0.6,
        n=1,
        stop=["User:", assistant_name+":"]
    )
    message = response["choices"][0]["text"]
    conversation_history += message + restart_sequence
    print ("message is: " + message)
    print ("conversation history is: " + conversation_history)
    return message

if __name__ == '__main__':
    config=load_config()
    uvicorn.run(app, host='0.0.0.0', port=8000)