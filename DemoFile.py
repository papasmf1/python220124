# DemoFile.py 
for x in range(1,6):
    print(x,"*",x,"=",x*x)

print("---서식을 지정---")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).rjust(3))

print("---16진수,2진수출력---")
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))
print("{0:,}".format(15000))

#파일에 쓰기(유니코드로 읽기와쓰기) 
f = open("c:\\work\\demo.txt", "wt", encoding="utf-8")
f.write("첫줄\n두번째라인\n세번째\n")
f.close() 

#파일을 읽기
f = open("c:\\work\\demo.txt", "rt", encoding="utf-8")
result = f.read() 
f.close() 
print(result)
