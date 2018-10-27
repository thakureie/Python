#!/usr/bin/python
ten_things = "Orage My name is ABhimanyu Thakur"
print("Let's check if we have 10 things in list else add some more")

more_stuff = ["apple", "abc", "ram", "shyam", "ghanshyam", "chainpur", " Saharsa"]

stuff = ten_things.split(' ')


while len(stuff) != 10:
	next_one = more_stuff.pop()
	print("Adding: " , next_one)
	stuff.append(next_one)
	print("Now we have %d items " % len(stuff))

print("Now list is complete as we have 10 items" % stuff)

print("Leti us do some more stuff ")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
