# todo-client

## Build Setup
```bash

# checkout the codes
- Clone this repository
- checkout 'main' branch
- Go inside todo-client folder

# install dependencies
$ yarn install

# change the .env API_URL
local: http://127.0.0.1:8000/ (depends on your local api server)
prod: https://todo-fastapi-3j36.onrender.com ( depends on your production API URL)

# serve with hot reload at localhost:3000
$ yarn dev

# build for production and launch server
$ yarn build
$ yarn start

# generate static project
$ yarn generate
```

## Deployment Setup
Step 1: 
- Create a Web Service on [Render](https://dashboard.render.com/).
- Login and Go to the Render Dashboard.
- Click New > Web Service.
- Select your GitHub repository. Choose repository you want to deploy

- Configure the service:

**  Build Command:**
    yarn && yarn build
 ** Start Command:**
    yarn start

Step 2: 

Configure Environment Variables
 - In Render, navigate to the Environment tab of your service.
   
BASE_URL: https://todo-fastapi-3j36.onrender.com

HOST: 0.0.0.0

Step 3: 

Deploy and Test
Render will build and deploy your application automatically. Once completed, Render provides a live URL for your web service.

Todo App Site can be accessed [here](https://todo-client-m42u.onrender.com)

Endpoints is available here [here](https://todo-fastapi-3j36.onrender.com/docs)

![image](https://github.com/user-attachments/assets/62862540-68d6-4f21-bd82-e6f4f1f9ebbe)



