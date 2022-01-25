# class1.py 
#1)클래스를 정의 
class Person:
    #데이터를 공유하는 용도로 클래스 멤버 변수를 초기화
    num_person = 0 
    #초기화 메서드(가장 먼저 실행)
    def __init__(self):
        self.name = "default name"
        Person.num_person += 1 
    #인스턴스 메서드
    def print(self):
        print("My name is ", self.name)

#2)인스턴스를  생성 
p1 = Person() 
p2 = Person()
p3 = Person() 

print("인스턴스 갯수:",  Person.num_person)


