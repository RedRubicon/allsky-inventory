from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:5000')

assert 'AllSky Inventory' in browser.title