import requests
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestOrder:
    def test_place_order(self, driver):
        # ① UI 加购物车（已有）
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

        # ② 组装下单数据
        cookies = {c['name']: c['value'] for c in driver.get_cookies()}
        payload = {
            "name": "tester",
            "country": "China",
            "city": "Beijing",
            "card": "4111111111111111",
            "month": "12",
            "year": "2025"
        }

        # ③ 调真实接口
        resp = requests.post(
            "https://api.demoblaze.com/placeOrder",
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload),
            cookies=cookies
        )

        # ④ 断言
        assert resp.status_code == 200
        assert "Thank you" in resp.text