from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Hello Anand! FastApi Is Working!"}