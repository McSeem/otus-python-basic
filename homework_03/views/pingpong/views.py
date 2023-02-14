from fastapi import APIRouter, status, HTTPException

router = APIRouter(prefix="homework_03/views/pingpong", tags=["Ping"])


@router.get("/", status_code=status.HTTP_200_OK)
def get_ping():
    return {
        "message": "pong",
    }
