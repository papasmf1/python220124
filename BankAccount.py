# BankAccount.py
#파이썬은 은폐성이 약하다(이름 변경으로 커버~~ )
#은행의 계정을 표현한 클래스 
class BankAccount(object):
    #초기화 메서드는 인스턴스 멤버변수 초기화 루틴(생성자) 
    def __init__(self, id, name, balance):
        #이름을 숨겨달라(이름변경)
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    #입금
    def deposit(self, amount):
        self.__balance += amount 
    #출금
    def withdraw(self, amount):
        self.__balance -= amount
    #문자열 결과를 리턴
    def __str__(self):
        return "{0}, {1}, {2}".format(self.__id, 
        self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
print(account1)
#print(account1.__balance)
#외부에서 혹시 접근할 필요가 있다면(백도어)
print(account1._BankAccount__balance)






