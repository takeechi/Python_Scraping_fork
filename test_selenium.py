from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import chromedriver_binary
import time


option = Options()
option.add_argument('--headless')

driver = webdriver.Chrome(options=option)
driver.get('https://www.google.co.jp/')

# 検索フィールドの取得
query = driver.find_element(by=By.NAME, value='q')

# 検索文字列を入力
query.send_keys('フィレンツェ')

# 3秒待つ
time.sleep(3)

# 検索ボタンをクリック
button = driver.find_element(by=By.NAME, value='btnK')
button.click()

# 3秒待つ
time.sleep(3)

# 最初のリンクを取得
link_tags = driver.find_elements(by=By.TAG_NAME, value='a')
actions = ActionChains(driver)
actions.move_to_element(link_tags[8]).click().perform()

# 3秒待つ
time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text()
result_count = text.count('フィレンツェ')
print(f'フィレンツェの出現回数は{result_count}回です。')

# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')

# ll = [x for x in soup.text.split(' ') if len(x) > 0]
# for elem in ll:
#     print(elem)