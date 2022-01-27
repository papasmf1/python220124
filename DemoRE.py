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


