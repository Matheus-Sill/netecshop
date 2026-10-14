from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PaginaLogin:
    CAMPO_USUARIO = (By.ID, "usuario")
    CAMPO_SENHA = (By.ID, "senha")
    BOTAO_ENTRAR = (By.ID, "btn-entrar")
    MENSAGEM_ERRO = (By.ID, "msg-erro")
    SAUDACAO = (By.ID, "ola-usuario")

    def __init__(self, driver, tempo=10):
        self.driver = driver
        self.espera = WebDriverWait(driver, tempo)

    def entrar(self, usuario, senha):
        self.driver.find_element(*self.CAMPO_USUARIO).send_keys(usuario)
        self.driver.find_element(*self.CAMPO_SENHA).send_keys(senha)
        self.driver.find_element(*self.BOTAO_ENTRAR).click()
        return self

    def saudacao(self):
        return self.espera.until(
            EC.visibility_of_element_located(self.SAUDACAO)
        ).text

    def mensagem_de_erro(self):
        return self.espera.until(
            EC.visibility_of_element_located(self.MENSAGEM_ERRO)
        ).text