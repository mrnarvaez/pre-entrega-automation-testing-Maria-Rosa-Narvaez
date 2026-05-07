from selenium.webdriver.common.by import By
from utils.helpers import login, obtener_productos


def test_catalogo_productos(driver):

    login(
        driver,
        "standard_user",
        "secret_sauce"
    )

    # Validar Products
    titulo = driver.find_element(By.CLASS_NAME, "title").text

    assert titulo == "Products"

    # Validar productos visibles
    productos = obtener_productos(driver)

    assert len(productos) > 0

    # Validar menú
    menu = driver.find_element(By.ID, "react-burger-menu-btn")

    assert menu.is_displayed()

    # Validar filtro
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")

    assert filtro.is_displayed()

    # Nombre y precio del primero
    primer_nombre = driver.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text

    primer_precio = driver.find_element(
        By.CLASS_NAME,
        "inventory_item_price"
    ).text

    print(f"\nPrimer producto: {primer_nombre}")
    print(f"Precio: {primer_precio}")