"""
# @Time             : 2022-01-22 10:03:25
# @Author           : Albert Wang
# @Email            : shadowofgost@outlook.com
# @Software         : Vscode
# @FilePath         : /WebBackend/src/Api/run.py
# @Copyright Notice : Copyright (c) ${now_year} Albert Wang 王子睿, All Rights Reserved.
# @Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Description      :
# @LastTime         : 2022-02-08 15:37:47
# @LastAuthor       : Albert Wang
"""
from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import uvicorn
from datetime import timedelta
import time
from fastapi.middleware.cors import CORSMiddleware
from ..Services import (
    public,
    ModelEquipmentCrud,
    ModelDepartmentCrud,
    ModelLocationCrud,
    ModelLocationExtensionCrud,
    ModelMmxDataCrud,
    ModelTyperaCrud,
    ModelUserCrud,
    ModelUserExtensionCrud,
)

from ..Models import *

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


@app.get("users/delete/")
def delete(model: str, user: schema.User = Depends(crud.jwt_get_current_user)):
    if not user:
        raise HTTPException(status_code=400, detail="Token Error")
    return public.delete(model=model)


@app.get("users/department/update/")
def department_update(user: schema.User = Depends(crud.jwt_get_current_user)):
    if not user:
        raise HTTPException(status_code=400, detail="Token Error")
    else:
        model = "t_cydept"
        id = user.id
        return ModelDepartmentCrud.update(model=model, id=id)


@app.get("users/department/insert/")
def department_insert(user: schema.User = Depends(crud.jwt_get_current_user)):
    if not user:
        raise HTTPException(status_code=400, detail="Token Error")
    else:
        model = "t_cydept"
        id = user.id
        return ModelDepartmentCrud.insert(model=model, id=id)


@app.get(
    "users/department/select/", response_model=ModelDepartmentSelectOutSingleTableSchema
)
def department_select(
    type: int, user: schema.User = Depends(crud.jwt_get_current_user)
):
    if not user:
        raise HTTPException(status_code=400, detail="Token Error")
    else:
        model = "t_cydept"
        return ModelDepartmentCrud.service_select(
            model=model, service_type=type, schema=user
        )


@app.get("users/equipment/update/")
def equipment_update(user: schema.User = Depends(crud.jwt_get_current_user)):
    if not user:
        raise HTTPException(status_code=400, detail="Token Error")
    else:
        model = "t_cyequipment"
        id = user.id
        return ModelEquipmentCrud.update(model=model, id=id)


@app.get("users/equipment/insert/")
def equipment_insert(user: schema.User = Depends(crud.jwt_get_current_user)):
    if not user:
        raise HTTPException(status_code=400, detail="Token Error")
    else:
        model = "t_cyequipment"
        id = user.id
        return ModelEquipmentCrud.insert(model=model, id=id)


@app.get(
    "users/equipment/select/", response_model=ModelEquipmentSelectOutSingleTableSchema
)
def equipment_select(type: int, user: schema.User = Depends(crud.jwt_get_current_user)):
    if not user:
        raise HTTPException(status_code=400, detail="Token Error")
    else:
        model = "t_cyequipment"
        return ModelEquipmentCrud.service_select(
            model=model, service_type=type, schema=user
        )


@app.get("users/location/update/")
def location_update(user: schema.User = Depends(crud.jwt_get_current_user)):
    if not user:
        raise HTTPException(status_code=400, detail="Token Error")
    else:
        model = "t_cylocation"
        id = user.id
        return ModelLocationCrud.update(model=model, id=id)


@app.get("users/location/insert/")
def location_insert(user: schema.User = Depends(crud.jwt_get_current_user)):
    if not user:
        raise HTTPException(status_code=400, detail="Token Error")
    else:
        model = "t_cylocation"
        id = user.id
        return ModelLocationCrud.insert(model=model, id=id)


@app.get(
    "users/location/select/", response_model=ModelLocationSelectOutSingleTableSchema
)
def location_select(
    type: int, get_ex: int, user: schema.User = Depends(crud.jwt_get_current_user)
):
    if not user:
        raise HTTPException(status_code=400, detail="Token Error")
    else:
        model = "t_cylocation"
        return ModelLocationCrud.service_select(
            model=model, service_type=type, schema=user
        )


@app.get("users/loactionextension/update/")
def locationextension_update(user: schema.User = Depends(crud.jwt_get_current_user)):
    if not user:
        raise HTTPException(status_code=400, detail="Token Error")
    else:
        model = "t_cylocationex"
        id = user.id
        return ModelLocationExtensionCrud.update(model=model, id=id)


@app.get("users/loactionextension/insert/")
def locationextension_insert(user: schema.User = Depends(crud.jwt_get_current_user)):
    if not user:
        raise HTTPException(status_code=400, detail="Token Error")
    else:
        model = "t_cylocationex"
        id = user.id
        return ModelLocationExtensionCrud.insert(model=model, id=id)


