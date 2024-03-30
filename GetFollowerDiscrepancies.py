from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

username = 'eric.mxrtin'
password = 'love2Run'
count = 0

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
  total_follower_count = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "[href*=\"" + username + "/followers/\"]"))
  )
  print(total_follow_count.text + " total followers.")

  css_select_close = '[aria-label="Close"]'
  
  following_css =  "[href*=\"" + username + "/following/\"]"
  total_following_count = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "[href*=\"" + username + "/following/\"]"))
  )
  print(total_follow_count.text + " total followers.")

  click_button_with_css(driver, followers_css)
  followers_list = get_usernames_from_dialog(driver, total_follower_count)

  click_button_with_css(driver, css_select_close)
  time.sleep(1)

  click_button_with_css(driver, following_css)
  following_list = get_usernames_from_dialog(driver, total_following_count)

  no_followbacks = no_followback(followers, following)
  for i in no_followbacks:
    print(i)

def no_followback(followers, following):
  followers.sort()
  following.sort()
  no_followback_list = []
  for i in range(len(following)):
    try: 
      followers.index(following[i])
    except ValueError:
      no_followback_list += [following[i]]
  return no_followback_list

def get_usernames_from_dialog(driver):
  list_xpath = "//div[@role='dialog']//li"
  print("attempting EC xpath")

  time.sleep(3)
  # scroll_down(driver)

  class_name = "x1dm5mii"
  list_elems = driver.find_elements(By.CLASS_NAME, class_name)
  time.sleep(1)

  users = []
  for i in range(len(list_elems)):
    try:
      row_text = list_elems[i].text
      username = row_text[0:row_text.index("\n")]
      users += [username]
    except:
      print("continue")

  return users

def check_difference_in_count(driver):
  global count
  new_count = len(driver.find_elements(By.XPATH, "//div[@role='dialog']//li"))
  
  if count != new_count:
    count = new_count
    return True
  else: 
    return False

def scroll_down(driver):
  global count
  iter = 0
  # consider using the following number as end case!!
  while True:
    scroll_top_num = str(iter * 1000)
    iter +=1
    time.sleep(1)
    # scrolling script
    driver.execute_script("document.querySelector('div[role=dialog] ul').parentNode.scrollTop=" + scroll_top_num)
    try:
      WebDriverWait(driver, 1).until(check_difference_in_count)
    except:
      count = 0
      break
  return

__main__()