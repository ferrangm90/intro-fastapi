from fastapi import FastAPI

app = FastAPI()

@app.get("/hola")
def index():
    return {"message": "Hola, mundo!"}
