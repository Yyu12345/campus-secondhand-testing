import pytest, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="class")
def driver():
    drv = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    drv.maximize_window()
    yield drv
    drv.quit()

class TestAuth:
    def test_register_and_login(self, driver):
        driver.get("https://www.demoblaze.com")
        driver.find_element(By.ID, "signin2").click()
        time.sleep(1)
        user = f"test{int(time.time())}"  # 唯一账号
        driver.find_element(By.ID, "sign-username").send_keys(user)
        driver.find_element(By.ID, "sign-password").send_keys("123456")
        driver.find_element(By.XPATH, "//button[text()='Sign up']").click()
        time.sleep(1)
        # 自动处理弹窗
        assert driver.switch_to.alert.text == "Sign up successful."
        driver.switch_to.alert.accept()

        # 立即登录
        driver.find_element(By.ID, "login2").click()
        time.sleep(1)
        driver.find_element(By.ID, "loginusername").send_keys(user)
        driver.find_element(By.ID, "loginpassword").send_keys("123456")
        driver.find_element(By.XPATH, "//button[text()='Log in']").click()
        time.sleep(2)
        assert driver.find_element(By.ID, "nameofuser").text == f"Welcome {user}"