from selenium import webdriver

browser = webdriver.Chrome('/home/jeffrey/Documents/Tutorial/tddenv/chromedriver-Linux64')

browser.get('http://localhost:8000')

assert 'Django' in browser.title
