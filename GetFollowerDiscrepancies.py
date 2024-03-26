from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
username = ''
password = ''

def __main__():
  driver = webdriver.Chrome(ChromeDriverManager().install())
  time.sleep(10)

__main__()