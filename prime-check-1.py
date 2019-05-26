#!/usr/bin/python
n = int(input("Please Enter Integer to validate Prime Number: "))

def myprime(n):

	for i in range(2, n):
		if n<= 1:
			return False
		else:
			if n % i == 0:
				return False

	return True


if myprime(n):
	print("Number ", n, "is Prime Number")
else:
	print("Number", n, "is Not Prime")


