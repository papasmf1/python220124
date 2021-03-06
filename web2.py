# web2.py 
#웹서버에 요청
import urllib.request
#크롤링
from bs4 import BeautifulSoup

#패키지명.모듈명.함수명()
data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")

#전체문서에서 검색 
# <td class="title">
#     <a href="/webtoon/detail?titleId">마음의 소리 50화 <격렬한 나의 하루> </a>
# </td>
soup = BeautifulSoup(data, "html.parser")
#필요한 태그만 검색: <td class="title"> 10개를 가져오기 
cartoons = soup.find_all("td", class_="title")
#1개만 검색 
print("갯수:{0}".format( len(cartoons)) )
#슬라이싱을 해서 첫번째만 가져오기 
title = cartoons[0].find("a").text 
link = cartoons[0].find("a")["href"]
print(title)
print(link)

#파일로 저장(첨부연산): wt, a+ 
f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")
for item in cartoons:
    title = item.find("a").text.strip()
    print(title)
    f.write(title + "\n")

print("웹툰 크롤링 종료")
f.close() 



