from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class GoogleLogger:
	def __init__(self, email, password):
		self.email = email
		self.password = password
		self.logger = webdriver.Firefox()
	
	def login(self):
		logger = self.logger
		logger.get('https://www.google.com/gmail/')
		time.sleep(3)
		email = logger.find_element_by_name('identifier')
		email.send_keys(self.email)
		email.send_keys(Keys.RETURN)
		time.sleep(2)
		password = logger.find_element_by_name('password')
		password.send_keys(self.password)
		password.send_keys(Keys.RETURN)
		time.sleep(15)
		logger.quit()

bot = GoogleLogger('**********@gmail.com', '**********')
bot.login()