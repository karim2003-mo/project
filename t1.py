from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})
chrome_service=Service()
driver = webdriver.Chrome(options=chrome_options,service=chrome_service)
actions = ActionChains(driver)
# driver.get("https://www.instagram.com/")
# element_usernaem= driver.find_element(By.NAME, "username")
# element_usernaem.send_keys("karimgamal62")
# element_password= driver.find_element(By.NAME, "password")
# element_password.send_keys("karim012064258")
# button=driver.find_element(By.XPATH,"//button[@class=' _acan _acap _acas _aj1- _ap30']")
# button.click()
# time.sleep(200)
driver.get("https://www.facebook.com/")
element_usernaem= driver.find_element(By.NAME, "email")
element_usernaem.send_keys("196b8a81ec@emailfoxi.pro")
element_password= driver.find_element(By.NAME, "pass")
element_password.send_keys("abbas12345#")
button=driver.find_element(By.XPATH,"//button[@class='_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy']")
button.click()
time.sleep(10)
driver.get("https://www.facebook.com/photo?fbid=122244262328007065&set=a.122098928570007065")
# time.sleep(5)
# pyautogui.click(clicks=1,x=100,y=300)
# time.sleep(5)
time.sleep(2)
comment=driver.find_element(By.XPATH,"//div[@aria-label='اكتب تعليقًا...' and @contenteditable='true']")
comment.send_keys("angry")
# time.sleep(5)
comment_click=driver.find_element(By.XPATH,"//div[@role='button' and @aria-label='تعليق']")
# comment_click.click()
time.sleep(2)
reaction_buttons = driver.find_element(By.XPATH, "//div[@aria-label='أعجبني' and @role='button']")
actions.move_to_element(reaction_buttons).perform()
time.sleep(2)
print(reaction_buttons)
time.sleep(2)
love_buttons = driver.find_element(By.XPATH, "//div[@aria-label='أحببته' and @role='button']")
love_buttons.click()
time.sleep(250)
# b=driver.find_element(By.XPATH,"//p[@class='xdj266r x11i5rnm xat24cr x1mh8g0r']")
# b.send_keys("legend")
# 6wmuwLmiQv8QMB_
# "//div[@aria-label='أعجبني' and @role='button']"
