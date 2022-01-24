
# DemoDict.py 
#사전식 변수
color = {"apple":"red", "banana":"yellow"}

print( color )
print( type(color) )
for item in color.items():
    print(item)

#특정 키를 검색
print( color["apple"] )
#입력
color["cherry"] = "red"
for item in color.items():
    print(item)

#삭제
del color["apple"]
for item in color.items():
    print(item)

#전화번호를 관리
phone = {"kim":"1111", "lee":"2222", "park":"3333"}
print(len(phone))
print(phone["park"])
print("kim" in phone)
print("moon" not in phone)

#참조를 복사해서 전달
p = phone 
p["kang"] = "1234"
print(p)
print(phone)
#id()함수는 랜덤한 숫자값인데 주소처럼 사용 
print( id(phone), id(p) )




