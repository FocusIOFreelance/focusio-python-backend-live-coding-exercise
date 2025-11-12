from typing import Optional, List, Dict
from db import favorites_repository


def get_favorite(id: int) -> Optional[Dict]:
    return favorites_repository.get_favorite_by_id(id)


def list_favorites() -> List[Dict]:
    return favorites_repository.list_favorites()


def create_favorite(data: Dict) -> Dict:
    return favorites_repository.insert_favorite({'name': data['name']})


def delete_favorite(id: int) -> bool:
    return favorites_repository.delete_favorite(id)
