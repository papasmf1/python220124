# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
#정규표현식 
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

#파일로 저장
f = open("c:\\work\\today.txt", "wt", encoding="utf-8")
#페이지가 0부터시작~~ 1부터시작~~ (한페이지가 30개 * 10페이지 = 300개)
for n in range(0,10):
        #클리앙의 중고장터 주소 
        data ='http://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        #문자열 데이터(실행결과)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우는 디코딩(해석)
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')

        # <td class="subject">
        #    <a href="/board/view.php">천주교 신부님 필력이 대단하시네요...</a>
        # 특정 조건이 있는 필터링: attributes(속성들)
        list = soup.find_all('td', attrs={'class':'subject'})
        for item in list:
                try:
                        item2 = item.find("a")
                        title = item2.text 
                        #print(title) 
                        if (re.search('대한민국', title)):
                                print(title.strip())
                                f.write(title.strip() + "\n")
                except:
                        pass
        

f.close()
print("웹 크롤링 종료~~")