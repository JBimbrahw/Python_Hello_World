#!/usr/bin/env python
def greeting():
	name = input("Please enter your name: ")
	print("Yo, {}.".format(name))

def main():
	greeting()

if __name__ == "__main__":
	main()