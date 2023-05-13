from fastapi import FastAPI
from fastapi.responses import FileResponse
import kociemba

app = FastAPI()


@app.get("/")
async def get_root():
    return FileResponse("./front/dist/index.html")


@app.get("/api")
async def get_api(cubestr: str):
    try:
        solution = kociemba.solve(cubestr).split()
    except Exception as e:
        print(e)
        solution = []
    return {"solution": solution}


@app.get("/{path}")
async def get_front(path: str):
    return FileResponse(f"./front/dist/{path}")


@app.get("/assets/{path}")
async def get_assets(path: str):
    return FileResponse(f"./front/dist/assets/{path}")
