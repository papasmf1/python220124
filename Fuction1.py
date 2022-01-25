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
    x[0] = "H"

#호출
wordlist = ["J","A","M"]
change(wordlist)
print("함수 호출후:", wordlist)



