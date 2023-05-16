# from transformers import OpenAiAgent
# agent = OpenAiAgent(model="text-davinci-003", api_key="<your_api_key>")

from huggingface_hub import login
from transformers import HfAgent


login("<Insert HuggingFace Token>")

# Starcoder
agent = HfAgent("https://api-inference.huggingface.co/models/bigcode/starcoder")
# StarcoderBase
# agent = HfAgent("https://api-inference.huggingface.co/models/bigcode/starcoderbase")
# OpenAssistant
# agent = HfAgent(url_endpoint="https://api-inference.huggingface.co/models/OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5")

# agent.run("Draw me a picture of rivers and lakes.", remote = True)


# agent.run("Draw me a picture of the sea then transform the picture to add an island", remote = True)

# Generate code from prompt. Works with Starcoder and StarcoderBase agent.
code = agent.run("Draw me a picture of rivers and lakes", return_code=True)
print('Code:-')
print(code)

agent.run("Caption the following image", image='beaver.png')

