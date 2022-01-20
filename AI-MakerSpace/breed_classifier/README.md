<<<<<<< HEAD
# DPS-AIMS-Workshop#1: streamlit-heroku:

Hi, Amigos! Here we are going to learn how to easily create a machine learning web app, test it locally and then deploy it on cloud using free tools.

### Tools 2B Used:

These are the tools that we are going to use today:

- Streamlit
- Heroku
- Github
- Optional: Docker & Dockerhub

### Steps:

These are the steps that we will follow in order to have a hands-on experience of what's happening:

1. Create a directory to `aiWorkshop1`using:
```bash
mkdir DPS-AIMS-Workshop-1 
```
2. Clone the repository locally using:
```bash
git clone https://github.com/afiDPS/AI-MakerSpace.git
```
3. Change the directory to `workshop-1-streamlit-heroku` in the cloned repository folder using:
```bash
cd AI-MakerSpace/workshop-1-streamlit-heroku/
```
4. Install all the dependencies using:
```bash
pip3 install -r requirements.txt
```
5. Run the `streamlit_app.py` file using:
```bash
streamlit run streamlit_app.py
```
6. Upload sample images of dogs and test the application using:
- [Norfolk terrier Dog](http://vision.stanford.edu/aditya86/ImageNetDogs/images/n02094114-Norfolk_terrier/n02094114_1637.jpg)

- [Samoyed Dog](http://vision.stanford.edu/aditya86/ImageNetDogs/images/n02111889-Samoyed/n02111889_11729.jpg)

### Streamlit Cloud:
[Streamlit Cloud](https://streamlit.io/cloud)

### Heroku:
[Heroku](https://id.heroku.com/login)

### Optional: Docker

7. Build the project's docker image using:
```bash
docker build -t "alihussainia/aims-dogimgclassifier:v1" .
```
8. Check your docker image successful build using:
```bash
docker images
```
9. Tryout your streamlit app in your browser using:
```bash
docker run -d -p80:8501 alihussainia/aims-dogimgclassifier:v1
```
10. let's push our docker image to dockerhub aka the most popular container registry but first login to your dockerhub a/c using:
```bash
docker login
```
11. Now push the docker image to dockerhub using: 
```bash
docker push alihussainia/aims-dogimgclassifier:v1
```
12. Finally, we are done with docker so stop the container using:
```bash
docker stop <container-id>
```
### Dataset 2B Used:
- stanford_dogs from tensorflow datasets. [link](https://www.tensorflow.org/datasets/catalog/stanford_dogs)
=======
# AIMakerspace
>>>>>>> fe1de7a277148841a9d22a5fb89f51598878cd99
