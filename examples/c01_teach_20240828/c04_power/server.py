from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root(a: int, b: int):
    return {"message": a ** b}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8888)
