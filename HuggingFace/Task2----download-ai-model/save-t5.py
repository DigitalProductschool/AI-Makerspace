from transformers import AutoTokenizer, AutoModelWithLMHead

tokenizer = AutoTokenizer.from_pretrained("t5-small")

model = AutoModelWithLMHead.from_pretrained("t5-small")

#saving the model
model.save_pretrained('t5-small-saved')
tokenizer.save_pretrained('t5-small-saved')