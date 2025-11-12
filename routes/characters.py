from fastapi import APIRouter, HTTPException
from typing import List, Any
from services import characters_service

router = APIRouter()

@router.get('/characters')
async def get_characters(name: str | None = None):
    try:
        characters = await characters_service.get_characters(name)
        return characters
    except Exception:
        # Node returns 502 on failure
        raise HTTPException(status_code=502, detail='failed to fetch characters')
