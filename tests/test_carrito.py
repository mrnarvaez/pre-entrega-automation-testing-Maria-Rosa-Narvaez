from selenium.webdriver.common.by import By
from utils.helpers import (
    login,
    agregar_primer_producto,
    abrir_carrito
)


def test_agregar_producto_carrito(driver):

    login(
        driver,
        "standard_user",
        "secret_sauce"
    )

    # Obtener nombre del producto
    producto = driver.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text

    # Agregar producto
    agregar_primer_producto(driver)

    # Verificar contador carrito
    contador = driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_badge"
    ).text

    assert contador == "1"

    # Abrir carrito
    abrir_carrito(driver)

    # Verificar producto en carrito
    producto_carrito = driver.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text

    assert producto == producto_carrito