from email.policy import default

from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import BaseModel
import fastzdp_api as api


class Course(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(default=None)
    class_id: int = Field(default=None)
    class_name: str = Field(default=None)
    price: int = Field(default=None)
    order: int = Field(default=None)
    add_time: int = Field(default=None)


class CourseSchema(BaseModel):
    name: str
    class_id: int
    class_name: str
    price: int
    order: int
    add_time: int


def get_course_router(engine):
    """得到班级的路由对象"""
    return api.get_crud_router(engine, CourseSchema, Course)
