from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": "root"}

@app.get("/hello")
def hello(name: str = "Home"):
    return {
        "message": f"Hello, {name}!",
    }
