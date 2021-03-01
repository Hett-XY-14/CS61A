print("Count up to:")

def count_up(n):

	"""Prints the numbers from 1 to n. 
	>>> count_up(1)
	1
	>>> count_up(2)
	1
	2
	>>> count_up(4)
	1
	2
	3
	4
	"""
	
	# Base Case: 
	if (n == 1):
		print (n)
	else:
		count_up(n-1)
		print(n)
	
count_up(7)
	
print("\n")

print("Sum Digits:")
def sum_digits(n):
	"""Calculates the sum of the digits 'n'.

	>>> sum_digits(9)
	9
	>>> sum_digits(19)
	10
	>>> sum_digits(2019)
	12
	"""

	if (n < 10):
		return n
	else:
		return sum_digits(n//10) + n%10


print(sum_digits(2019))


