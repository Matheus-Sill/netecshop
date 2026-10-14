from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_login import fazer_login


def entrar_no_catalogo(driver):
    fazer_login(driver)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "campo-busca"))
    )


def test_catalogo_lista_seis_produtos(navegador):
    entrar_no_catalogo(navegador)

    produtos = navegador.find_elements(By.CSS_SELECTOR, ".produto")

    assert len(produtos) == 6


def test_busca_filtra_resultados(navegador):
    entrar_no_catalogo(navegador)

    navegador.find_element(By.ID, "campo-busca").send_keys("mouse")
    navegador.find_element(By.ID, "btn-buscar").click()

    WebDriverWait(navegador, 10).until(
        lambda d: len(
            d.find_elements(By.CSS_SELECTOR, ".produto")
        ) == 1
    )

    nome = navegador.find_element(
        By.CSS_SELECTOR, ".produto .produto-nome"
    ).text

    assert "Mouse" in nome


def test_busca_sem_resultado(navegador):
    entrar_no_catalogo(navegador)

    navegador.find_element(By.ID, "campo-busca").send_keys("impressora")
    navegador.find_element(By.ID, "btn-buscar").click()

    aviso = WebDriverWait(navegador, 10).until(
        EC.visibility_of_element_located((By.ID, "msg-vazio"))
    )

    assert "Nenhum produto" in aviso.text

    assert navegador.find_elements(
        By.CSS_SELECTOR, ".produto"
    ) == []

    
def test_assinar_newsletter_dentro_do_iframe(navegador):
    entrar_no_catalogo(navegador)
    espera = WebDriverWait(navegador, 10)

    # 1) Entrar no contexto do iframe
    espera.until(
        EC.frame_to_be_available_and_switch_to_it(
            (By.ID, "frame-newsletter")
        )
    )

    # 2) Interagir com os elementos do documento interno
    navegador.find_element(
        By.ID, "email-news"
    ).send_keys("aluno@acad.ifma.edu.br")

    navegador.find_element(By.ID, "btn-assinar").click()

    msg = espera.until(
        EC.visibility_of_element_located((By.ID, "msg-news"))
    )

    assert "inscrito" in msg.text.lower()

    # 3) Voltar ao documento principal
    navegador.switch_to.default_content()

    assert navegador.find_element(
        By.ID, "contador-carrinho"
    ).is_displayed()
