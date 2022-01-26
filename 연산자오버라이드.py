#연산자 오버라이드(연산자를 내가 원하는 로직으로 변경) 
class NumBox:
	def __init__(self, num):
		self.Num = num
	#일반 메서드로 구현 
	def add(self, num):
		self.Num += num
	#일반 메서드로 구현 
	def remove(self, num):
		self.Num -= num

#인스턴스 생성
n = NumBox(40)
n.add(50)
print(n.Num)
n.remove(50)
print(n.Num)
