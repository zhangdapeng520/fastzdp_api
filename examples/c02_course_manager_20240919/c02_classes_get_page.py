import fastzdp_sqlmodel as fasm

from fastapi import FastAPI
from pydantic import BaseModel
from sqlmodel import SQLModel, Field
from typing_extensions import Optional

engine = fasm.get_engine(password="zhangdapeng520", database="fastzdp_sqlmodel")
app = FastAPI()


class Classes(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class ClassesSchema(BaseModel):
    name: str

@app.post("/classes")
async def add_classes(req_data: ClassesSchema):
    fasm.add(engine, Classes(name=req_data.name))
    return None

@app.get("/classes")
async def get_classes(page: int = 1, size: int = 8):
    return fasm.get_page(engine, Classes, page, size)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8888)
