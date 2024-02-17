# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestLoginTest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(executable_path = "chromedriver-mac-arm64/chromedriver")
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_loginTest(self):
    self.driver.get("https://eprint.com.hr/demo/addauser.php")
    self.driver.set_window_size(1920, 971)
    self.driver.find_element(By.NAME, "username").click()
    self.driver.find_element(By.NAME, "username").send_keys("user0")
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys("asdfg")
    self.driver.find_element(By.NAME, "FormsButton2").click()
    self.driver.find_element(By.CSS_SELECTOR, "small > a:nth-child(1)").click()
    self.driver.find_element(By.NAME, "username").click()
    self.driver.find_element(By.NAME, "username").send_keys("user0")
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys("asdfg")
    self.driver.find_element(By.NAME, "FormsButton2").click()
  