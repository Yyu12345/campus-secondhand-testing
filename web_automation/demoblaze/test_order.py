import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestOrder:
    def test_place_order(self, driver):
        # ① UI 加购物车
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

        # ② 获取浏览器 cookies 里的 token
        cookies = {c['name']: c['value'] for c in driver.get_cookies()}
        # ③ 直接调下单接口
        url = "https://www.demoblaze.com/cart/doPurchase.json"
        payload = {
            "name": "tester",
            "country": "China",
            "city": "Beijing",
            "card": "4111111111111111",
            "month": "12",
            "year": "2025"
        }
        resp = requests.post(url, data=payload, cookies=cookies)
        assert resp.status_code == 200
        assert "Thank you" in resp.text