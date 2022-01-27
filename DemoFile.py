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

