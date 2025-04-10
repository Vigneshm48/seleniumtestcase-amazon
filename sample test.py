!pip install selenium

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class AmazonHomePageTests(unittest.TestCase):

  def setupclass(cls):
    cls.driver= webdriver.chrome()
    cls.driver.maximize_window()
    cls.driver.get("https://www.amazon.in/")
    time.sleep(3)
