# Fuction1.py 
#리턴값이 있는 경우
def swap(x,y):
    return y,x 

#호출
result = swap(3,4)
print(result[0])
print(result[1])

print("---불변형식---")
a = 1.2
print( id(a) )
a = 2.3 
print( id(a) )

print("---가변형식---")
lst = [1,2,3]
print( id(lst) )
lst.append(4)
print( id(lst) )

#참조를 복사해서 전달(Pass By Reference)
def change(x):
    #복사본으로 작업하면 된다.
    x1 = x[:]
    x1[0] = "H"
    print("함수내부:", x1)

#호출
wordlist = ["J","A","M"]
change(wordlist)
print("함수 호출후:", wordlist)


#전역변수와 지역변수 충돌 
#전역변수 초기화
x = 10 
y = 20 
def func1(a):
    #지역변수
    x = 1 
    return x+a 

#호출
print( func1(1) )

def func2(a):
    return x+a 

#호출
print( func2(1) )

#디버깅 연습을 위한 예제 
def intersect(prelist, postlist):
    #내부에 교집합 문자를 담을 지역변수(list)
    result = []
    #H(0) | A(1) | M(2)
    for x in prelist:
        #어떤 글자가 postlist에도 있고 그리고 result에 없으면 추가 
        if x in postlist and x not in result:
            result.append(x)
    return result 

#호출
print( intersect("HAM","SPAM") )


