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
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result 

#호출
print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))