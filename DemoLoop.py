# DemoLoop.py 

value = 5 
while value > 0:
    print(value)
    value -= 1 

print("---while루프 종료---")

lst = ["apple", 100, 3.14]
for item in lst:
    print(item, type(item))

#구구단 출력: 미리 약속된 기호 {0} {1} 미리 출력할 위치를 지정 
#입력 파라메터로 문자열을 출력
#outer 반복 구문 
#디버깅할 때 멈춰~~(중단점)
for x in [2,3,4,5,6]:
    print("---{0}단---".format(x))
    #inner 반복 구문
    for y in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(x,y,x*y))

#루프를 탈출(break): 프리즌 브레이크 
lst = [1,2,3,4,5,6,7,8,9,10]
for item in lst:
    if item > 5:
        break
    print("Item:{0}".format(item))

print("---for in루프 종료---")

#루프를 지속하는 경우 continue
for item in lst:
    if item % 2 == 0:
        continue
    print("Item:{0}".format(item))

print("---for in루프 종료---")