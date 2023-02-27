from fastapi import APIRouter, status, HTTPException

router = APIRouter(prefix="/ping", tags=["Ping"])


@router.get("/", status_code=status.HTTP_200_OK)
@router.get("/{wrong_ping}", status_code=status.HTTP_200_OK)
def get_ping(wrong_ping: str = '') -> dict:
    if wrong_ping != '':
        raise HTTPException(status_code=404, detail="Ping from your client is bad")
    return {
        "message": "pong",
    }
