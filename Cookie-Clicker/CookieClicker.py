from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class CookieClicker:
	def __init__(self):
		self.logger = webdriver.Firefox()

	
	def click(self):
		logger = self.logger
		logger.get('https://orteil.dashnet.org/cookieclicker/')
		time.sleep(3)
		while(1):
			logger.find_element_by_id('bigCookie').click()
			logger.find_element_by_id('bigCookie').click()
			logger.find_element_by_id('bigCookie').click()
			logger.find_element_by_id('bigCookie').click()
			logger.find_element_by_id('bigCookie').click()
			logger.find_element_by_id('bigCookie').click()

cookie = CookieClicker()
cookie.click()