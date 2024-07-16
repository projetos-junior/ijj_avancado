from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
import time


browser = Firefox()

link = 'https://google.com.br'

browser.get(link)

time.sleep(3)

# def seatch_google()