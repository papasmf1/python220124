# DemoCopy.py 
# 주석을 추가
# 독서 ==> 필사 ==> 블로그에 올리기 ==> 피드백받기 
# 프랭클린 플래서(3P Binder) 한근태작가님(일생에 한번 고수를 만나라~~ )

#얕은복사(기본)
a = [1,2,3]
b = a 
a[0] = 38 
print(a)
print(b)
print(id(a), id(b))

#깊은 복사는 필요한 경우에 코딩
print("---깊은 복사---")
a = [10,20,30]
b = a[:] 
a[0] = 38 
print(a)
print(b)
print(id(a), id(b))

#리스트가 아닌 경우는 copy모듈 사용
print("---copy모듈 사용---")
import copy 
a = [100,200,300]
b = copy.deepcopy(a)
a[0] = 101
print(a)
print(b)
print(id(a),id(b))