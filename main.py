from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def hello_world():
    return JSONResponse(content={'message': 'hello chatGPT'}, status_code=200)

@app.get("/{n}")
def hello_world(n: int):
    n_1 = n + 1
    return JSONResponse(content={"n": n_1}, status_code=200)