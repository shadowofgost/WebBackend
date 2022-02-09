"""
# @Time             : 2022-01-22 10:03:25
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Api/run.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-01-28 18:46:38
# @LastAuthor       : Albert Wang
"""
from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import delete
from src.Api import models, schema, crud
from sqlalchemy.orm import Session
from src.Api.database import SessionLocal, engine
import uvicorn
from datetime import timedelta
import time
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["http://127.0.0.1:8080" "http://127.0.0.1"]


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schema.User)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, id=user.id)
    if db_user:
        raise HTTPException(status_code=400, detail="id already registered")
    return crud.create_user(db=db, user=user)


@app.post("/jwt/token", response_model=schema.Token)
def login_for_access_token(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
):
    user = crud.jwt_authenticate_user(
        db=db, id=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=crud.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = crud.created_access_token(
        data={"sub": user.id}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me/", response_model=schema.User)
async def read_users_me(current_user: schema.User = Depends(crud.jwt_get_current_user)):
    return current_user


if __name__ == "__main__":
    uvicorn.run(
        "run:app", host="0.0.0.0", port=8000, reload=True, debug=True, workers=1
    )
@app.delete("/ModelUser/{user_id}/")
async def ModelUserDelete(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends(),idmanager)：
    model="ModelUser"
    return delete(db,schema,model,idna)
