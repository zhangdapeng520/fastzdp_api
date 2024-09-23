from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import BaseModel
from fastapi import APIRouter
from fastapi.responses import JSONResponse
import fastzdp_sqlmodel as fasm
import fastzdp_api as api


class Classes(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class ClassesSchema(BaseModel):
    name: str


def get_classes_router(engine):
    """得到班级的路由对象"""
    # router = APIRouter(tags=["班级管理"])
    #
    # @router.post("/classes", summary="新增班级")
    # async def add_classes(req_data: ClassesSchema):
    #     fasm.add(engine, Classes(name=req_data.name))
    #     return None
    #
    # @router.put("/classes/{id}", summary="更新班级")
    # async def update_classes(id: int, req_data: ClassesSchema):
    #     classes = fasm.get(engine, Classes, id)
    #     if not classes:
    #         return JSONResponse(status_code=404, content={"error": "数据不存在"})
    #
    #     fasm.update(engine, classes, req_data.model_dump())
    #     return None
    #
    # @router.delete("/classes/{id}", summary="删除班级")
    # async def delete_classes(id: int):
    #     fasm.delete_id(engine, Classes, id)
    #     return None
    #
    # @router.get("/classes", summary="查询班级")
    # async def get_classes(page: int = 1, size: int = 8):
    #     return fasm.get_page(engine, Classes, page, size)
    #
    # return router
    return api.get_crud_router(engine, ClassesSchema, Classes, "班级")
