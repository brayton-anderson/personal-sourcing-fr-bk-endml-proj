from fastapi import FastAPI
from application import  models
from application.database import engine
from fastapi.middleware.cors import CORSMiddleware
from application.routers import application, user, authentication

app = FastAPI()

# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
#     "http://localhost:3000/",
#     "http://localhost:8000/",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(application.router)
app.include_router(user.router) 
