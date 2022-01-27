# DemoRE.py 
import re 

#print(dir(re))
#특정한 규칙(패턴)을 검색 
result = re.search("[0-9]*th", "35th")
#매칭오브젝트
print(result)
result2 = re.match("[0-9]*th", "35th")
print(result2)
print(result2.group())

print("---함정추가---")
print(bool(re.search("[0-9]*th", "  35th")))
print(bool(re.match("[0-9]*th", "  35th")))

#주로 검색은 search()함수 사용
if bool(re.search("apple", "this is apple")):
    print("apple을 찾았어~~")
else:
    print("없음") 


if bool(re.match("apple", "this is apple")):
    print("apple을 찾았어~~")
else:
    print("없음") 

#년도를 검색
if bool(re.search("\d{4}", "올해는 2022년입니다.")):
    print("년도 패턴을 찾았어~~")
else:
    print("없음") 

if bool(re.match("\d{4}", "올해는 2022년입니다.")):
    print("년도 패턴을 찾았어~~")
else:
    print("없음") 