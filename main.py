from fastapi import FastAPI
from database import  base , engine 

from routes import Blogs,Users,Login

base.metadata.create_all(bind=engine)



app=FastAPI()

app.include_router(Blogs.router)
app.include_router(Users.router)
app.include_router(Login.router)






