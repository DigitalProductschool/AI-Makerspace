# Introduction to PyCaret
This AI-Makerspace workshop introduces PyCaret, an open-source low-code machine learning library in Python that automates machine learning workflows. The directory contains all the necessary files that you are going to need to practice this workshop on your own. You can start from opening `LoanClassification.ipynb` where you will find a button `Open in Colab` to open the notebook in Google Colab, the IDE used in the workshop.

### Dataset
The `Bank Loan Classification` dataset used during the workshop is taken from Kaggle and can be found [here]('https://www.kaggle.com/sriharipramod/bank-loan-classification').

### Components:
In the workshop we discussed [`classification module`]('https://pycaret.gitbook.io/docs/') of PyCaret particularly these methods:

1. [`setup`]('https://pycaret.gitbook.io/docs/get-started/functions/initialize#setting-up-environment') - This function initializes the environment in pycaret and creates the transformation pipeline to prepare the data for modeling and deployment.
2. [`compare_models`]('https://pycaret.gitbook.io/docs/get-started/functions/train#compare_models') - This function uses all models in the model library and scores them.
3. [`create_model`]('https://pycaret.gitbook.io/docs/get-started/functions/train#create_model') - This function creates a model and scores it.  
4. [`tune_model`]('https://pycaret.gitbook.io/docs/get-started/functions/optimize#tune_model') - This function tunes the hyperparameters of a model and the best model is selected based on the metric defined in optimize parameter.
5. [`plot_model`]('https://pycaret.gitbook.io/docs/get-started/functions/analyze#plot_model') - This function takes a trained model object and returns a plot based on the test / hold-out set.
6. [`evaluate_model`]('https://pycaret.gitbook.io/docs/get-started/functions/analyze#evaluate_model') - This function displays a user interface for all of the available plots for a given estimator. It internally uses the plot_model() function.
7. [`predict_model`]('https://pycaret.gitbook.io/docs/get-started/functions/deploy#predict_model') - This function is used to predict new data using a trained estimator.
8. [`finalize_model`]('https://pycaret.gitbook.io/docs/get-started/functions/deploy#finalize_model') - This function fits the estimator onto the complete dataset passed during the setup() stage.
9. [`save_model`]('https://pycaret.gitbook.io/docs/get-started/functions/deploy#save_model') - This function saves the transformation pipeline and trained model object into the current active directory as a pickle file for later use.
10. [`load_model`]('https://pycaret.gitbook.io/docs/get-started/functions/deploy#load_model') - This function loads a previously saved transformation pipeline and model from the current active directory into the current python environment. Load object must be a pickle file.
11. [`convert_model`]('https://pycaret.gitbook.io/docs/get-started/functions/deploy#convert_model') - Convert Model into different Language. 
12. [`create_api`]('https://pycaret.gitbook.io/docs/get-started/functions/deploy#create_api') - This function will create a fastAPI instance. 
13. [`create_docker`]('https://pycaret.gitbook.io/docs/get-started/functions/deploy#create_docker') - This function will create a DockerFile of the API. 
14. [`check_fairness`]('https://pycaret.gitbook.io/docs/get-started/functions/analyze#check_fairness') - This will allow to check model fairness with respect to a feature(s).
15. [`mlflow ui`]('https://www.mlflow.org/docs/latest/index.html') - This will allow to track experiments.
16. [`streamlit`]('https://docs.streamlit.io/') - This will allow easy web app creation.

`Note` - All the headings mentioned above are hyperlinks to their respective official documentation.
