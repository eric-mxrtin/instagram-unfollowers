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
  # locate elements
  username_field = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.NAME, "username"))
  )
  password_field = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.NAME, "password"))
  )

  # enter credentials
  username_field.send_keys(username)
  password_field.send_keys(password)
  password_field.send_keys(Keys.ENTER)

def click_button_with_css(driver, css_selector):
  element = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
  )
  element.click()

def __main__():
  # configure web driver
  driver = webdriver.Chrome()
  driver.get('https://www.instagram.com/accounts/login/')

  # log into instagram
  time.sleep(1)
  login(driver)

  # navigate to profile
  profile_css = "[href*=\"" + username + "\"]"
  click_button_with_css(driver, profile_css)

  # navigate to followers
  followers_css =  "[href*=\"" + username + "/followers/\"]"
  total_follower_count = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "[href*=\"" + username + "/followers/\"]"))
  )
  print(total_follower_count.text + " total followers.")
  click_button_with_css(driver, followers_css)
  time.sleep(3)
  # dialog_box = WebDriverWait(driver, 5).until(
  #   EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div'))
  # )
  dialog_box = driver.find_element(By.XPATH, "//div[@class='_aano']")
  driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", dialog_box)

  # Wait for some time to let the new content load (you may adjust the time accordingly)
  driver.implicitly_wait(10)
  # followers_list = get_usernames_from_dialog(driver, total_follower_count)


  # # navigate to following
  # css_select_close = WebDriverWait(driver, 10).until(
  #   EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Close"]'))
  # )
  # click_button_with_css(driver, css_select_close)

  # following_css =  WebDriverWait(driver, 10).until(
  #   EC.element_to_be_clickable((By.CSS_SELECTOR, "[href*=\"" + username + "/following/\"]"))
  # )
  # total_following_count = following_css.text
  # print(total_following_count + " total following.")
  # click_button_with_css(driver, following_css)
  # following_list = get_usernames_from_dialog(driver, total_following_count)

  # time.sleep(1)

  # no_followbacks = no_followback(followers_list, following_list)
  # for i in no_followbacks:
  #   print(i)

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
  scroll_within_dialog_until_no_more_elements(driver)

def check_difference_in_count(driver):
  global count
  new_count = len(driver.find_elements(By.XPATH, "//div[@role='dialog']//li"))
  
  if count != new_count:
    count = new_count
    return True
  else: 
    return False

def scroll_within_dialog_until_no_more_elements(driver):
    dialog_element = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[role='dialog']")))
    previous_height = driver.execute_script("return arguments[0].scrollHeight;", dialog_element)
    while True:
        # Scroll down within the dialog box
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", dialog_element)
        # Wait for a short period to load more content (adjust as needed)
        driver.implicitly_wait(5)
        # Calculate new scroll height
        new_height = driver.execute_script("return arguments[0].scrollHeight;", dialog_element)
        # Check if scroll height has not changed (no more content to load)
        if new_height == previous_height:
            print("breaking")
            break
        previous_height = new_height

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