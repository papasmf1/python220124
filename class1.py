# class1.py 
#1)클래스를 정의 
class Person:
    #초기화 메서드(가장 먼저 실행)
    def __init__(self):
        self.name = "default name"
    #인스턴스 메서드
    def print(self):
        print("My name is ", self.name)

#2)인스턴스를  생성 
p1 = Person() 

#3)메서드 호출 
p1.print() 

