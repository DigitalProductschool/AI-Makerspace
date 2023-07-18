# AI-Coloring-App
The solution uses DeOldify to fill color in black and white images using GANS.

### Deployed Application
<a href="http://35.208.52.140:8501/">Colorizer App</a>

### Project Pre-reqs:
- Anaconda/Miniconda

### Structure:
```
- models
  - ColorizeArtistic_gen.pth
- requirements.txt
- streamlit_app.py
```
### Steps to run it locally:

1. Create a `models` directory and download the model into it.
```bash
mkdir 'models'
```
2. Download the model.
```bash
wget https://data.deepai.org/deoldify/ColorizeArtistic_gen.pth -O ./models/ColorizeArtistic_gen.pth
```
3. Install the required dependencies.
```bash
pip install -r requirements.txt
```
4. Run streamlit App
```bash
streamlit run streamlit_app.py
```
### References:
- <a href="https://github.com/jantic/DeOldify">Deoldify</a>
