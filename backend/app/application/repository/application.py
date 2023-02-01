from sqlalchemy.orm import Session
from application import models, schemas
from fastapi import HTTPException, status


def get_all(db: Session):
    applications = db.query(models.Profile).all()
    return applications


def create(request: schemas.Profile, db: Session):
    new_application = models.Profile(title=request.title, body=request.body, user_id=1)
    db.add(new_application)
    db.commit()
    db.refresh(new_application)
    return new_application


def destroy(id: int, db: Session):
    application = db.query(models.Profile).filter(models.Profile.id == id)

    if not application.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Profile with id {id} not found")

    application.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(id: int, request: schemas.Profile, db: Session):
    application = db.query(models.Profile).filter(models.Profile.id == id)

    if not application.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Profile with id {id} not found")

    application.update(request)
    db.commit()
    return 'updated'


def show(id: int, db: Session):
    application = db.query(models.Profile).filter(models.Profile.id == id).first()
    if not application:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Profile with the id {id} is not available")
    return application
