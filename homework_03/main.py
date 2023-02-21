from fastapi import FastAPI
from views.pingpong.views import router as ping_router

app = FastAPI()
app.include_router(ping_router)
