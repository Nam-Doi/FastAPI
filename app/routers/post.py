from fastapi import Body, FastAPI, Response,status, HTTPException,Depends,APIRouter
from .. import models, schemas, utils
from sqlalchemy.orm import Session
from typing import Optional,List
from ..database import get_db

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


@router.get("/", response_model=List[schemas.Post])
async def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all() 
    # cursor.execute(""" SELECT * FROM posts
    # """)
    # posts = cursor.fetchall()
    return posts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
async def post_create(post : schemas.PostCreate, db: Session = Depends(get_db)):
    # cursor.execute("""INSERT INTO posts(title, content, published) VALUES(%s, %s, %s) RETURNING *""",(post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    # new_post = models.Post(title = post.title, content = post.content, published = post.published) cach 1
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post) # lay lai thong tin vua them vi du id.. vi ta khong the dung returning
    return new_post

@router.get("/{id}", response_model=schemas.Post)
async def getby_id(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    # cursor.execute("""SELECT * FROM posts WHERE id = %s""", (id,))
    # post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found")
    return post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_by_id(id: int, db: Session = Depends(get_db)):
    # cursor.execute(""" DELETE FROM posts WHERE id = %s RETURNING *""",(id,))
    # deleted_post = cursor.fetchone()
    deleted_post = db.query(models.Post).filter(models.Post.id == id)
    if deleted_post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id {id} was not found")
    deleted_post.delete(synchronize_session=False)
    db.commit()
    return

@router.put("/{id}", response_model=schemas.Post)
def update_by_id(id: int, post:schemas.PostCreate, db: Session = Depends(get_db)):
    # cursor.execute(""" UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",(post.title, post.content, post.published,id))
    # update = cursor.fetchone()
    # conn.commit()
    update_post = db.query(models.Post).filter(models.Post.id == id)
    if update_post.first() == None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id {id} was not found")
    update_post.update(post.model_dump(), synchronize_session=False)
    db.commit()
    return update_post.first()