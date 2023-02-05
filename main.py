from fastapi import FastAPI

app = FastAPI()

# Runserver : uvicorn main:app --reload

@app.get("/")
def read_root():
    return {"Hello":"World"}