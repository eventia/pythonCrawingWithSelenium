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

# youtube 의 playlist 를 아래에 넣으면, 플레이리스트안에 있는 모든 영상파일의 링크와 제목을 가져온다.
playlist = 'PLsS-TVNjbU7cdhwa-s-X7CTOIiP761yVP'

# PC 에 selenium 의 웹드라이브(크롬브라우저사용)를 다운받아 둘것
# 아래의 위치에 chromedriver.exe 파일을 압축해제하여 둠
path = "C:/Utils/chromedriver.exe"

driver = webdriver.Chrome(path)
# driver.implicitly_wait(1)    #1초 기다림

# 유튜브 플레이리스트
driver.get('https://www.youtube.com/playlist?list='+playlist)

# 화면상 모든 소스를 html 에 저장
html = driver.page_source

# BeautifulSoup 을 사용하여 html 을 파싱함
soup = BeautifulSoup(html, 'html.parser')

# 전제 페이지 중 a 태그의 class 가 'yt-simple-endpoint style-scope ytd-playlist-video-renderer' 인 것을 선택
# 이곳이 리스트의 링크와 제목이 담긴 곳
all_title = soup.find_all('a', {'class':'yt-simple-endpoint style-scope ytd-playlist-video-renderer'})

# 리스트 안의 영상의 갯수만큼 링크와 타이틀을 가져옴
# 타이틀은 내부에서 "title" 태그를 사용하지 않아 편법으로 get_text() 를 이용해 순수한 텍스트만 골라낸 후
# 앞에서 30번째 부터 시작해서 30개의 문자를 가져온 후 뒤편의 공백(\n포함)을 제거함
for link in all_title:
    tmp = link.get('href')
    ttle = link.get_text()[30:60].strip()
    print('https://youtu.be/'+tmp[9:20], ttle)

# 웹드라이브 종료
driver.close()
