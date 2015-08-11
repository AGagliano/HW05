#!/usr/bin/env python
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the 
# words with more than 20 characters (not counting whitespace).
##############################################################################

# Body

fin = open('words.txt')

while True:
	line = fin.readline()
	if not line: 						#Breaks from loop at end of file.						
		break
	word = line.strip()
	if len(word) > 20:
		print word

##############################################################################
def main():
    pass # Call your functions here.

if __name__ == '__main__':
    main()
