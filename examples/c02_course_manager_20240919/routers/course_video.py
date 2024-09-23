from email.policy import default

from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import BaseModel
import fastzdp_api as api


class CourseVideo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(default=None)
    course_id: int = Field(default=None)
    course_name: str = Field(default=None)
    order: int = Field(default=None)
    add_time: int = Field(default=None)


class CourseVideoSchema(BaseModel):
    name: str
    course_id: int
    course_name: str
    order: int
    add_time: int


def get_course_video_router(engine):
    """得到班级的路由对象"""
    return api.get_crud_router(engine, CourseVideoSchema, CourseVideo)
