##  3/ Flask Server + Heroku + UI & JS  + Input & Firebase | skkh003
---

<p class="ex1" align="justify" style="padding: 15px 15px 15px 15px">            
 This repository is a continuation of 2/ and we deployed basic Flask server to Heroku with basic HTML, CSS, JavaScript and Bootstrap. This repository will focus on how to take user input, forms and database - mongodb. I added a new endpoint '/input' to highlight several forms and input section.
</p>

##### Expectation: 
- Your responsive web application in Flask Server deployed to Heroku will have proper UI as well as forms to take user input.
- This prototype focuses of database - firebase.

<img src="./app/static/img/about/flask.png" height=200px> <img src="./app/static/img/about/heroku.png" height=200px> 
<img src="./app/static/img/about/firebase.png" height=180px>

Step 1: clone the repository with `$git clone`

Step 2: Inside the repository, set virtual environment:
```powershell
> pip3 install virtualenv
> virtualenv env
> source env/bin/activate (ubuntu)
> env\Scripts\activate (windows)
```
WIN: If running scripts is disabled in your windows system by default , then in PowerShell (admn):
```powershell
> Set-ExecutionPolicy RemoteSigned
```
to get back to original configuration `Set-ExecutionPolicy Restricted`.

Step 3: Install requirements:
```python
> pip3 install -r requirements.txt or
> pip3 install -r .\requirements.txt
```
 
 * NOTE :  gcc is required to build pyrebase

Step 4: To run the server:
```python
> python app.py
```


• `NOTE:` In case of installation of new python library, don't forget to `$ pip freeze > requirements.txt`

 ### File Structure:
 ```
|-----|
       |--- Procfile
       |--- README.MD
       |--- app.py
       |--- requirements.txt
       |--- env (virtual environment)
       |--- app ---|
                   |--- __init__.py
                   |--- admin_views.py
                   |--- view.py
                   |--- templates ---|
                   |                 |--- admin 
                   |                 |--- macros
                   |                 |--- public (all html files)
                   |               
                   |--- static ---|               
                                  | --- css
                                  | --- image
                                  | --- js
                                  | --- favicon.ico
                                  
 ``` 

 To push to Heroku as a heroku webapp: ( pwd == . )
 ```python
 $ git init . #skip if already a github repository
 $ git add app.py Procfile requirements.txt app (or $git add *)
 $ git commit -m "v3 project --skk" 
 $ heroku login -i
 $ heroku create projectname
 $ heroku git:remote -a projectname
 $ git push heroku master
 ```

### localhost:
<img src="./localhost1.png" width=100%> </br></br>
<img src="./localhost2.png" width=100%>

author: @[s-ai-kia](https://github.com/s-ai-kia)