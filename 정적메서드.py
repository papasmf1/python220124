# 정적메서드.py
#클래스에 소속되어서 직접 클래스에서 호출
class MyCalc(object):
    #데코레이터를 추가
    @staticmethod
    def my_add(x,y):
        return x+y

#클래스에서 직접 호출한다.
a = MyCalc.my_add(5,7)
print(a)

