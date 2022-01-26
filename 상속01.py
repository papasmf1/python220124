#부모 클래스 정의 
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))

#자식 클래스 정의
class Student(Person):
    #학생이면 학과와 학번이 추가 
    def __init__(self, name, phoneNumber, subject, studentID):
        #명시적으로 부모의 초기화 메서드 호출(부모는 base, super키워드 )
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #상속받은 메서드를 덮어쓰기(내가 원하는 로직으로 재정의, override)
    #상속받아서 코드를 덮어쓰기(다형적인 메서드)
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))
        print("Info(학과:{0}, 학번: {1})".format(
            self.subject, self.studentID))


#인스턴스 생성
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "151122")
#다중 라인 주석처리: ctrl + / 
# print( p.__dict__ )
# print( s.__dict__ )
p.printInfo()
s.printInfo()

