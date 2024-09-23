from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import BaseModel
import fastzdp_api as api


class Classes(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class ClassesSchema(BaseModel):
    name: str


def get_classes_router(engine):
    """得到班级的路由对象"""
    return api.get_crud_router(engine, ClassesSchema, Classes)
