#Use transform functions like filter, sort,map

def filterFunc(x):
	if x %2 == 0:
		return False
	return True

def filterFunc2(x):
	if x.isupper():
		return False
	return True



def squareFunc(x):
	pass

def toGrade(x):
	pass


def main():
	num = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
	chars = "abcDeFGHiJklmnoP"
	grades = (81, 89, 94, 78, 61, 66, 99, 74)


    # TODO: use filter to remove items from a list

	odds = filter(filterFunc, num)
	print("ODD Numbers:", odds)

    # TODO: use filter on non-numeric sequence

	lowers = filter(filterFunc2, chars)
	print("Lower Characters are printed :", lowers)

    # TODO: use map to create a new sequence of values

    # TODO: use sorted and map to change numbers to grades



if __name__ == "__main__":
	main()
