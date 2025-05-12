# Projeto: RPG com base no Livro 1984 de George Orwell
# Data Início: 08/05/2025.
# Versão 1.0.2025.05
# Autor: André Rogério Bononi e Filhos
# Contato: arbononi@gmail.com

import os
import locale
from os import system as clear_screen
from services.database import open_connection, close_connection
from utils.userfunctions import *
from layouts.layouts import tela_principal, rosto, tela_capitulos, legenda_rosto
from configs.config import lin_terminal, col_terminal, lin_message

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def set_size_terminal(lines=30, columns=100):
    os.system(f"mode con: cols={columns} lines={lines}")

def iniciar():
    desenhar_tela(layout=tela_principal, line_loop=4, stop_loop=lin_message - 1)
    str_data_atual = formatar_data(get_data_atual(), True, True)
    exibir_conteudo(str_data_atual, lin=2, col=104)
    try:
        open_connection()
        limpar_linha()
        exibir_mensagem("Pressione qualquer tecla para continuar...", wait_key=True)
    except Exception as ex:
        exibir_mensagem(ex, wait_key=True)

if __name__ == "__main__":
    os.system("chcp 65001 > nul")
    clear_screen("cls")
    set_size_terminal(lin_terminal, col_terminal)
    iniciar()
    clear_screen("cls") 
    close_connection()
