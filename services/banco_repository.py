import sqlite3
from services.database import get_connection
from models.models import *
from models.models_dto import *

class BancoRepository:
    def __init__(self):
        self.con = get_connection()
        self.cur = self.con.cursor()

    def inserir_usuario(self, usuario: Usuario):
        try:
            self.cur.execute("INSERT INTO Usuarios(Nome, Login, Password, DataCadastro) VALUES(?, ?, ?, ?)",
                            (usuario.nome, usuario.login, usuario.password, usuario.data_cadastro.strftime("%Y-%m-%d %H:%M:%S")))
            self.con.commit()
            id_usuario = self.cur.lastrowid
            return id_usuario
        except Exception as ex:
            raise ex

    def atualizar_usuario(self, usuario: Usuario, atualizar_senha: bool = False):
        try:
            if atualizar_senha:
                query = "UPDATE Usuarios Set Nome = ?, Login = ?, Password = ? where Id = ?"
                self.cur.execute(query, (usuario.nome, usuario.login, usuario.password, usuario.id))
            else:
                query = "UPDATE Usuarios Set Nome = ?, Login = ? where Id = ?"
                self.cur.execute(query, (usuario.nome, usuario.login, usuario.id))
            self.con.commit()
        except Exception as ex:
            self.con.rollback()
            raise ex

    def inserir_livro(self, livro: Livro):
        self.cur.execute("INSERT INTO Livros (Titulo, Autor, DataCadastro) VALUES (?, ?, ?)",
                    (livro.titulo, livro.autor, livro.data_cadastro))
        self.con.commit()
        id_livro = self.cur.lastrowid
        return id_livro

    def inserir_capitulo(self, capitulo: Capitulo):
        self.cur.execute("INSERT INTO Capitulos(IdLivro, NrPaginas) VALUES (?, ?)",
                    (capitulo.idlivro, capitulo.nrpaginas))
        self.con.commit()
        id_capitulo = self.cur.lastrowid
        return id_capitulo

    def inserir_pagina(self, pagina: Pagina):
        self.cur.execute("INSERT INTO Paginas(IdCapitulo, NrLinhas) VALUES (?, ?)",
                    (pagina.idcapitulo, pagina.nrlinhas))
        self.con.commit()
        id_pagina = self.cur.lastrowid
        return id_pagina

    def inserir_linha(self, linha: Linha):
        self.cur.execute("INSERT INTO Linhas(IdPagina, Conteudo, PossuiAcao) VALUES (?, ?, ?)",
                    (linha.idpagina, linha.conteudo, linha.possuiacao))
        self.con.commit()
        id_linha = self.cur.lastrowid
        return id_linha

    def inserir_acao(self, acao: Acao):
        self.cur.execute("INSERT INTO Acoes(IdLinha, TipoAcao, PossuiAcaoAutomatica, ProximoPasso) VALUES (?, ?, ?, ?)",
                    (acao.idlinha, acao.tipoacao, acao.possuiacaoautomatica, acao.proximopasso))
        self.con.commit()
        id_acao = self.cur.lastrowid
        return id_acao

    def inserir_acao_automatica(self, acao_automatica: AcaoAutomatica):
        self.cur.execute("INSERT INTO AcoesAutomaticas(IdAcao, PassosAExecutar) VALUES (?, ?)",
                    (acao_automatica.idacao, acao_automatica.passosexecutar))
        self.con.commit()
        id_acao_automatica = self.cur.lastrowid
        return id_acao_automatica

    def inserir_progresso_usuario(self, progresso_usuario: ProgressoUsuario):
        progresso_usuario.idlogin = self.get_proximo_idLogin_progresso_usuario(progresso_usuario.idusuario)
        self.cur.execute("INSERT INTO ProgressoUsuario(IdUsuario, IdLogin,\
                         DataLogin, IdLivro, IdCapitulo, IdPagina, IdLinha)\
                         VALUES(?, ?, ?, ?, ?, ?, ?)")
        self.con.commit()
        return True

    def buscar_usuario_por_id(self, id_usuario: int) ->Optional[Usuario]:
        self.con.row_factory = sqlite3.Row
        self.cur.execute("SELECT * FROM Usuarios WHERE Id = ?", (id_usuario,))
        row_usuario = self.cur.fetchone()
        if not row_usuario:
            return None
        return Usuario(
            id=row_usuario["Id"],
            nome=row_usuario["Nome"],
            login=row_usuario["Login"],
            password=row_usuario["Password"],
            data_cadastro=datetime.strptime(row_usuario["DataCadastro"], '%Y-%m-%d %H:%M:%S')
        )
       
    def buscar_usuario_por_login(self, login: str) ->Optional[Usuario]:
        self.con.row_factory = sqlite3.Row
        self.cur.execute("SELECT * FROM Usuarios WHERE UPPER(Login) = ?", (login.upper(),))
        row_usuario = self.cur.fetchone()
        if not row_usuario:
            return None
        return Usuario(
            id=row_usuario["Id"],
            nome=row_usuario["Nome"],
            login=row_usuario["Login"],
            password=row_usuario["Password"],
            data_cadastro=row_usuario["DataCadastro"]
        )
    
    def checar_login_disponivel(self, login: str, id_usuario: int=0) -> bool:
        self.con.row_factory = sqlite3.Row
        if id_usuario > 0:
           self.cur.execute("SELECT * FROM Usuarios WHERE UPPER(Login) = ? and Id <> ?", (login.upper(), id_usuario,))
        else:
           self.cur.execute("SELECT * FROM Usuarios WHERE UPPER(Login) = ?", (login.upper(),)) 
        row_usuario = self.cur.fetchone()
        if row_usuario:
            return False
        return True

    def buscar_livro(self, id_livro: int) ->Optional[Livro]:
        self.con.row_factory = sqlite3.Row
        self.cur.execute("SELECT * FROM Livros WHERE Id = ?", (id_livro,))
        row_livro = self.cur.fetchone()
        if not row_livro:
            return None
        return Livro(
            id=row_livro["Id"],
            titulo=row_livro["Titulo"],
            autor=row_livro["Autor"],
            data_cadastro=row_livro["DataCadastro"]
        )
   
    def carregar_livro_completo(self, id_livro: int) -> Optional[LivroDTO]:
        # Buscar livro
        livro = self.buscar_livro(id_livro)
        if livro is None:
            return None
        
        livro_dto = LivroDTO(
            id=livro.id,
            titulo=livro.titulo,
            autor=livro.autor,
            data_cadastro=livro.data_cadastro,
            capitulos=[]
        )

        # Buscar capítulos
        self.cur.execute("SELECT * FROM Capitulos WHERE IdLivro = ?", (id_livro,))
        for row_cap in self.cur.fetchall():
            capitulo = CapituloDTO(
                id=row_cap["IdCapitulo"],
                numero_paginas=row_cap["NrPaginas"],
                paginas=[]
            )

            # Buscar páginas
            self.cur.execute("SELECT * FROM Paginas WHERE IdCapitulo = ?", (capitulo.id,))
            for row_pag in self.cur.fetchall():
                pagina = PaginaDTO(
                    id=row_pag["IdPagina"],
                    numero=row_pag["NrLinhas"],  # ou outro campo se houver
                    linhas=[]
                )

                # Buscar linhas
                self.cur.execute("SELECT * FROM Linhas WHERE IdPagina = ?", (pagina.id,))
                for row_lin in self.cur.fetchall():
                    linha = LinhaDTO(
                        id=row_lin["IdLinha"],
                        conteudo=row_lin["Conteudo"],
                        possui_acao=bool(row_lin["PossuiAcao"]),
                        acoes=[]
                    )

                    # Buscar ações
                    self.cur.execute("SELECT * FROM Acoes WHERE IdLinha = ?", (linha.id,))
                    for row_acao in self.cur.fetchall():
                        acao = AcaoDTO(
                            id=row_acao["IdAcao"],
                            tipo=row_acao["TipoAcao"],
                            possui_acao_automatica=bool(row_acao["PossuiAcaoAutomatica"]),
                            proximo_passo=row_acao["ProximoPasso"],
                            acoes_automaticas=[]
                        )

                        # Buscar ações automáticas
                        self.cur.execute("SELECT * FROM AcoesAutomaticas WHERE IdAcao = ?", (acao.id,))
                        for row_auto in self.cur.fetchall():
                            acao_auto = AcaoAutomaticaDTO(
                                id=row_auto["IdAcaoAutomatica"],
                                passos_a_executar=row_auto["PassosAExecutar"]
                            )
                            acao.acoes_automaticas.append(acao_auto)

                        linha.acoes.append(acao)

                    pagina.linhas.append(linha)
                capitulo.paginas.append(pagina)
            livro_dto.capitulos.append(capitulo)

        return livro_dto
    
    def get_proximo_idLogin_progresso_usuario(self, id_usuario: int) -> int:
        self.con.row_factory = sqlite3.Row
        self.cur.execute("SELECT COALESCE(MAX(IdLogin), 0) + 1 as Proximo from ProgressoUsuario Where IdUsuario = ?", (id_usuario,))
        row_idlogin = self.cur.fetchone()
        if not row_idlogin:
            return 1
        return row_idlogin["Proximo"]
    
    def get_progresso_usuario(self, id_usuario: int) -> Optional[ProgressoUsuario]:
        self.con.row_factory = sqlite3.Row
        self.cur.execute("select * from ProgressoUsuario\
                          where IdUsuario = ?\
                          order by IdLogin DESC\
                          limit 1", (id_usuario,))
        row_progresso = self.cur.fetchone()
        if not row_progresso:
            return None
        return ProgressoUsuario(
            idusuario=row_progresso['IdUsuario'],
            idlogin=row_progresso["IdLogin"],
            datalogin=datetime.strptime(row_progresso["DataLogin"], '%Y-%m-%d %H:%M:%S'),
            idlivro=row_progresso["IdLivro"],
            idcapitulo=row_progresso["IdCapitulo"],
            idpagina=row_progresso["IdPagina"],
            idlinha=row_progresso["IdLinha"]
        )
    

