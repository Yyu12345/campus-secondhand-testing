import pytest, time
from selenium.webdriver.common.by import By

class TestCart:
    def test_add_cart(self, driver):
        driver.get("https://www.demoblaze.com")
        # 点击第一个商品
        driver.find_element(By.CLASS_NAME, "hrefch").click()
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "Add to cart").click()
        time.sleep(1)
        assert driver.switch_to.alert.text == "Product added"
        driver.switch_to.alert.accept()