# web1.py 
#웹크롤링을 위한 선언
#from 패키지명 import 모듈명 
from bs4 import BeautifulSoup

#파일을 로딩(Read Text)
#메서드를 연속으로 호출: 메서드 체인
#read()는 처음부터 끝까지 읽엇 str리턴 
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read() 
#검색을 위한 객체 생성(html문서, xml문서)
soup = BeautifulSoup(page, "html.parser")
#전체 문서 보기
#print( soup.prettify() )

#문서의 <p>태그 몽땅~~ 
#print( soup.find_all("p") )
#첫번째 <p>태그 
#print( soup.find("p") )

#조건이 있는 태그(필터링)
#<p class='outer-text'>컨텐츠</p>
#print( soup.find_all("p", class_="outer-text") )

#태그 내부에 컨텐츠만 가져오기
for item in soup.find_all("p"):
    #<p>문자열</p> ==> .text 속성
    #가공 
    title = item.text.strip()
    title = title.replace("\n", "")
    title = title.replace("\t", "")
    print(title)


