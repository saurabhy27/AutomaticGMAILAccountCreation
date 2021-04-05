from selenium.webdriver import Chrome
from selenium import webdriver
import time
import re

url = "http://google.com/intl/en-GB/gmail/about/"
first_name = "Saurabh"
last_name = "Singh"
email = "tmptestayraaai1"
password = "----"
phone_number = "xxxxxxxxxx"

# Setting the properties for the selenium driver
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\isaur\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument('--profile-directory=Profile 1')
driver = Chrome(executable_path="src/chromedriver.exe", options=options)
driver.implicitly_wait(30)
driver.maximize_window()
# Opening the Url
driver.get(url)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[4]/ul[1]/li[3]/a').click()
driver.switch_to.window(driver.window_handles[-1])

# Inserting data and process at next step
driver.find_element_by_xpath('//*[@id="firstName"]').send_keys(first_name)
driver.find_element_by_id('lastName').send_keys(last_name)
driver.find_element_by_id("username").send_keys(email)
driver.find_element_by_xpath('//*[@id="passwd"]/div[1]/div/div[1]/input').send_keys(password)
driver.find_element_by_xpath('//*[@id="confirm-passwd"]/div[1]/div/div[1]/input').send_keys(password)
driver.find_element_by_xpath('//*[@id="accountDetailsNext"]/div/button/div[2]').click()

driver.find_element_by_id('phoneNumberId').send_keys(phone_number)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()

# Opening the new browser for OTP verification
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[-1])

# Wait 15 sec for OTP
time.sleep(15)

# Open recent msg and extract otp
driver.get("https://messages.google.com/web/conversations")
time.sleep(5)
driver.find_element_by_xpath('/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-main-nav/mws-conversations-list/nav/div[1]/mws-conversation-list-item[1]/a').click()
time.sleep(5)
otpmsg = driver.find_element_by_xpath('/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-conversation-container/div[1]/div/mws-messages-list/mws-bottom-anchored/div/div/div/mws-message-wrapper/div/div/div/mws-message-part-router/mws-text-message-part/div/div/mws-message-part-content/div/div').text
print(otpmsg)
otp = re.findall(r'\d+', otpmsg)[0]

# back to previous tab
driver.switch_to.window(driver.window_handles[-2])

# Enter OTP and Continue
time.sleep(3)
driver.find_element_by_xpath('//*[@id="code"]').send_keys(otp)
driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/button').click()

# Fill DOB Details and Proceed
driver.find_element_by_xpath('//*[@id="day"]').send_keys('01')
driver.find_element_by_xpath('//*[@id="month"]/option[text()="January"]').click()
driver.find_element_by_xpath('//*[@id="year"]').send_keys('2000')
driver.find_element_by_xpath('//*[@id="gender"]/option[text()="Male"]').click()
driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()

time.sleep(3)
driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/button').click()
driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
time.sleep(60)
driver.quit()