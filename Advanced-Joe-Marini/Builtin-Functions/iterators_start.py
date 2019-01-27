#use iterator functions like enumarate, zip,iter,next

def main():
	days= ["Sun", "Mon", "Tue", "Wed", "Thur", "Fri" ,"SAT"]
	daysfr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]


  # TODO: use iter to create an iterator over a collection

#	i = iter(days)
#	print(next(i))
#	print(next(i))
#	print(next(i))

    # TODO: iterate using a function and a sentinel

	with open('testfile.txt' , "r") as fp:
		for line in iter(fp.readline , ''):
			print(line)

    # TODO: use regular interation over the days
	for line in range(len(days)):
		print(line+1, days[line])

    # TODO: using enumerate reduces code and provides a counter

	for i,m in enumerate(days):
		print(i,m)

    # TODO: use zip to combine sequences

	for i,m in enumerate(zip(days, daysfr) , start=1):
		print(i,m[0], "=", m[1] ,"Frensch version")

if __name__ == "__main__":
	main()
