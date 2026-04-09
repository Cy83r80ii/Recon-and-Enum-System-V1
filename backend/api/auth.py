from fastapi import APIRouter
from jose import jwt
from datetime import datetime, timedelta

router = APIRouter()

SECRET = "ARESX_SECRET"

@router.post("/login")
def login(data: dict):

    username = data.get("username")

    token = jwt.encode(
        {"sub": username, "exp": datetime.utcnow()+timedelta(hours=5)},
        SECRET,
        algorithm="HS256"
    )

    return {"token": token}
