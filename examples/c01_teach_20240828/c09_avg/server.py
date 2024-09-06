from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class AddRequest(BaseModel):
    arr: list[int]


@app.get("/")
async def root(req_data: AddRequest):
    return {
        "sum": sum(req_data.arr),
        "min": min(req_data.arr),
        "max": max(req_data.arr),
        "avg": sum(req_data.arr) / len(req_data.arr),
    }


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8888)
