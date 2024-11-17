import unittest
from practice1 import rotateArr, leftRot, insertElem

class testRotArr(unittest.TestCase):
	def test(self):
		arr0 = []
		arr1 = [1, 2, 3, 4]
		arr2 = [1, 1, 1, 1]
		arr3 = [1, 3]

		self.assertEqual(rotateArr(arr0), [])
		self.assertEqual(rotateArr(arr1), [4, 1, 2, 3])
		self.assertEqual(rotateArr(arr2), [1, 1, 1, 1])
		self.assertEqual(rotateArr(arr3), [3, 1])

class testLeftRot(unittest.TestCase):
	def test(self):
		arr0 = []
		arr1 = [1, 2, 3, 4]
		arr2 = [1, 1, 1, 1]
		arr3 = [1, 3]
		arr4 = [2, 4, 6, 7, 1, 8]

		self.assertEqual(leftRot(arr0, 1), [])
		self.assertEqual(leftRot(arr1, 1), [2, 3, 4, 1])
		self.assertEqual(leftRot(arr2, 2), [1, 1, 1, 1])
		self.assertEqual(leftRot(arr3, 1), [3, 1])
		self.assertEqual(leftRot(arr4, 2), [6,7,1,8,2,4])
		self.assertEqual(leftRot(arr4, 3), [7,1,8,2,4,6])
		self.assertEqual(leftRot(arr4, 5), [8,2,4,6,7,1])
		
class testInsert(unittest.TestCase):
	def test(self):
		arr4 = [2, 4, 6, 7, 1, 8]
		self.assertEqual(insertElem(arr4, 2, 55), [2,4,55,6,7,1,8])

if __name__ == "__main":
	unittest.main()
