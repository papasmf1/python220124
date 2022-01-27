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

#블럭으로 주석 처리: ctrl + / 
# #파일에 쓰기(유니코드로 읽기와쓰기) 
# f = open("c:\\work\\demo.txt", "wt", encoding="utf-8")
# f.write("첫줄\n두번째라인\n세번째\n")
# f.close() 

# #파일을 읽기
# f = open("c:\\work\\demo.txt", "rt", encoding="utf-8")
# #str변수로 한번에 읽기 
# print( f.read() ) 
# print( f.tell() )
# #리셋(처음으로 돌아가~~)
# f.seek(0)
# print("---readlines()---")
# print( f.readlines() )
# f.seek(0)
# print("---readline()---")
# print( f.readline(), end="" )
# print( f.readline(), end="" )

#기존 파일에 첨부하는 경우
f = open("c:\\work\\demo.txt", "a+", encoding="utf-8")
f.write("새로운 데이터\n")

f.close() 



