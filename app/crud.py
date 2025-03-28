import random
import string
from sqlmodel import Session, select
from fastapi import Depends
from app.models import URL
from app.db.session import get_session

from app.schemas import URLCreate


import string

BASE62_ALPHABET = string.ascii_letters + string.digits  # a-z, A-Z, 0-9


def encode_base62(num: int) -> str:
    """Convert an integer to a Base62 string."""
    if num == 0:
        return BASE62_ALPHABET[0]

    base62 = []
    while num:
        num, rem = divmod(num, 62)
        base62.append(BASE62_ALPHABET[rem])

    return ''.join(base62[::-1])  # Reverse the string


def create_short_url(url_data: URLCreate, db: Session = Depends(get_session)):
    db_url = URL(long_url=url_data.long_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)

    # Convert the auto-incremented ID to a short URL
    short_code = encode_base62(db_url.id)
    db_url.short_url = short_code
    db.commit()

    return db_url


def get_long_url(short_code: str, db: Session = Depends(get_session)):
    query = select(URL).where(URL.short_url == short_code)
    db_url = db.exec(query).first()
    return db_url
