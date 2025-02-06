# todo-client

## Build Setup
```bash

# checkout the codes
- Clone this repository
- checkout 'main' branch
- Go inside todo-fastapi folder

# create virtual environment
$python3 -m venv venv

# activate virtual environment
#source venv/bin/activate

# install dependencies
$ pip install -r requirements.txt

# change the .env Database environment variables
local db :
 - DATABASE_HOST=localhost
 - DATABASE_NAME=TodoApplicationDatabase
 - DATABASE_USER=postgres
 - DATABASE_PASSWORD=test1234!
 - DATABASE_PORT=5432
prod db :
DATABASE_URL=postgresql://todo_db_8qmn_user:XlIjz9A2C4XnkmR2uDQ0vlOY8huWN2Ze@dpg-cuhka5tds78s73eva9rg-a.singapore-postgres.render.com/todo_db_8qmn

# start with hot reload at localhost
$ uvicorn main:app --reload

# you can now access the site

e.g.  http://localhost:3000/ 
```

## Deployment Setup
Step 1: 
- Create a Web Service on [Render](https://dashboard.render.com/).
- Login and Go to the Render Dashboard.
- Click New > Web Service.
- Select your GitHub repository. Choose repository you want to deploy

- Configure the service:

**  Build Command:**

    pip install -r requirements.txt
    
 ** Start Command:**
 
    uvicorn main:app --host 0.0.0.0 --port 10000

Step 2: 

Deploy and Test

- Click Create Web Service.
- Render will build and deploy your app automatically.
- Visit the provided URL to see your FastAPI app live.

Todo App Site can be accessed [here](https://todo-client-m42u.onrender.com)

Endpoints is available here [here](https://todo-fastapi-3j36.onrender.com/docs)

![image](https://github.com/user-attachments/assets/62862540-68d6-4f21-bd82-e6f4f1f9ebbe)



