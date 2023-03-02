# Introduction to PyCaret
This AI-Makerspace workshop introduces PyCaret, an open-source low-code machine learning library in Python that automates machine learning workflows. The directory contains all the necessary files that you are going to need to practice this workshop on your own. You can start from opening `LoanClassification.ipynb` where you will find a button <a href='https://colab.research.google.com/github/alihussainia/AI-Makerspace/blob/master/PyCaret-Classification/LoanClassification.ipynb'>`Open in Colab`</a> to open the notebook in Google Colab, the IDE used in the workshop.

### Dataset
The `Bank Loan Classification` dataset used during the workshop is taken from Kaggle and can be found <a href='https://www.kaggle.com/sriharipramod/bank-loan-classification'>`here`</a>.

### Components:
In the workshop we discussed <a href='https://pycaret.gitbook.io/docs/'>`classification module`</a> of PyCaret particularly these methods:

1. <a href='https://pycaret.gitbook.io/docs/get-started/functions/initialize#setting-up-environment'>`setup`</a> - This function initializes the environment in pycaret and creates the transformation pipeline to prepare the data for modeling and deployment.
2. <a href='https://pycaret.gitbook.io/docs/get-started/functions/train#compare_models'>`compare_models`</a> - This function uses all models in the model library and scores them.
3. <a href='https://pycaret.gitbook.io/docs/get-started/functions/train#create_model'>`create_model`</a> - This function creates a model and scores it.  
4. <a href='https://pycaret.gitbook.io/docs/get-started/functions/optimize#tune_model'>`tune_model`</a> - This function tunes the hyperparameters of a model and the best model is selected based on the metric defined in optimize parameter.
5. <a href='https://pycaret.gitbook.io/docs/get-started/functions/analyze#plot_model'>`plot_model`</a> - This function takes a trained model object and returns a plot based on the test / hold-out set.
6. <a href='https://pycaret.gitbook.io/docs/get-started/functions/analyze#evaluate_model'>`evaluate_model`</a> - This function displays a user interface for all of the available plots for a given estimator. It internally uses the plot_model() function.
7. <a href='https://pycaret.gitbook.io/docs/get-started/functions/deploy#predict_model'>`predict_model`</a> - This function is used to predict new data using a trained estimator.
8. <a href='https://pycaret.gitbook.io/docs/get-started/functions/deploy#finalize_model'>`finalize_model`</a> - This function fits the estimator onto the complete dataset passed during the setup() stage.
9. <a href='https://pycaret.gitbook.io/docs/get-started/functions/deploy#save_model'>`save_model`</a> - This function saves the transformation pipeline and trained model object into the current active directory as a pickle file for later use.
10. <a href='https://pycaret.gitbook.io/docs/get-started/functions/deploy#load_model'>`load_model`</a> - This function loads a previously saved transformation pipeline and model from the current active directory into the current python environment. Load object must be a pickle file.
11. <a href='https://pycaret.gitbook.io/docs/get-started/functions/deploy#convert_model'>`convert_model`</a> - Convert Model into different Language. 
12. <a href='https://pycaret.gitbook.io/docs/get-started/functions/deploy#create_api'>`create_api`</a> - This function will create a fastAPI instance. 
13. <a href='https://pycaret.gitbook.io/docs/get-started/functions/deploy#create_docker'>`create_docker`</a> - This function will create a DockerFile of the API. 
14. <a href='https://pycaret.gitbook.io/docs/get-started/functions/analyze#check_fairness'>`check_fairness`</a> - This will allow to check model fairness with respect to a feature(s).
15. <a href='https://www.mlflow.org/docs/latest/index.html'>`mlflow ui`</a> - This will allow to track experiments.
16. <a href='https://docs.streamlit.io/'>`streamlit`</a> - This will allow easy web app creation.

`Note` - All the headings mentioned above are hyperlinks to their respective official documentation.

### Model API:
Here we are using `FastAPI` framework to create a custom API for our loan classification model. Two files are added to the dir that belongs to API logic devlopment and call; `main.py` and `call.py`.

The `main.py` follows the following structure:

1. Import dependencies.
2. Create FastAPI Instance.
3. Define Root Function.
4. Create Model Class using Pydantic's BaseModel.
5. Load AI Models.
6. Create `/loans` path operation or route.
7. Show Auto documentation options in FastAPI.
8. Test `/loans` using Thunder Client on GitPod.
9. Create `/loans/{version}` path parameter.
10. Test `/loans/{version}` using Thunder Client on GitPod. 
11. Explain importance of operation order with `/loans/greetings` path parameter.
