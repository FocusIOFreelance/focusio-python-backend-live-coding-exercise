import httpx
from typing import List, Dict
from urllib.parse import quote

BASE = 'https://rickandmortyapi.com/api/character/'


async def get_characters(name: str | None = None) -> List[Dict]:
    q = (name or '').strip()
    url = f"{BASE}?name={quote(q)}" if q else BASE
    try:
        async with httpx.AsyncClient() as client:
            res = await client.get(url, timeout=10.0)
            if res.status_code != 200:
                if res.status_code == 404:
                    return []
                raise Exception(f'rickandmortyapi returned {res.status_code}')
            body = res.json()
            return body.get('results', [])
    except Exception:
        return []
