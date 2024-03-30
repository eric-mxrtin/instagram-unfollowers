from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

username = 'eric.mxrtin'
password = 'love2Run'

def login(driver):
  # replace with web driver wait
  driver.find_element(By.NAME, "username").send_keys(username)
  driver.find_element(By.NAME, "password").send_keys(password)
  driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)

def click_button_with_css(driver, css_selector):
  element = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
  )
  element.click()

def navigate_to_followers(driver):
  profile_css = "[href*=\"" + username + "\"]"
  click_button_with_css(driver, profile_css)

def __main__():
  driver = webdriver.Chrome()
  driver.get('https://www.instagram.com/accounts/login/')
  time.sleep(1)
  login(driver)
  navigate_to_followers(driver)

  followers_css = "[href*=\"" + username + "/followers/\"]"
  css_select_close = '[aria-label="Close"]'
  following_css =  "[href*=\"" + username + "/following/\"]"

  click_button_with_css(driver, followers_css)
  print("followers button pressed")
  followers_list = get_usernames_from_dialog(driver)

  click_button_with_css(driver, css_select_close)

  click_button_with_css(driver, following_css)
  following_list = get_usernames_from_dialog(driver)

  time.sleep(20)



def get_usernames_from_dialog(driver):
  list_xpath = "//div[@role='dialog']//li"
  WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, list_xpath))
  )

  scroll_down()

  list_elems = driver.find_elements(By.XPATH, list_xpath)
  time.sleep(10000)

  return

__main__()