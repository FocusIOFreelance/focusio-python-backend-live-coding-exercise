import sqlite3
from typing import List, Dict, Optional
import os

DB_PATH = os.path.join(os.getcwd(), 'data', os.getenv('DB_FILE', 'dev.sqlite'))

def _get_conn():
    # Use a connection per call (sqlite in python is threadsafe when used like this)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def get_favorite_by_id(id: int) -> Optional[Dict]:
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute('SELECT id, name, created_at, updated_at FROM favorites WHERE id = ?', (id,))
    row = cur.fetchone()
    conn.close()
    if not row:
        return None
    return dict(row)


def list_favorites() -> List[Dict]:
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute('SELECT id, name, created_at, updated_at FROM favorites ORDER BY id DESC')
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]


def insert_favorite(data: Dict) -> Dict:
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute('INSERT INTO favorites (name) VALUES (?)', (data['name'],))
    conn.commit()
    last_id = cur.lastrowid
    cur.execute('SELECT id, name, created_at, updated_at FROM favorites WHERE id = ?', (last_id,))
    row = cur.fetchone()
    conn.close()
    return dict(row)


def delete_favorite(id: int) -> bool:
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute('DELETE FROM favorites WHERE id = ?', (id,))
    conn.commit()
    changes = cur.rowcount
    conn.close()
    return changes > 0
