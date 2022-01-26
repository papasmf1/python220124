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
#변수를 추가
Person.title = "new title"
p1 = Person() 
p2 = Person()

print(Person.title)
print(p1.title)
print(p2.title)

#인스턴스에 추가
p1.age = 30 
print(p1.age)
print(p2.age)


