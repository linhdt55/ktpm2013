import math

class test:
	a=""
	b=""
	c=""
	def __init__(self, a , b , c):
		self.a = a
		self.b = b
		self.c = c

	def testIsTriangle(self):
		if self.a + self.b > self.c and self.c + self.b > self.a and self.a + self.c > self.b and self.a > 0.0 and self.b > 0.0 and self.c > 0.0:
			return True
		return False
	def testShape(self):
		if self.a == self.b == self.c:
			print "Tam Giac Deu"
			return
		if (self.a == self.b and self.a*self.a + self.b*self.b == self.c*self.c) or (self.a == self.c and self.a*self.a + self.c*self.c == self.b*self.b) or (self.c == self.b and self.c*self.c + self.b*self.b == self.a*self.a):
			print "Tam Giac Vuong Can"
			return
		if (self.a*self.a + self.b*self.b == self.c*self.c) or (self.a*self.a + self.c*self.c == self.b*self.b) or (self.c*self.c + self.b*self.b == self.a*self.a):
			print "Tam Giac Vuong"
			return
		if (self.a == self.b) or (self.a == self.c) or (self.b == self.c):
		 	print "Tam Giac Can"
		 	return
		print "Tam Giac Thuong"
		return

	def resulf(self):
		if self.testIsTriangle() :
			self.testShape()
		else : 
			print "Khong Phai La Tam Giac"
		pass
def Input(number):
	try :
		inl = float(raw_input("Nhap canh %d = " %number ))
	except ValueError : 
		print " gia tri nhap vao phai la so "
		try :
			inl = float(raw_input("Nhap canh %d = " %number))
		except ValueError:
			print " ban vui long thu lai xin cam on"
			return False
	return inl
	pass
if __name__ == '__main__':
	so1 = Input(1)
	so2 = Input(2)
	so3 = Input(3)
	resul = test(so1 , so2 , so3)
	resul.resulf()
