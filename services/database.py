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

def create_database():
    global _connection
    _ = get_connection()
    cursor = _connection.cursor()
    try:
        create_table_usuarios(cursor)
        create_table_progressousuario(cursor)
        create_table_livros(cursor)
        create_table_capitulos(cursor)
        create_table_paginas(cursor)
        create_table_linhas(cursor)
        create_table_acoes(cursor)
        create_table_acoes_automaticas(cursor)
        _connection.commit()
        return True
    except Exception as ex:
        _connection.rollback()
        raise ex

def create_table_usuarios(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Usuarios(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT NOT NULL,
            Login TEXT NOT NULL,
            Password BLOB NOT NULL,
            DataCadastro TEXT NOT NULL
        );
    """)

def create_table_progressousuario(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ProgressoUsuario(
            IdUsuario INTEGER NOT NULL,
            IdLogin INTEGER NOT NULL,
            DataLogin TEXT NOT NULL,
            IdLivro INTEGER NOT NULL,
            IdCapitulo INTEGER NOT NULL,
            IdPagina INTEGER NOT NULL,
            IdLinha INTEGER NOT NULL,
            PRIMARY KEY(IdUsuario, IdLogin)
        );
    """)

def create_table_livros(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Livros (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Titulo TEXT NOT NULL,
            Autor TEXT,
            DataCadastro TEXT NOT NULL
        );
    """)

def create_table_capitulos(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Capitulos (
            IdCapitulo INTEGER PRIMARY KEY AUTOINCREMENT,
            IdLivro INTEGER NOT NULL,
            NrPaginas INTEGER NOT NULL,
            FOREIGN KEY (IdLivro) REFERENCES Livros(Id)
        );
    """)

def create_table_paginas(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Paginas (
            IdPagina INTEGER PRIMARY KEY AUTOINCREMENT,
            IdCapitulo INTEGER NOT NULL,
            NrLinhas INTEGER NOT NULL,
            FOREIGN KEY (IdCapitulo) REFERENCES Capitulos(IdCapitulo)
        );
    """)

def create_table_linhas(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Linhas (
            IdLinha INTEGER PRIMARY KEY AUTOINCREMENT,
            IdPagina INTEGER NOT NULL,
            PossuiAcao INTEGER NOT NULL CHECK (PossuiAcao IN (0, 1)),
            FOREIGN KEY (IdPagina) REFERENCES Paginas(IdPagina)
        );
    """)

def create_table_acoes(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Acoes (
            IdAcao INTEGER PRIMARY KEY AUTOINCREMENT,
            IdLinha INTEGER NOT NULL,
            TipoAcao TEXT NOT NULL,
            PossuiAcaoAutomatica INTEGER NOT NULL CHECK (PossuiAcaoAutomatica IN (0, 1)),
            ProximoPasso TEXT,
            FOREIGN KEY (IdLinha) REFERENCES Linhas(IdLinha)
        );
    """)

def create_table_acoes_automaticas(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS AcoesAutomaticas (
            IdAcaoAutomatica INTEGER PRIMARY KEY AUTOINCREMENT,
            IdAcao INTEGER NOT NULL,
            PassosAExecutar TEXT NOT NULL,
            FOREIGN KEY (IdAcao) REFERENCES Acoes(IdAcao)
        );
    """)