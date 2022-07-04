from transformers import AutoTokenizer, AutoModelWithLMHead

tokenizer = AutoTokenizer.from_pretrained("t5-small")

model = AutoModelWithLMHead.from_pretrained("t5-small")

model.save_pretrained('t5-small-saved')
tokenizer.save_pretrained('t5-small-saved')