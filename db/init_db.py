import sqlite3
import os
from pathlib import Path

DATA_DIR = Path(os.getcwd()) / 'data'
DB_FILE = os.getenv('DB_FILE', 'dev.sqlite')
DB_PATH = DATA_DIR / DB_FILE

MIGRATION_SQL = '''
CREATE TABLE IF NOT EXISTS favorites (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TRIGGER IF NOT EXISTS favorites_update_timestamp
AFTER UPDATE ON favorites
FOR EACH ROW
BEGIN
  UPDATE favorites SET updated_at = datetime('now') WHERE id = OLD.id;
END;
'''


def run_migrations():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.executescript(MIGRATION_SQL)
        conn.commit()
        print('Migrations applied. DB file:', str(DB_PATH))
    finally:
        conn.close()


if __name__ == '__main__':
    run_migrations()
