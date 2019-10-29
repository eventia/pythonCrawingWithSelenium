from selenium import webdriver

path = "C:/Utils/chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get('https://www.google.com')
search_box=driver.find_element_by_name('q')
search_box.send_keys('처음코딩')
search_box.submit()
