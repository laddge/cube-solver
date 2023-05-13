from fastapi import FastAPI
import kociemba

app = FastAPI()


@app.get("/api")
async def get_api(cubestr: str):
    try:
        solution = kociemba.solve(cubestr).split()
    except Exception as e:
        print(e)
        solution = []
    return {"solution": solution}
