from paginas.pagina_login import PaginaLogin


def test_login_valido(navegador):
    pagina = PaginaLogin(navegador)
    pagina.entrar("aluno", "ifma2026")
    assert pagina.saudacao() == "Olá, aluno"


def test_login_invalido(navegador):
    pagina = PaginaLogin(navegador)
    pagina.entrar("aluno", "errada")
    assert "inválidos" in pagina.mensagem_de_erro()