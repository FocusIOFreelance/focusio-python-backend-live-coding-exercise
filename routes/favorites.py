from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from services import favorites_service

router = APIRouter()

class FavoriteIn(BaseModel):
    name: str

class FavoriteOut(BaseModel):
    id: int
    name: str
    created_at: str | None = None
    updated_at: str | None = None

@router.get('/favorites', response_model=List[FavoriteOut])
def list_favorites():
    return favorites_service.list_favorites()

@router.get('/favorites/{id}', response_model=FavoriteOut)
def get_favorite(id: int):
    fav = favorites_service.get_favorite(id)
    if not fav:
        raise HTTPException(status_code=404, detail='not found')
    return fav

@router.post('/favorites', status_code=201, response_model=FavoriteOut)
def create_favorite(payload: FavoriteIn):
    name = payload.name.strip()
    if not name:
        raise HTTPException(status_code=400, detail='field "name" is required')
    try:
        created = favorites_service.create_favorite({"name": name})
        return created
    except Exception:
        raise HTTPException(status_code=500, detail='failed to create favorite')

@router.delete('/favorites/{id}')
def delete_favorite(id: int):
    ok = favorites_service.delete_favorite(id)
    if not ok:
        raise HTTPException(status_code=404, detail='not found')
    return {"deleted": True}
