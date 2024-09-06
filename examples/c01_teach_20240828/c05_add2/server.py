from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root(a: int, b: int, c: int, d: int, e: int):
    return {"message": a + b + c + d + e}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8888)
