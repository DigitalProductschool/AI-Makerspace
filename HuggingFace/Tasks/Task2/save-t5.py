
from transformers import AutoTokenizer, AutoModelWithLMHead

#download the model
tokenizer = AutoTokenizer.from_pretrained("t5-small")

model = AutoModelWithLMHead.from_pretrained("t5-small")

#saving the model and tokenizer in "t5-small-saved" dir locally
model.save_pretrained('t5-small-saved')
tokenizer.save_pretrained('t5-small-saved')