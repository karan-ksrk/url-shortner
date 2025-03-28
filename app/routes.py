from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlmodel import Session
from app.schemas import URLResponse, URLCreate
from app.db.session import get_session
from app.crud import get_long_url, create_short_url
router = APIRouter()


@router.post("/shortner", response_model=URLResponse)
def shortner_url(url_data: URLCreate, db: Session = Depends(get_session)):
    db_url = create_short_url(url_data, db)
    return URLResponse(long_url=db_url.long_url, short_url=db_url.short_url, clicks=db_url.clicks)


@router.get("/{short_code}")
def redirect_to_long_url(short_code: str, db: Session = Depends(get_session)):
    db_url = get_long_url(short_code, db)
    if not db_url:
        raise HTTPException(status_code=404, detail="URL not found")
    db_url.clicks += 1
    db.commit()
    return RedirectResponse(url=db_url.long_url)
