from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

option = Options()
option.add_argument('--headless')

driver = webdriver.Chrome()
driver.get('https://www.google.co.jp/')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

ll = filter(lambda x: len(x) > 0, soup.text.split(' '))
for elem in ll:
    print(elem)
