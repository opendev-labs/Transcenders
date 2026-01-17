from fastapi import APIRouter
from ..config import CONF

router = APIRouter()

@router.get("/health")
def health():
    return {
        "status": "ok",
        "app": CONF["cfg"]["app"]["name"],
        "env": CONF["env"],
        "version": CONF["cfg"]["app"]["version"]
    }
