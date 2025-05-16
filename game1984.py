# Projeto: RPG com base no Livro 1984 de George Orwell
# Data Início: 08/05/2025.
# Versão 1.0.2025.05
# Autor: André Rogério Bononi e Filhos
# Contato: arbononi@gmail.com

import os
import locale
from os import system as clear_screen
from services.database import _DB_PATH
from services.database import open_connection, close_connection, create_database
from services.banco_repository import BancoRepository
from utils.userfunctions import *
from layouts.layouts import *
from configs.config import *
from controllers.usuario_controller import UsuarioController

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
_banco = None

def set_size_terminal(lines=30, columns=100):
    os.system(f"mode con: cols={columns} lines={lines}")

def check_database():
    arquivo = _DB_PATH
    if arquivo.is_file():
        return True
    try:
        return create_database()
    except Exception as ex:
        print(ex)
        return False

def acessar_sistema():
    pass

def cadastrar_usuario():
    usuario_controller = UsuarioController(_banco)
    usuario_controller.iniciar()

def iniciar():
    desenhar_tela(layout=tela_principal, line_loop=4, stop_loop=lin_message - 1)
    exibir_conteudo(titulos_tela["menu_principal"], lin=2, col=4)
    str_data_atual = formatar_data(get_data_atual(), True, True)
    exibir_conteudo(str_data_atual, lin=2, col=104)
    try:
        open_connection()
        while True:
            limpar_tela()
            limpar_linha()
            opcao = exibir_mensagem(linha_opcoes["acesso_sistema"], wait_key=True).upper()
            if opcao not in opcoes_disponiveis["acesso_sistema"]:
                limpar_linha()
                exibir_mensagem("Opção inválida!", wait_key=True)
                continue
            if opcao == 'S':
                break
            if opcao == "L":
                acessar_sistema()
            if opcao == "C":
                cadastrar_usuario()
            
    except Exception as ex:
        exibir_mensagem(ex, wait_key=True)

if __name__ == "__main__":
    os.system("chcp 65001 > nul")
    clear_screen("cls")
    set_size_terminal(lin_terminal, col_terminal)
    if not check_database():
        exit()
    _banco = BancoRepository()
    iniciar()
    clear_screen("cls") 
    close_connection()
