import math
import unittest
import input
import itertools

def data():
	doc = input.main.__doc__
	bien1 = doc
	bien2 = bien1.split("\n")
	x = 1
	i=0
	j=0
	y=0
	t=0
	mang = ['a' , 'b' , 'c' ,'d' , 'e' ]
	list1 = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'k']
	while x < len(bien2)-1:
		thamso = bien2[x].split(":")
		thamso1 = thamso[1].split("]")
		while y < len(thamso1)-1:
			thamso2 = thamso1[y].split("[")
			mang[i] = thamso2[1].split(";")
			mang[i][0] = int(mang[i][0])
			mang[i][1] = int(mang[i][1])
			y = y+1
			i = i+1
		if i == 1:
			list1[t] = [mang[0][0]]
			if mang[0][0] > mang[0][1]:
				raise Exception("wrong input")
		if i == 2:
			list1[t] = [mang[0][0] , mang[1][0]]
			a = mang[0][0]
			b = mang[1][0]
			A = [a , b]
			A.sort()
			if mang[0][0] > mang[0][1] or mang[1][0] > mang[1][1]:
				raise Exception("wrong input")
			if A[0] == a and mang[0][1] >= b:	
				raise Exception("wrong input")
			if A[0] == b and mang[1][1] >= a:
				raise Exception("wrong input")
		if i == 3:
			list1[t] = [mang[0][0] , mang[1][0], mang[2][0]]
			a = mang[0][0]
			b = mang[1][0]
			c = mang[2][0]
			A = [a , b ,c]
			A.sort()
			if mang[0][0] > mang[0][1] or mang[1][0] > mang[1][1] or mang[2][0] > mang[2][1]:
				raise Exception("wrong input")
			if A[0] == a and A[1] == b and (mang[0][1] >= b or mang[1][1] >= c):
				raise Exception("wrong input")
			if A[0] == a and A[1] == c and (mang[0][1] >= c or mang[2][1] >= b): 
				raise Exception("wrong input")
			if A[0] == b and A[1] == a and (mang[1][1] >= a or mang[0][1] >= c): 
				raise Exception("wrong input")
			if A[0] == b and A[1] == c and (mang[1][1] >= c or mang[2][1] >= a): 
				raise Exception("wrong input")
			if A[0] == c and A[1] == a and (mang[2][1] >= a or mang[0][1] >= b): 
				raise Exception("wrong input")
			if A[0] == c and A[1] == b and (mang[2][1] >= b or mang[0][1] >= a): 
				raise Exception("wrong input")
		if i == 4:
			list1[t] = [mang[0][0] , mang[1][0], mang[2][0],mang[3][0]]
			a = mang[0][0]
			b = mang[1][0]
			c = mang[2][0]
			d = mang[3][0]
			A = [a , b, c, d]
			A.sort()
			if mang[0][0] > mang[0][1] or mang[1][0] > mang[1][1] or mang[2][0] > mang[2][1] or mang[3][0] > mang[3][1]:
				raise Exception("wrong input")
			if A[0] == a and A[1] == b and A[2] == c and (mang[0][1] >= b or mang[1][1] >= c or mang[2][1] >= d):
				raise Exception("wrong input")
			if A[0] == a and A[1] == b and A[2] == d and (mang[0][1] >= b or mang[1][1] >= d or mang[3][1] >= c): 
				raise Exception("wrong input")
			if A[0] == a and A[1] == c and A[2] == b and (mang[0][1] >= c or mang[2][1] >= b or mang[1][1] >= d): 
				raise Exception("wrong input")
			if A[0] == a and A[1] == c and A[2] == d and (mang[0][1] >= c or mang[2][1] >= d or mang[3][1] >= b): 
				raise Exception("wrong input")
			if A[0] == a and A[1] == d and A[2] == b and (mang[0][1] >= d or mang[3][1] >= b or mang[1][1] >= c): 
				raise Exception("wrong input")
			if A[0] == a and A[1] == d and A[2] == c and (mang[0][1] >= d or mang[3][1] >= c or mang[1][1] >= b): 
				raise Exception("wrong input")
			if A[0] == b and A[1] == a and A[2] == c and (mang[1][1] >= a or mang[0][1] >= c or mang[2][1] >= d):
				raise Exception("wrong input")
			if A[0] == b and A[1] == a and A[2] == d and (mang[1][1] >= a or mang[0][1] >= d or mang[3][1] >= c):
				raise Exception("wrong input")
			if A[0] == b and A[1] == c and A[2] == a and (mang[1][1] >= c or mang[2][1] >= a or mang[0][1] >= d):
				raise Exception("wrong input")
			if A[0] == b and A[1] == c and A[2] == d and (mang[1][1] >= c or mang[2][1] >= d or mang[3][1] >= a):
				raise Exception("wrong input")
			if A[0] == b and A[1] == d and A[2] == a and (mang[1][1] >= d or mang[3][1] >= a or mang[0][1] >= c):
				raise Exception("wrong input")
			if A[0] == b and A[1] == d and A[2] == c and (mang[1][1] >= d or mang[3][1] >= c or mang[2][1] >= a):
				raise Exception("wrong input")
			if A[0] == c and A[1] == b and A[2] == a and (mang[2][1] >= b or mang[1][1] >= a or mang[0][1] >= d):
				raise Exception("wrong input")
			if A[0] == c and A[1] == b and A[2] == d and (mang[2][1] >= b or mang[1][1] >= d or mang[3][1] >= a):
				raise Exception("wrong input")
			if A[0] == c and A[1] == a and A[2] == b and (mang[2][1] >= a or mang[0][1] >= b or mang[1][1] >= d):
				raise Exception("wrong input")
			if A[0] == c and A[1] == a and A[2] == d and (mang[2][1] >= a or mang[0][1] >= d or mang[3][1] >= b):
				raise Exception("wrong input")
			if A[0] == c and A[1] == d and A[2] == b and (mang[2][1] >= d or mang[3][1] >= b or mang[1][1] >= a):
				raise Exception("wrong input")
			if A[0] == c and A[1] == d and A[2] == a and (mang[2][1] >= d or mang[3][1] >= a or mang[0][1] >= b):
				raise Exception("wrong input")
			if A[0] == d and A[1] == a and A[2] == c and (mang[3][1] >= a or mang[0][1] >= c or mang[2][1] >= b):
				raise Exception("wrong input")
			if A[0] == d and A[1] == a and A[2] == b and (mang[3][1] >= a or mang[0][1] >= b or mang[1][1] >= c):
				raise Exception("wrong input")
			if A[0] == d and A[1] == c and A[2] == a and (mang[3][1] >= c or mang[2][1] >= a or mang[0][1] >= b):
				raise Exception("wrong input")
			if A[0] == d and A[1] == c and A[2] == b and (mang[3][1] >= c or mang[2][1] >= b or mang[3][1] >= a):
				raise Exception("wrong input")
			if A[0] == d and A[1] == b and A[2] == a and (mang[3][1] >= b or mang[1][1] >= a or mang[0][1] >= c):
				raise Exception("wrong input")
			if A[0] == d and A[1] == b and A[2] == c and (mang[3][1] >= b or mang[1][1] >= c or mang[2][1] >= a):
				raise Exception("wrong input")
		t = t+1
		x = x+1
		i = 0
		y = 0
	if t == 1:
		list2 = list(itertools.product(list1[0]))
		return list2
	if t == 2:
		list2 = list(itertools.product(list1[0] , list1[1]))
		return list2
	if t == 3:
		list2 = list(itertools.product(list1[0] , list1[1] , list1[2]))
		return list2
	if t == 4:
		list2 = list(itertools.product(list1[0] , list1[1] , list1[2] , list1[3]))
		return list2
	if t == 5:
		list2 = list(itertools.product(list1[0] , list1[1] , list1[2] , list1[3] , list1[4]))
		return list2
	if t == 6:
		list2 = list(itertools.product(list1[0] , list1[1] , list1[2] , list1[3] , list1[4] , list1[5]))
		return list2
	if t == 7:
		list2 = list(itertools.product(list1[0] , list1[1] , list1[2] , list1[3] , list1[4] , list1[5] , list1[6]))
		return list2
	if t == 8:
		list2 = list(itertools.product(list1[0] , list1[1] , list1[2] , list1[3] , list1[4] , list1[5] , list1[6] , list1[7]))
		return list2
	if t == 9:
		list2 = list(itertools.product(list1[0] , list1[1] , list1[2] , list1[3] , list1[4] , list1[5] , list1[6] , list1[7], list1[8]))
		return list2
	if t == 10:
		list2 = list(itertools.product(list1[0] , list1[1] , list1[2] , list1[3] , list1[4] , list1[5] , list1[6] , list1[7], list1[8] , list1[9]))
		return list2
class testCase(unittest.TestCase):
	pass
def addFunction(parameter):
	def test(self):
		self.assertEqual(input.main(*parameter),'')
	return test
k=0
value = ""

for j in data():
	value = addFunction(j)
	func_name="test_" + str(k)
	setattr(testCase,func_name,value)
	k=k+1
if __name__=="__main__":
	unittest.main()
