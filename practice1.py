"""
Rotate an Array by One Position
Write a function that rotates an array to the right by 
one position (i.e., the last element moves to the first position).
"""
def rotateArr(arr):
	"""
	if len(arr) <= 1:
		return arr
	arr.insert(0, arr.pop())
	return arr
	"""
	if len(arr) <= 1:
		return arr
	moving = 1
	while moving < len(arr):
		temp = arr[moving]
		arr[moving] = arr[0]
		arr[0] = temp
		moving += 1
	return arr

"""
Left Rotation by K Positions
Write a function to rotate an array to the left by k positions.
Use modular arithmetic to handle the array indexing.
"""
def leftRot(arr, k):
	if len(arr) <= 1:
		return arr
	k = k % len(arr)
	return arr[k:] + arr[:k]

"""
Insert an Element at a Specific Index
Write a function that inserts a new element at a specific index in the array, 
shifting the other elements to the right.
"""
def insertElem(arr, index, elem):
	return arr[:index] + [elem] + arr[index:]

"""
Multiplication Table
Write a program that prints the multiplication table for numbers from 1 to N.
Example: For N=5:
1  2  3  4  5
2  4  6  8  10
3  6  9  12 15
4  8  12 16 20
5  10 15 20 25
"""
def multTable(n):
	table = ""
	for r in range(1, n + 1):
		row = []
		for c in range(1, n + 1):
			spaces = (len(str(n * n)) - len(str(r * c))) * " "
			row.append(str(r * c) + spaces)
		table += " ".join(row) + "\n"
	print(table)
multTable(10)
multTable(5)
multTable(1)

"""
Print a Pyramid of Numbers
Write a program that prints a pyramid of numbers of height N, 
where the numbers increase along each row.
   1
  1 2
 1 2 3
1 2 3 4
"""
def pyramid(n):
	if n == 0:
		return ""
	pyr = ""
	for r in range(1, n + 1):
		row = []
		spaces = " " * (n - r)
		for c in range(r):
			row.append(str(c + 1))
		pyr += spaces + " ".join(row) + "\n"
	print(pyr)
pyramid(4)
pyramid(1)
pyramid(0)

"""
Sum of Multiples of a Number
Write a program that computes the sum of all 
multiples of a given number M up to N.
Example: M = 3, N = 10
Sum of multiples of 3 up to 10 is 18
"""
def sumMult(m, n):
	total = 0
	for i in range(0, n, m):
		total += i
	return total
print(sumMult(3, 10))
print(sumMult(1, 10))

"""
Print an Inverted Pyramid of Stars
Write a program that prints an inverted pyramid of *
characters with a base width of N.
Example: N=5
*****
 ****
  ***
   **
    *
"""
def invPyrStars(n):
	if n == 0:
		return ""
	pyr = ""
	for i in range(n, 0, -1):
		spaces = (n - i) * " "
		stars = i * "*"
		pyr += spaces + stars + ("\n" if i > 1 else "")
	print(pyr)
invPyrStars(5)
invPyrStars(1)
invPyrStars(0)