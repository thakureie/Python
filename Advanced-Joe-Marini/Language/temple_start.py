#demonstarte template string functions

from string import Template

def main():
	#usual string formattin with format()
	str1 = "You're watching {0} by {1}".format("Advanced Python", "Joe Marini")
	print(str1)

#TODO :  create a template with placeholders
	templ = Template("You're watching ${title} by ${author}")
	str2= templ.substitute(title="Advanced Python", author="Joe Marini") 
	print(str2)
# TODO: use the substitute method with keyword arguments
    
# TODO: use the substitute method with a dictionary

	str3 = {"title" :"Advanced Python",
		"author":"Joe Marini" }
	str4= templ.substitute(str3)
	print(str4)
if __name__ == "__main__":
	main()
