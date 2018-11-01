#Written By : Mohit vadhera
#Description: To fetch the current root passwords from PMM box

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import getpass
username='abhimanyu.thakur@oracle.com'
password1 = getpass.getpass("Please enter password:")
def ap_login():
	browser=webdriver.Firefox()
	browser.get('https://apditpbox.oracle.com/pmm/f?p=110:101')
	time.sleep(2)
	user=browser.find_element_by_css_selector('#P101_USERNAME')
	user.send_keys(username)
	password=browser.find_element_by_css_selector('#P101_PASSWORD')
	password.send_keys(password1)
	login=browser.find_element_by_css_selector('.t9C > a:nth-child(1)')
	login.click()
	time.sleep(5)
	for hosts1 in open('servers','r').readlines():
		hosts=hosts1.rstrip('\n')
		search_host=browser.find_element_by_css_selector('#P1_REPORT_SEARCH')
		search_host.clear()
		search_host.send_keys(hosts)
		get=browser.find_element_by_css_selector('.t9C > a:nth-child(1)')
		get.click()
		time.sleep(6)

		try:
			fetch_passwd=browser.find_element_by_xpath("//*[@class='R']//following::span[2]")
			print( hosts, fetch_passwd.text)			
			time.sleep(5)
			
		except Exception as e:
			print( hosts, "NO PASSWORD FOUND")
	
ap_login()
