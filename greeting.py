#!/usr/bin/env python
def greeting():
	name = input("Please enter your name: ")
	print("Hello, {}.".format(name))

def main():
	greeting()

if __name__ == "__main__":
	main()