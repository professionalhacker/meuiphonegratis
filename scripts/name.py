import sys

def greetName(name):
	print("Hello " + name + ", how are you?")

def readName():
	name = input("What is your name?: ")
	greetName(name)

if __name__ == '__main__':
	readName()	
