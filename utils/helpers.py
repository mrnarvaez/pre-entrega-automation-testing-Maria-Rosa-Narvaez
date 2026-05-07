from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://www.saucedemo.com/"


def login(driver, username, password):

    driver.get(URL)

    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    # Espera explícita
    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )


def obtener_productos(driver):

    return driver.find_elements(By.CLASS_NAME, "inventory_item")


def agregar_primer_producto(driver):

    boton = driver.find_element(By.CSS_SELECTOR, ".btn_inventory")
    boton.click()


def abrir_carrito(driver):

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()