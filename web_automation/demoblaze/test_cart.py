import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCart:
    def test_add_cart(self, driver):
        driver.get("https://www.demoblaze.com")
        first_phone = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "hrefch"))
        )
        first_phone.click()
        add_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Add to cart"))
        )
        add_btn.click()
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        assert driver.switch_to.alert.text == "Product added"
        driver.switch_to.alert.accept()