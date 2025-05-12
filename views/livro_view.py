# views/livro_view.py

from models.models_dto import LivroDTO, CapituloDTO, PaginaDTO, LinhaDTO, AcaoDTO, AcaoAutomaticaDTO

def exibir_livro_completo(livro: LivroDTO):
    print("\n=== LIVRO COMPLETO ===")
    exibir(livro)
    for capitulo in livro.capitulos:
        exibir_capitulo(capitulo)

def exibir(livro: LivroDTO):
    print(f"\n📚 Livro ID: {livro.id}")
    print(f"   Título: {livro.titulo}")
    print(f"   Autor: {livro.autor}")
    print(f"   Data de Cadastro: {livro.data_cadastro}")

def exibir_capitulo(capitulo: CapituloDTO):
    print(f"\n--- Capítulo ID: {capitulo.id} | Nº de Páginas: {capitulo.numero_paginas} ---")
    for pagina in capitulo.paginas:
        exibir_pagina(pagina)

def exibir_pagina(pagina: PaginaDTO):
    print(f"\n📄 Página ID: {pagina.id} | Nº Linhas: {len(pagina.linhas)}")
    for linha in pagina.linhas:
        exibir_linha(linha)

def exibir_linha(linha: LinhaDTO):
    print(f"\n📝 Linha ID: {linha.id}")
    print(f"   Conteúdo: {linha.conteudo.strip()}")
    print(f"   Possui Ação? {'Sim' if linha.possui_acao else 'Não'}")

    for acao in linha.acoes:
        exibir_acao(acao)

def exibir_acao(acao: AcaoDTO):
    print(f"\n   🔁 Ação ID: {acao.id}")
    print(f"      Tipo: {acao.tipo}")
    print(f"      Próximo Passo: {acao.proximo_passo}")
    print(f"      Possui Ação Automática? {'Sim' if acao.possui_acao_automatica else 'Não'}")

    for auto in acao.acoes_automaticas:
        exibir_acao_automatica(auto)

def exibir_acao_automatica(auto: AcaoAutomaticaDTO):
    print(f"\n      ⚙️ Ação Automática ID: {auto.id}")
    print(f"         Passos a Executar: {auto.passos_a_executar}")
