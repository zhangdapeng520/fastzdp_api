from fastapi import FastAPI

app = FastAPI()


def get_99table():
    talbe99 = ""
    for i in range(1, 10):
        for j in range(1, i + 1):
            talbe99 += f"{j} x {i} = {j * i}\t"
        talbe99 += "\n"
    return talbe99


@app.get("/")
async def root():
    return {"message": get_99table()}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8888)
