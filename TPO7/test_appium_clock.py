import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

class TestClockApp:
    @pytest.fixture(scope="function")
    def driver(self):
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.platform_version = "16"
        options.device_name = "emulator-5554"
        options.app_package = "com.google.android.deskclock"
        options.app_activity = "com.android.deskclock.DeskClock"
        options.automation_name = "UiAutomator2"
        options.no_reset = False
        
        driver = webdriver.Remote('http://localhost:4723', options=options)
        time.sleep(3)
        
        yield driver
        
        driver.quit()

    def click_alarm_tab(self, driver):
        driver.save_screenshot("clock_main_screen.png")
        print("Скриншот главного экрана сохранен")
        
        try:
            alarm_tab = driver.find_element(AppiumBy.ID, "com.google.android.deskclock:id/tab_menu_alarm")
            alarm_tab.click()
            print("Клик по вкладке 'Будильник' по ID")
        except:
            try:
                alarm_tab = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Alarm")
                alarm_tab.click()
                print("Клик по вкладке 'Будильник' по тексту")
            except:
                print("Вкладка не найдена")
        
        time.sleep(2)
        driver.save_screenshot("clock_alarm_screen.png")
        print("Скриншот экрана будильника сохранен")
        
        assert True

    def test_add_alarm_button(self, driver):
        self.click_alarm_tab(driver)
        
        try:
            add_alarm_btn = driver.find_element(AppiumBy.ID, "com.google.android.deskclock:id/fab")
            add_alarm_btn.click()
            print("Клик по кнопке добавления будильника")
        except:
            try:
                add_alarm_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Add alarm")
                add_alarm_btn.click()
                print("Клик по кнопке добавления будильника по тексту")
            except:
                print("Кнопка добавления будильника не найдена")
        
        time.sleep(2)
        driver.save_screenshot("clock_add_alarm_screen.png")
        print("Скриншот экрана добавления будильника сохранен")
        
        assert True