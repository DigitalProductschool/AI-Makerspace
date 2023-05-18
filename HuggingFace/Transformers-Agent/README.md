# HuggingFace Transformers Agent
In short, it provides a natural language API on top of transformers: It has defined a set of curated tools and designed an agent to interpret natural language and to use these tools. It is extensible by design.

For this repo, I have added the following capabilities:-
- Image Generation
- Image Caption Generation
- Text to Speech
- PDF Document Question Answering
- Translation
- Summary of link

## How to Run

### Installations
Run the following command to install all project requirements.
```console
$ pip install -r requirements.txt
```

### Add HuggingFace Token
1. Get the token on your profile page on HuggingFace
2. Open `main.py`
3. Add your token to the following line in the code as an argument to `login`
```console
login("<Insert HuggingFace Token>")
```

### Run the Python file
Run `main.py` using command line
```console
$ python main.py
```

`NOTE:` For 'Image Generation' and 'Translation', I am generating the code which will give the output for these features. This is due to my lack of computational resources. If you don't have this challenge, search for the following statement in `main.py`
```console
return_code=True
```
Remove this argument from the function call and the features will run normally after!
