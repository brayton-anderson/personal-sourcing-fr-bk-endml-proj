from fastapi import FastAPI
from application import  models
from application.database import engine
from application.routers import application, user, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(application.router)
app.include_router(user.router)
