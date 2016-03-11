from selenium import webdriver

profile = webdriver.FirefoxProfile()
browser = webdriver.Firefox(profile)
# browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title