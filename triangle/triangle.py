import math
def detect_triangle( a , b , c):
	if isinstance(a , (float,int)) and isinstance(b , (float,int)) and isinstance(c , (float,int)):
		return resulf(a , b , c)
	else:
		return "gia tri nhap vao phai la so float"
		pass
	pass
def testIsTriangle(a , b , c):
	if a + b > c and c + b > a and a + c > b and a > 0.0 and b > 0.0 and c > 0.0 and a <= 2**31-1 and b <= 2**31-1 and c <= 2**31-1:
		return "La Tam Giac"
	return False
def testShape(a , b ,c):
	if a == b == c:
		return "Tam Giac Deu"
	if (a == b and a**2 + b**2 - c**2<10**-20) or (a == c and a**2 + c**2 - b**2<10**-20) or (c == b and c**2 + b**2 - a**2<10**-20):
		return "Tam Giac Vuong Can"
	if (a == b) or (a == c) or (b == c):
		 return "Tam Giac Can"
	if (a*a + b*b - c*c<10**-20) or (a*a + c*c - b*b<10**-20) or (c*c + b*b - a*a<10**-20):
		return "Tam Giac Vuong"
	return "Tam Giac Thuong"

def resulf(a , b ,c):
	if testIsTriangle(a , b ,c) == "La Tam Giac" :
		return testShape(a , b , c)
	else : 
		return "Khong Phai La Tam Giac"
	pass
