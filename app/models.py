from sqlmodel import SQLModel, Field
from typing import Optional


class URL(SQLModel, table=True):
    __tablename__ = "urls"

    id: int = Field(primary_key=True, index=True)
    short_url: Optional[str] = Field(unique=True, index=True)
    long_url: str = Field(unique=True)
    clicks: int = Field(default=0)
