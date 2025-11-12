import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestOrder:
    def test_place_order(self, driver):
        # ① 先加一件商品到购物车
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
        driver.switch_to.alert.accept()

        # ② 再去购物车下单
        driver.get("https://www.demoblaze.com/cart.html")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-success"))
        ).click()
        # 填写表单
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "name"))).send_keys("tester")
        driver.find_element(By.ID, "country").send_keys("China")
        driver.find_element(By.ID, "city").send_keys("Beijing")
        driver.find_element(By.ID, "card").send_keys("4111111111111111")
        driver.find_element(By.ID, "month").send_keys("12")
        driver.find_element(By.ID, "year").send_keys("2025")
        driver.find_element(By.XPATH, "//button[text()='Purchase']").click()
        # 等成功弹窗
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        assert "Thank you" in driver.switch_to.alert.text
        driver.switch_to.alert.accept()