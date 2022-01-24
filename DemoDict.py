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

