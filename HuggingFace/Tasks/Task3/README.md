In this task we will see how can we dockerize our application.

Since, the model is relatively large(245mb approx.). We cannot push it to GitHub repository because github allows only files upto 100mb to be pushed via git cli.

- **git lfs** could be an alternate solution to push your model to the repository, but in this tutorial we won't be getting our hands dirty with **git lfs**

So, we would using our save-t5.py script from the previous task to download the t5-model within the docker image while building it.

- Create the Dockerfile
    - I am using **python3.9** image 
    - Define the working directory: **WORKDIR** sets the working directory for all the subsequent Dockerfile instructions.

    - Install all the dependencies from requirements.txt.
    For running any command in the image we use **RUN** instruction. The **RUN** instruction will execute any command in a new layer on top of the current image and commit the results. The resulting committed image will be used for the next step in the Dockerfile.

    - Copy all the files from a local source location to a destination in the Docker container by using **COPY** instruction.

    - Finally the most important step:
    ```bash
    RUN python save-t5.py
    ```
    While buidling the image the above instruction will execute our save-t5.py script which will download and save the model files within the Docker image.

    - Start the application

<br/>

- Build the docker image and test it out locally

```bash
docker build -t inference .
```

```bash
docker run -d -p 80:80 inference:latest
```
