# Machine_Learning_Project
This is my First Machine Learning Project

## Requirements:
1. [GitHub Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku/com/login)
3. [vscode IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)


Creating Conda Environment
```
conda create -p <env name> python=3.9 -y 
```
To activate conda env
```
conda actiavte <env name>/
```
To install all imports from requirements.txt file
```
pip install -r requirements.txt
```
## Git Commands
```
git status --> this command tells us all the changes that are not staged from local
```
```
git add. --> this commands adds files to git
```
```
git log  --> this command gives us list of previous commits
```
```
git commit -m "<message>"  -->  commits all the changes to git
```
```
git push origin main --> to send all the changes to main branch
```
to check remote url
```
git remote -v
```

## Deployments:

To setup CI/CD pipeline in Heroku we need below information

1. HEROKU_EMAIL
2. HEROKU_API_KEY 
3. HEROKU_APP_NAME hemanthmlproject 

### Build Docker image:
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase

To list Docker images
```
docker images
```
To run docker image
```
docker run -p 5000:5000 -e PORT=5000 <image id>
```
To check running containers in docker
```
docker ps
```
To stop docker container
```
docker stop <conatiner_id>
```
## To run Python setup file
```
python setup.py install
```
Install ipykernerl
```
pip install ipykernel
```
