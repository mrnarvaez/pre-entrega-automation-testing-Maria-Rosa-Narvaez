import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Configuración de logs
logging.basicConfig(
    filename="logs/test_execution.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)


URL = "https://www.saucedemo.com/"


def login(driver, username, password):

    logging.info("Abriendo página SauceDemo")

    driver.get(URL)

    logging.info("Ingresando usuario")
    driver.find_element(By.ID, "user-name").send_keys(username)

    logging.info("Ingresando contraseña")
    driver.find_element(By.ID, "password").send_keys(password)

    logging.info("Haciendo click en Login")
    driver.find_element(By.ID, "login-button").click()

    # Espera explícita
    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )

    logging.info("Login exitoso")


def obtener_productos(driver):

    logging.info("Obteniendo lista de productos")

    return driver.find_elements(By.CLASS_NAME, "inventory_item")


def agregar_primer_producto(driver):

    logging.info("Agregando primer producto al carrito")

    boton = driver.find_element(By.CSS_SELECTOR, ".btn_inventory")
    boton.click()


def abrir_carrito(driver):

    logging.info("Abriendo carrito de compras")

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()