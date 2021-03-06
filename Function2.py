# Function2.py 
#불변형식을 함수 내부에서 쓰기
g = 1 

def testScope(a):
    #global g 
    g = 2 
    return g+a 

#호출
testScope(1)
print("전역변수 g:", g)

#기본값을 셋팅
def times(a=10,b=20):
    return a*b 

#호출
print(times())
print(times(5))
print(times(5,6))

#키워드 인자(파라메터명을 기술)
def connectURI(server, port):
    strURL = "http://" + server + ":" + port 
    return strURL

#호출
print(connectURI("credu.com","80"))
print(connectURI(port="80",server="naver.com"))

#가변인자 
def union(*ar): 
    #지역변수
    result = []
    #단어를 자르기 
    for item in ar:
        #글자를 자르기 
        for x in item:
            #없으면 추가 
            if x not in result:
                result.append(x)
    return result 

#호출
print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))

#정의되지 않은 인자:필수, 옵션 
def userURIBuilder(server, port, **user):
    strURL = "http://" + server + ":" + port + "/?"
    #user는 딕셔너리 
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL

#호출
print(userURIBuilder("credu.com","80",id="kim"))
print(userURIBuilder("credu.com","80",id="kim",name="mike"))

#람다함수(간결하게 함수를 정의하는 문법)
g = lambda x,y:x*y 
print(g(3,4))
print(g(5,6))

print( (lambda x:x*x)(3) )

print( globals() )


