import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import HtmlTestRunner

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        ser = Service("C:\\drivers\\chromedriver_win32 (3)\\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=ser)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(15)
    def test_dropdown(self):
        self.driver.get("https://webdriveruniversity.com/Actions/index.html")
        self.driver.maximize_window()
        source_element = self.driver.find_element(By.XPATH,'//*[@id="draggable"]/p/b')
        target_element = self.driver.find_element(By.XPATH,'//*[@id="droppable"]')
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element,target_element).perform()
    def test_doubleclick(self):
        self.driver.get("https://webdriveruniversity.com/Actions/index.html")
        self.driver.maximize_window()
        double_click = self.driver.find_element(By.XPATH,'//*[@id="double-click"]/h2')
        actions = ActionChains(self.driver)
        actions.double_click(double_click).perform()
    def test_clickandhold(self):
        self.driver.get("https://webdriveruniversity.com/Actions/index.html")
        self.driver.maximize_window()
        click_hold = self.driver.find_element(By.XPATH, '//*[@id="click-box"]')
        actions = ActionChains(self.driver)
        actions.click_and_hold(click_hold).perform()

    def test_hover(self):
        self.driver.get("https://webdriveruniversity.com/Actions/index.html")
        hover1 = self.driver.find_element(By.XPATH,'//*[@id="div-hover"]/div[1]/button')
        hover2 = self.driver.find_element(By.XPATH,'//*[@id="div-hover"]/div[1]/div/a')
        actions = ActionChains(self.driver)
        actions.move_to_element(hover1).move_to_element(hover2).click().perform()

# second_hover1 = driver.find_element(By.XPATH,'//*[@id="div-hover"]/div[2]/button')
# second_hover2 = driver.find_element(By.XPATH,'//*[@id="div-hover"]/div[2]/div/a')
# actions = ActionChains(driver)
# actions.move_to_element(second_hover1).move_to_element(second_hover2).click().perform()
# third_hover1 = driver.find_element(By.XPATH,'//*[@id="div-hover"]/div[3]/button')
# third_hover2 = driver.find_element(By.XPATH,'//*[@id="div-hover"]/div[3]/div/a')
# actions = ActionChains(driver)
# actions.move_to_element(third_hover1).move_to_element(third_hover2).click().perform()
    @classmethod
    def tearDownClass(cls):
        print(cls.driver.title)
        print(cls.driver.current_url)
        cls.driver.quit()
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/manoh/PycharmProjects/pythonProject1/reports"))