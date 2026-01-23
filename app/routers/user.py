from fastapi import Body, FastAPI, Response,status, HTTPException,Depends,APIRouter
from .. import models, schemas, utils,oauth2
from sqlalchemy.orm import Session
from typing import Optional,List
from ..database import get_db


router = APIRouter(
    prefix= "/users",
    tags=["Users"]
)

@router.get("/", response_model=List[schemas.User])
async def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    print(users)
    # cursor.execute(""" SELECT * FROM posts
    # """)
    # posts = cursor.fetchall()
    return users

@router.post("/",status_code=status.HTTP_201_CREATED, response_model=schemas.User)
def create_user(users: schemas.UserBase,db: Session =Depends(get_db), current_user: schemas.TokenData = Depends(oauth2.get_current_user)):

    user = db.query(models.User).filter(models.User.email == users.email).first()
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Mail already exists!")
    hashed_password = utils.hash(users.password)
    users.password = hashed_password
    new_user = models.User(**users.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}", response_model=schemas.User)
def get_user(id: int, db:Session = Depends(get_db),  current_user: schemas.TokenData = Depends(oauth2.get_current_user)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} does not exists!")
    return user

@router.put('/',response_model=schemas.User)
def update_user(id: int, db: Session =Depends(get_db),  current_user: schemas.TokenData = Depends(oauth2.get_current_user)):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} does not exits!")
    