from selenium.webdriver.common.by import By

URL = "https://practicetestautomation.com/practice-test-login/"

def test_positive_login(driver):
    driver.get(URL)
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    assert "logged-in-successfully" in driver.current_url
    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert "Congratulations" in body_text or "successfully logged in" in body_text
    logout_btn = driver.find_element(By.XPATH, "//a[text()='Log out']")
    assert logout_btn.is_displayed()

def test_negative_username(driver):
    driver.get(URL)
    driver.find_element(By.ID, "username").send_keys("incorrectUser")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    error = driver.find_element(By.ID, "error")
    assert error.is_displayed()
    assert error.text.strip() == "Your username is invalid!"

def test_negative_password(driver):
    driver.get(URL)
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("incorrectPassword")
    driver.find_element(By.ID, "submit").click()

    error = driver.find_element(By.ID, "error")
    assert error.is_displayed()
    assert error.text.strip() == "Your password is invalid!"
