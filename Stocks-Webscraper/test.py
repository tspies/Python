from time import sleep
from selenium import webdriver

def run_scrape(site = 'http://testing-ground.scraping.pro/'):
    driver = webdriver.Firefox(executable_path='/Users/tristyn/WebDriver/geckodriver')
    driver.get(site)
    stocks = driver.find_elements_by_xpath('//div[@class="caseblock"]')
    for stock in stocks:
        print(stock.text)
    driver.quit()
if __name__ == '__main__':
    # here we go
    run_scrape()