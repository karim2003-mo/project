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
driver.get("https://www.instagram.com/accounts/emailsignup/")
driver.execute_script("window.open('');")