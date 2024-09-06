from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class AddRequest(BaseModel):
    arr: list[int]


@app.get("/")
async def root(req_data: AddRequest):
    return {"result": sum(req_data.arr)}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8888)
