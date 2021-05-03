import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

s = requests.session()

PROXY = "185.198.188.51:8080"


# mail_url = 'https://www.google.com/'

mail_url = 'https://ucf.uscourts.gov/search?SelectedCourts=&CreditorSearch=&DebtorSearch=&CaseNumber=&Amount=40&EnteredOn=08%2F15%2F2020&page=4'

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

chrome_options = Options()
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options=chrome_options, executable_path=ChromeDriverManager().install())

driver.get(mail_url)

p = driver.current_window_handle

time.sleep(5)
