# /e/StudentFiles/Quarter05/USD-T/Python/BookWork

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title