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
print( strA.upper() )
print( strA.count("p") )
print( strA.count("p",7) )
print( "MBC2580".isalnum() )
print( "MBC:2580".isalnum() )
print( "2580".isdecimal() )
print( "demo.ppt".endswith("ppt") )

#웹에서 또는 텍스트파일에서 문자열을 읽어오는 경우(전처리)
strB = "<<<  spam and ham  >>>"
print("---공백문자---")
print(strB)
#앞뒤에 불필요한 문자들을 나열해서 제거 
result = strB.strip("<> ")
print(result)
#치환
result2 = result.replace("spam", "spam egg")
print(result2)
print("---리스트로받기---")
lst = result2.split() 
print(lst)
print("---하나로 합치기---")
print(" ".join(lst))




