from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_catalogo import entrar_no_catalogo


def test_adicionar_itens_ao_carrinho(navegador):
    entrar_no_catalogo(navegador)
    espera = WebDriverWait(navegador, 10)

    navegador.find_element(By.ID, "add-TEC-001").click()
    navegador.find_element(By.ID, "add-SSD-004").click()

    espera.until(
        EC.text_to_be_present_in_element(
            (By.ID, "contador-carrinho"), "2"
        )
    )

    navegador.find_element(By.ID, "btn-ir-carrinho").click()

    linhas = navegador.find_elements(
        By.CSS_SELECTOR, "tr.item-carrinho"
    )

    assert len(linhas) == 2

    skus = [
        linha.find_element(By.CSS_SELECTOR, ".item-sku").text
        for linha in linhas
    ]

    assert "TEC-001" in skus
    assert "SSD-004" in skus


def test_esvaziar_carrinho_aceitando_dialogo(navegador):
    entrar_no_catalogo(navegador)
    espera = WebDriverWait(navegador, 10)

    navegador.find_element(By.ID, "add-MOU-002").click()
    navegador.find_element(By.ID, "btn-ir-carrinho").click()
    navegador.find_element(By.ID, "btn-limpar").click()

    alerta = espera.until(EC.alert_is_present())

    assert "remover todos" in alerta.text.lower()

    alerta.accept()

    espera.until(
        EC.text_to_be_present_in_element(
            (By.ID, "contador-carrinho"), "0"
        )
    )

    assert navegador.find_elements(
        By.CSS_SELECTOR, "tr.item-carrinho"
    ) == []


def test_cancelar_limpeza_mantem_item(navegador):
    entrar_no_catalogo(navegador)
    espera = WebDriverWait(navegador, 10)

    navegador.find_element(By.ID, "add-MOU-002").click()
    navegador.find_element(By.ID, "btn-ir-carrinho").click()
    navegador.find_element(By.ID, "btn-limpar").click()

    alerta = espera.until(EC.alert_is_present())

    assert "remover todos" in alerta.text.lower()

    alerta.dismiss()

    espera.until(
        EC.text_to_be_present_in_element(
            (By.ID, "contador-carrinho"), "1"
        )
    )

    linhas = navegador.find_elements(
        By.CSS_SELECTOR, "tr.item-carrinho"
    )

    assert len(linhas) == 1

    sku = linhas[0].find_element(
        By.CSS_SELECTOR, ".item-sku"
    ).text

    assert sku == "MOU-002"