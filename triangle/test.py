import unittest
import triangle
import math
import decimal

class testCase(unittest.TestCase):

	def test1(self):
		self.assertEqual(triangle.detect_triangle("a" , 3.0 , 5.0) , 'gia tri nhap vao phai la so float')

	def test2(self):
	 	self.assertEqual(triangle.detect_triangle(3.0 , "a" , 5.0) , 'gia tri nhap vao phai la so float')

	def test3(self):
	 	self.assertEqual(triangle.detect_triangle(4.0 , 3.0 , "a") , 'gia tri nhap vao phai la so float')

	def test4(self):
	 	self.assertEqual(triangle.detect_triangle(4 , 3 , 5) , 'Tam Giac Vuong')

	def test5(self):
		self.assertEqual(triangle.detect_triangle(1.0 , 2.0 , 3.0) , 'Khong Phai La Tam Giac')

	def test6(self):
	 	self.assertEqual(triangle.detect_triangle(3.0 , -2.0 , 5.0) , 'Khong Phai La Tam Giac')

	def test7(self):
	 	self.assertEqual(triangle.detect_triangle(-3.0 , 2.0 , 5.0) , 'Khong Phai La Tam Giac')

	def test8(self):
	 	self.assertEqual(triangle.detect_triangle(3.0 , 2.0 , -5.0) , 'Khong Phai La Tam Giac')

	def test9(self):
	 	self.assertEqual(triangle.detect_triangle(3.0 , 0.0 , 5.0) , 'Khong Phai La Tam Giac')

	def test10(self):
	 	self.assertEqual(triangle.detect_triangle(3.0 , 4.0 , 5.0) , 'Tam Giac Vuong')

	def test11(self):
	 	self.assertEqual(triangle.detect_triangle(4.0 , 3.0 , 5.0) , 'Tam Giac Vuong')

	def test12(self):
	 	self.assertEqual(triangle.detect_triangle(4.0 , 5.0 , 3.0) , 'Tam Giac Vuong')

	def test13(self):
		self.assertEqual(triangle.detect_triangle(3.0 , 5.0 , math.sqrt(34.0)) , 'Tam Giac Vuong')

	def test14(self):
	 	self.assertEqual(triangle.detect_triangle(3.0 , 3.0 , 3.0) , 'Tam Giac Deu')

	def test15(self):
	 	self.assertEqual(triangle.detect_triangle(5.0 , 6.0 , 7.0) , 'Tam Giac Thuong')

	def test16(self):
		self.assertEqual(triangle.detect_triangle(2.0**31-1 , 2.0**31-1 , math.sqrt(34.0)) , 'Tam Giac Can')

	def test17(self):
	   	self.assertEqual(triangle.detect_triangle(4.0 , 5.0 , math.sqrt(41.0)) , 'Tam Giac Vuong')

	def test18(self):
	   	self.assertEqual(triangle.detect_triangle(math.sqrt(41.0) , 5.0 , 4.0) , 'Tam Giac Vuong')

	def test19(self):
	   	self.assertEqual(triangle.detect_triangle(4.0 , math.sqrt(41.0) , 5.0) , 'Tam Giac Vuong')

	def test20(self):
	  	self.assertEqual(triangle.detect_triangle(2.0**31-1 , 2.0**31-1 , 10.0**2) , 'Tam Giac Can')

	def test21(self):
	   	self.assertEqual(triangle.detect_triangle(6e-10 , 4e-10 , 7e-10) , 'Tam Giac Thuong')

	def test22(self):
	   	self.assertEqual(triangle.detect_triangle(4 , 4 , math.sqrt(32)) , 'Tam Giac Vuong Can')

	def test23(self):
	   	self.assertEqual(triangle.detect_triangle(2.0**31-1 , 10**2 , 2.0**31-1) , 'Tam Giac Can')

	def test24(self):
	   	self.assertEqual(triangle.detect_triangle(10**2 , 2.0**31-1 , 2.0**31-1) , 'Tam Giac Can')

	def test21(self):
	   	self.assertEqual(triangle.detect_triangle(4e-10 , 6e-10 , 7e-10) , 'Tam Giac Thuong')

	def test21(self):
	   	self.assertEqual(triangle.detect_triangle(4e-10 , 7e-10 , 6e-10) , 'Tam Giac Thuong')
if __name__ == "__main__":
	unittest.main()