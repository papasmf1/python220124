# DemoStr.py 
#print( dir(str) )

#반복적인 문구 생성
names = ["전우치","이순신","박문수"]
for name in names:
    print("안녕하세요 {0}님 설날입니다.~~".format(name))
    print("=" * 40)


#메서드 사용
strA = "python is very powerful"
print( len(strA) )
print( strA.capitalize() )
print( strA.count("p") )
print( strA.count("p",7) )

