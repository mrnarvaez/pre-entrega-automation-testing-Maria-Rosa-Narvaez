from utils.helpers import login


def test_login_exitoso(driver):

    login(
        driver,
        "standard_user",
        "secret_sauce"
    )

    # Validación URL
    assert "inventory.html" in driver.current_url

    # Validación título
    assert "Swag Labs" in driver.title

    # Validación texto Products
    titulo = driver.find_element("class name", "title").text

    assert titulo == "Products"