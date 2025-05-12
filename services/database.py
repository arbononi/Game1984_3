# database.py
import sqlite3
from pathlib import Path

_DB_PATH = Path("data/livros.db")
_connection = None

def open_connection():
    _ = get_connection()
    
def get_connection():
    global _connection
    if _connection is None:
        _connection = sqlite3.connect(_DB_PATH)
        _connection.row_factory = sqlite3.Row  # Para acessar colunas por nome
    return _connection

def close_connection():
    global _connection
    if _connection:
        _connection.close()
        _connection = None
