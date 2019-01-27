
from string import Template
def main():
	str1 = "You are reading book {0} by author {1}".format("Advance Python",  "joe Marini")
	print(str1)

	templ=Template("You are reading book ${title} by author ${author}")
	str2=templ.substitute(title="Advance Python", author="Joe Marini")
	print(str2)

	Data={"title":"Advance python",
	"author":"Joe Marini"}

	str3=templ.substitute(Data)
	print(str3)


if __name__ == "__main__":
	main()
