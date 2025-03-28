from pydantic import BaseModel
from typing import Optional


class URLBase(BaseModel):
    long_url: str


class URLCreate(URLBase):
    pass


class URLResponse(URLBase):
    short_url: Optional[str]
    clicks: int

    class Config:
        from_attributes = True
