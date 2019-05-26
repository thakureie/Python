'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
url = "https://pdit-tools.oracleoutsourcing.com/apex/f?p=110:3:15004997345439::NO:RP,3::"
driver = webdriver.Firefox()
#time.sleep(30)
driver.get(url)
time.sleep(30)
u = driver.find_element_by_tag_name('Username')
u.send_keys('abhimanyu.thakur@oracle.com')
p = driver.find_element_by_name('Password')
p.send_keys('Pawan1@jha')
p.send_keys(Keys.RETURN)
'''
'''
if i[1] == "id_text":
    inst = driver.find_element_by_id(i[2])
    #inst.click()
    for option in inst.find_elements_by_tag_name('option'):
        if option.text == i[3]:
            option.click()


'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
url = "https://pdit-tools.oracleoutsourcing.com/apex/f?p=110:3:15004997345439::NO:RP,3::"
driver = webdriver.Firefox()
driver.get(url)
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "Username")))
    EC.send_keys('abhimanyu.thakur@oracle.com')
finally:
    driver.quit()
