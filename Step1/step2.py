from selenium import webdriver
import idpw
# import time
path = "C:/Utils/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.implicitly_wait(3)    #3초 기다림

# 1. 구글검색
# driver.get('https://www.google.com')
# search_box=driver.find_element_by_name('q')
# search_box.send_keys('처음코딩')
# search_box.submit()

# 2. 네이버로그인
driver.get('https://nid.naver.com/nidlogin.login')
id = 'eventia'
pw = 'lnv17A1801sk#'
driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
# time.sleep(1)
driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
# time.sleep(1)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

# 아래코드는 현재 작동되지 않음
# driver.find_element_by_name('id').send_keys('eventia')
# driver.find_element_by_name('pw').send_keys('lnv17A1801sk#')
