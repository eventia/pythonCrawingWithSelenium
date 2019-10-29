# 유튜브 리스트를 주소와 제목만 가져오기
# selenium 과 beautifulSoup 를 사용하여 처리
# 제작기간 : 4시간 / 처음으로 selenium 과 beautifulSoup 사용
# 부족한 부분이나 개선할 부분이 있으면 알려주기 바람
# 유튜브 영상을 다른 곳에 올리기 위한 작업중 기존 리스트의 내용을 하나씩 담는 것이 부담스러워 제작함
# 사용법 : 소스를 적당히 알아서 사용하면 됨
# 도스창에서
# C:\>python step3.py >> youtubeList.txt
# 이와 같이하면 파일로 저장됨

from selenium import webdriver
from bs4 import BeautifulSoup
import time

playlist = 'PLsS-TVNjbU7cdhwa-s-X7CTOIiP761yVP'

path = "C:/Utils/chromedriver.exe"
driver = webdriver.Chrome(path)
# driver.implicitly_wait(1)    #1초 기다림

driver.get('https://www.youtube.com/playlist?list='+playlist)

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
all_title = soup.find_all('a', {'class':'yt-simple-endpoint style-scope ytd-playlist-video-renderer'})
for link in all_title:
    tmp = link.get('href')
    ttle = link.get_text()[30:60].strip()
    print('https://youtu.be/'+tmp[9:20], ttle)

driver.close()
