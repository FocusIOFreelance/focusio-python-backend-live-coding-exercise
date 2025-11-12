from fastapi import APIRouter

from . import favorites, characters

router = APIRouter()

# Mount child routers with same paths as Node app
router.include_router(favorites.router)
router.include_router(characters.router)
