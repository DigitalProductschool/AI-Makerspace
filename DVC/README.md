#
# Data Version Control
<p><strong>Data Version Control</strong> is a <a href="https://github.com/iterative/dvc/blob/master/LICENSE">free</a>, open-source tool for <strong>data management,
ML pipeline automation, and experiment management</strong>. This helps
data science and machine learning teams manage <strong>large datasets</strong>, make projects
<strong>reproducible</strong>, and <strong>collaborate</strong> better.</p>

#
## Pre-Reqs

- Git
- Python
- DVC (Download <a href='https://dvc.org/'>`here`</a>)

#
## Project Structure
```bash
DVC
├── .dvc 
    ├── cache 
    ├── tmp 
    ├── .gitignore 
    ├── config
├── data 
    ├── .gitignore 
    ├── data.xml 
    ├── data.xml.dvc 
    ├── prepared 
        ├── test.tsv 
        ├── train.tsv 
    ├── features 
        ├── test.pkl 
        ├── train.pkl 
├── src 
    ├── prepare.py 
    ├── featurization.py
    ├── train.py 
    ├── evaluate.py
    ├── requirements.txt
├── .dvcignore
├── .gitignore
├── dvc.lock
├── dvc.yaml
├── model.pkl
├── params.yaml
├── eval
    ├── live
        ├── plots
        ├── metrics.json
    ├── prc
    ├── .gitignore
    ├── importance.png

```
#
## Commands:

- Initialize a git repository.
```bash
git init
```
- Initialize a dvc repository.
```bash
dvc init
```
- Create a new directory for data
```bash
mkdir data
```
- Fetch data from a remote dvc directory. (Or put your own dataset in this folder)
```bash
dvc get https://github.com/iterative/dataset-registry get-started/data.xml -o data/data.xml
```
- Stage data to start tracking it with DVC
```bash
cd data
```
```bash
dvc add data.xml
```
```bash
cd ..
```
- Commit the meta file to git. 
```bash
git add .
```
```bash
git commit -m "Add raw data"
```
- Add a remote storage location to store the data/models.
- Eg: dvc remote add -d storage gdrive://1YrgIhmczfkQTsdZGvxE9DJbA9KoRDwsN
```bash
dvc remote add -d 'name' 'path'
```
- Git commit the dvc config file.
```bash
git commit .dvc/config -m "Configure remote storage"
```
- Push data to remote storage
```bash
dvc push
```
- Removing, fetching and versioning the data
```bash
rm data/data.xml
```
```bash
dvc pull
```
```bash
cp data/data.xml /tmp/data.xml
```
```bash
cat /tmp/data.xml >> data/data.xml
```
```bash
cd data
```
```bash
dvc add data.xml
```
```bash
cd ..
```
```bash
git add data/data.xml.dvc
```
```bash
git commit -m "Dataset updated"
```
```bash
dvc push
```
```bash
git log --oneline
```
```bash
git checkout HEAD^1 data/data.xml.dvc
```
```bash
dvc checkout
```
```bash
git commit data/data.xml.dvc -m "Revert dataset changes"
```
- Creating a github repository
```bash
git remote add origin https://github.com/'username'/'repository_name'.git
```
```bash
git branch -M main
```
```bash
git push -u origin main
```
- Downloading code files
```bash
wget https://code.dvc.org/get-started/code.zip -o code.zip
```
```bash
tar -xf code.zip
```
```bash
rm code.zip
```
```bash
rm .github
```
- Create a python virtual environment
```bash
python -m venv env
```
```bash
env\Scripts\activate
```
- Installing the requirements
```bash
pip install -r src/requirements.txt
```
- Creating dvc.yaml file (adding stages of pipeline)
```bash
dvc stage add -n prepare -p prepare.seed,prepare.split -d src/prepare.py -d data/data.xml -o data/prepared python src/prepare.py data/data.xml
```
```bash
dvc stage add -n featurize -p featurize.max_features,featurize.ngrams -d src/featurization.py -d data/prepared -o data/features python src/featurization.py data/prepared data/features
```
```bash
dvc stage add -n train -p train.seed,train.n_est,train.min_split -d src/train.py -d data/features -o model.pkl python src/train.py data/features model.pkl
```
- Reproducing/Running the pipeline
```bash
dvc repro
```
```bash
git add .
```
```bash
git commit -m "Machine Learning Pipeline"
```
```bash
git push origin main
```
- Visualizing the pipeline
```bash
dvc dag
```
- Adding the model evaluation stage in the pipeline
```bash
dvc stage add -n evaluate -d src/evaluate.py -d model.pkl -d data/features -M eval/live/metrics.json -O eval/live/plots -O eval/prc -o eval/importance.png python src/evaluate.py model.pkl data/features
```
- Running the pipeline and saving the results of the model.
```bash
dvc repro
```
```bash
git add .
```
```bash
git commit -m “Model Results v1”
```
```bash
git push origin main
```
- Changing the hyperparameters (eg: set max_features = 400) and re-running the pipeline.
```bash
dvc repro
```
- Check difference in parameters
```bash
dvc params diff
```
- Check difference in metrics
```bash
dvc metrics diff
```
- Visualize the pipeline
```bash
dvc dag
```
- Git commit
```bash
git add .
```
```bash
git commit -m “Model Results v2”
```
```bash
git push origin main
```
- DVC commit to store models/prepared data to remote storage
```bash
dvc push
```

