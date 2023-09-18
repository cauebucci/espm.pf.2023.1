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
option.headless = False
driver = webdriver.Firefox(firefox_binary= binary, options=option, executable_path="C:\\geckodriver.exe")

driver.get(url)

teste = driver.find_element(By.XPATH, "//div[@class='Crom_container__C45Ti crom-container']//table//thead//tr//th[@field='PTS']")

print(teste)