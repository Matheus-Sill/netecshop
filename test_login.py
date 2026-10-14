
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def fazer_login(driver, usuario="aluno", senha="ifma2026"):
    driver.find_element(By.ID, "usuario").send_keys(usuario)
    driver.find_element(By.ID, "senha").send_keys(senha)
    driver.find_element(By.ID, "btn-entrar").click()

#teste de login
def test_login_valido(navegador):
    fazer_login(navegador)

    espera = WebDriverWait(navegador, 10)
    saudacao = espera.until(
        EC.visibility_of_element_located((By.ID, "ola-usuario"))
    )

    assert saudacao.text == "Olá, aluno"

#teste do selo
def test_selo_promocional(navegador):
    fazer_login(navegador)

    espera = WebDriverWait(navegador, 10)
    selo = espera.until(
        EC.visibility_of_element_located((By.ID, "selo-promocao"))
    )

    assert selo.is_displayed()

#teste de senha invalida
def test_login_senha_invalida(navegador):
    fazer_login(navegador, "aluno", "senha-errada")

    msg = WebDriverWait(navegador, 10).until(
        EC.visibility_of_element_located((By.ID, "msg-erro"))
    )

    assert "inválidos" in msg.text
    assert not navegador.find_element(
        By.ID, "tela-catalogo"
    ).is_displayed()

#teste de conta bloqueada
def test_conta_bloqueada(navegador):
    fazer_login(navegador, "bloqueado", "ifma2026")

    msg = WebDriverWait(navegador, 10).until(
        EC.visibility_of_element_located((By.ID, "msg-erro"))
    )

    assert "bloqueada" in msg.text.lower()
