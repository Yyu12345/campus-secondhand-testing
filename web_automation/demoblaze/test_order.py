import time

class TestOrder:
    def test_place_order(self, driver):
        driver.get("https://www.demoblaze.com/cart.html")
        driver.find_element(By.CLASS_NAME, "btn-success").click()
        time.sleep(1)
        driver.find_element(By.ID, "name").send_keys("tester")
        driver.find_element(By.ID, "country").send_keys("China")
        driver.find_element(By.ID, "city").send_keys("Beijing")
        driver.find_element(By.ID, "card").send_keys("4111111111111111")
        driver.find_element(By.ID, "month").send_keys("12")
        driver.find_element(By.ID, "year").send_keys("2025")
        driver.find_element(By.XPATH, "//button[text()='Purchase']").click()
        time.sleep(2)
        assert "Thank you" in driver.find_element(By.TAG_NAME, "h2").text