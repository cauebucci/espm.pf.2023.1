import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By

# Definir URL
url = 'https://www.nba.com/stats/players/traditional'
binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")

option = Options()
option.headless = True
driver = webdriver.Firefox(firefox_binary=binary, options=option, executable_path="C:\\geckodriver.exe")

driver.get(url)


element = driver.find_element(By.XPATH, "//*[@class='Crom_table__p1iZz']")

html_content = element.get_attribute("outerHTML")

soup = BeautifulSoup(html_content, 'lxml')
table = soup.find(name='table')

df_full = pd.read_html(str(table))
df_full[0].to_csv("nba_stats.csv", index=False)
print(df_full)