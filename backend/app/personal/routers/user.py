from fastapi import APIRouter
from personal import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from personal.repository import user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.post('/', response_model=schemas.User)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)




@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)
