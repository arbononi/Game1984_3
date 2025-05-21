from configs.config import lin_terminal, col_terminal

titulos_tela = {
    "menu_principal" : "GAME 1984 - Copyright © 2025 by André Rogério Bononi".center(92, " "),
    "cadastro_usuario": "CADASTRO DE USUÁRIOS".center(115, " "),
    "tela_game" : "GAME 1984 - Copyright © 2025 by André Rogério Bononi - "
}

linha_opcoes = {
    "acesso_sistema" : "[A]CESSAR SISTEMA                [C]ADASTRAR USUÁRIO                [S]AIR DO SISTEMA".center(115, " "),
    "cadastro_usuarios" : "[I]NCLUIR           [A]LTERAR           [E]XCLUIR           [V]ER ITENS           [C]ANCELAR           [R]ETORNAR".center(115, " "),
    "confirmar_dados" : "Confirmar Dados (S/N)? "
}

opcoes_disponiveis = {
    "acesso_sistema" : [ "A", "C", "S" ],
    "cadastro_usuarios" : [ "I", "A", "E", "V", "C", "R"],
    "confirmar_dados": [ "S", "N" ]
}


tela_principal = [
    { "lin" :  1, "col" : 2, "value" : "╔" + "═" * (col_terminal - 27) + "╦══════════════════════╗" },
    { "lin" :  2, "col" : 2, "value" : "║" + " " * (col_terminal - 27) + "║ DATA:                ║" },
    { "lin" :  3, "col" : 2, "value" : "╠" + "═" * (col_terminal - 27) + "╩══════════════════════╣" },
    { "lin" :  4, "col" : 2, "value" : "║" + " " * (col_terminal - 4) + "║" },
    { "lin" : lin_terminal - 2, "col" : 2, "value" : "╠" + "═" * (col_terminal - 4) + "╣" },
    { "lin" : lin_terminal - 1, "col" : 2, "value" : "║" + " " * (col_terminal - 4) + "║" },
    { "lin" : lin_terminal, "col" : 2, "value" : "╚" + "═" * (col_terminal - 4) + "╝" }
]

tela_capitulos = [
    { "lin" :  3, "col" : 2, "value" : "╠" + "═" * (col_terminal - 43) + "╦═══════════════╩══════════════════════╣" },
    { "lin" :  4, "col" : 2, "value" : "║" + " " * (col_terminal - 43) + "║                                      ║" },
    { "lin" : lin_terminal - 2, "col": 2, "value" : "╠" + "═" * (col_terminal - 43) + "╩══════════════════════════════════════╣" }
]

tela_login = [
    { "lin" : 14, "col" : 44, "value" : " ╔═══════════════════════════════╗" },
    { "lin" : 15, "col" : 44, "value" : "█║                               ║" },
    { "lin" : 16, "col" : 44, "value" : "█║ LOGIN: [                    ] ║" },
    { "lin" : 17, "col" : 44, "value" : "█║                               ║" },
    { "lin" : 18, "col" : 44, "value" : "█║ SENHA: [                    ] ║" },
    { "lin" : 19, "col" : 44, "value" : "█║                               ║" },
    { "lin" : 20, "col" : 44, "value" : "█╚═══════════════════════════════╝" },
    { "lin" : 21, "col" : 44, "value" : "▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ " },
]

tela_usuarios = [
    { "lin" :  5, "col" : 2, "value" : "╠" + "═" * (col_terminal - 4) + "╣" },
    { "lin" :  7, "col" : 2, "value" : "║ CÓDIGO ......: [      ]                NOME ........: [                    ] LOGIN .......: [                    ] ║"},
    { "lin" :  9, "col" : 2, "value" : "║ SENHA .......: [                    ]  CONFIRMAR ...: [                    ] DATA CADASTRO: [          ]           ║"}
]

rosto = [
    "   ~^~^~^~^~^~^~^~^~^~^~^~^~^~^",
    "  /----------------------------\\",
    " /                              \\",
    "|                                |",
    "|           O         O          |",
    "|                                |",
    "|                >               |",
    "|                                |",
    "|                                |",
    " \\       \______________/       /",
    "  \\                            /",
    "   \\                          /",
    "    \\                        /",
    "     \\                      /",
    "      \\____________________/"
]

legenda_rosto = "O Grande Irmão está vigiando você!". center(38, " ")