@app.get(
    "users/locationextension/select/",
    response_model=ModelLocationExtensionSelectOutSingleTableSchema,
)
def locationextension_select(
    type: int, user: schema.User = Depends(crud.jwt_get_current_user)
):
    if not user:
        raise HTTPException(status_code=400, detail="Token Error")
    else:
        model = "t_cylocationex"
        return ModelLocationExtensionCrud.service_select(
            model=model, service_type=type, schema=user
        )


@app.get("users/mmxdata/update/")
def mmxdata_update(user: schema.User = Depends(crud.jwt_get_current_user)):
    if not user:
        raise HTTPException(status_code=400, detail="Token Error")
    else:
        model = "t_cymmxdata"
        id = user.id
        return ModelMmxDataCrud.update(model=model, id=id)


@app.get("users/mmxdata/insert/")
def mmxdata_insert(user: schema.User = Depends(crud.jwt_get_current_user)):
    if not user:
        raise HTTPException(status_code=400, detail="Token Error")
    else:
        model = "t_cymmxdata"
        id = user.id
        return ModelMmxDataCrud.insert(model=model, id=id)


@app.get("users/mmxdata/select/", response_model=ModelMmxDataSelectOutSingleTableSchema)
def mmxdata_select(type: int, user: schema.User = Depends(crud.jwt_get_current_user)):
    if not user:
        raise HTTPException(status_code=400, detail="Token Error")
    else:
        model = "t_cymmxdata"
        return ModelMmxDataCrud.service_select(
            model=model, service_type=type, schema=user
        )


@app.get("users/typera/update/")
def typera_update(user: schema.User = Depends(crud.jwt_get_current_user)):
    if not user:
        raise HTTPException(status_code=400, detail="Token Error")
    else:
        model = "t_cytypera"
        id = user.id
        return ModelTyperaCrud.update(model=model, id=id)


@app.get("users/typera/insert/")
def typera_insert(user: schema.User = Depends(crud.jwt_get_current_user)):
    if not user:
        raise HTTPException(status_code=400, detail="Token Error")
    else:
        model = "t_cytypera"
        id = user.id
        return ModelTyperaCrud.insert(model=model, id=id)


@app.get("users/typera/select/", response_model=ModelTyperaSelectOutSingleTableSchema)
def typera_select(type: int, user: schema.User = Depends(crud.jwt_get_current_user)):
    if not user:
        raise HTTPException(status_code=400, detail="Token Error")
    else:
        model = "t_cytypera"
        return ModelTyperaCrud.service_select(
            model=model, service_type=type, schema=user
        )


@app.get("users/user/update/")
def user_update(user: schema.User = Depends(crud.jwt_get_current_user)):
    if not user:
        raise HTTPException(status_code=400, detail="Token Error")
    else:
        model = "t_cyuser"
        id = user.id
        return ModelUserCrud.update(model=model, id=id)


@app.get("users/user/insert/")
def user_insert(user: schema.User = Depends(crud.jwt_get_current_user)):
    if not user:
        raise HTTPException(status_code=400, detail="Token Error")
    else:
        model = "t_cyuser"
        id = user.id
        return ModelUserCrud.insert(model=model, id=id)


@app.get("users/user/select/", response_model=ModelUserSelectOutSingleTableSchema)
def user_select(type: int, user: schema.User = Depends(crud.jwt_get_current_user)):
    if not user:
        raise HTTPException(status_code=400, detail="Token Error")
    else:
        model = "t_cyuser"
        return ModelUserCrud.service_select(model=model, service_type=type, schema=user)


@app.get("users/userextension/update/")
def userextension_update(user: schema.User = Depends(crud.jwt_get_current_user)):
    if not user:
        raise HTTPException(status_code=400, detail="Token Error")
    else:
        model = "t_cyuserex"
        id = user.id
        return ModelUserExtensionCrud.update(model=model, id=id)


@app.get("users/userextension/insert/")
def userextension_insert(user: schema.User = Depends(crud.jwt_get_current_user)):
    if not user:
        raise HTTPException(status_code=400, detail="Token Error")
    else:
        model = "t_cyuserex"
        id = user.id
        return ModelUserExtensionCrud.insert(model=model, id=id)


@app.get(
    "users/userextension/select/",
    response_model=ModelUserExtensionSelectOutSingleTableSchema,
)
def userextension_select(
    type: int, user: schema.User = Depends(crud.jwt_get_current_user)
):
    if not user:
        raise HTTPException(status_code=400, detail="Token Error")
    else:
        model = "t_cyuserex"
        return ModelUserExtensionCrud.service_select(
            model=model, service_type=type, schema=user
        )


if __name__ == "__main__":
    uvicorn.run(
        "run:app", host="0.0.0.0", port=8000, reload=True, debug=True, workers=1
    )
