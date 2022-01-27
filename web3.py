# web2.py 
#웹서버에 요청
import urllib.request
#크롤링
from bs4 import BeautifulSoup

#파일로 저장(첨부연산): wt, a+ 
f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")
#페이징처리를 위해 동적으로 번호 만들기(수열함수)
for i in range(1,6): 
    url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
    print( url )
    data = urllib.request.urlopen(url)
    soup = BeautifulSoup(data, "html.parser")
    #필요한 태그만 검색: <td class="title"> 10개를 가져오기 
    cartoons = soup.find_all("td", class_="title")
    for item in cartoons:
        title = item.find("a").text.strip()
        print(title)
        f.write(title + "\n")

print("웹툰 크롤링 종료")
f.close() 



