import sqlite3
from typing import List, Tuple

class SearchIndex:
    """
    Offline-capable search engine for the community library.
    """
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self._create_schema()

    def _create_schema(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS resources (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    description TEXT,
                    path TEXT UNIQUE
                )
            """)

    def index_resource(self, title: str, description: str, path: str):
        with self.conn:
            self.conn.execute(
                "INSERT OR REPLACE INTO resources (title, description, path) VALUES (?, ?, ?)",
                (title, description, path)
            )

    def search(self, query: str) -> List[Tuple]:
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT title, path FROM resources WHERE title LIKE ? OR description LIKE ?",
            (f"%{query}%", f"%{query}%")
        )
        return cursor.fetchall()
