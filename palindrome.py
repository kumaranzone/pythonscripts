#!/usr/bin/env python

inputString = raw_input("Enter string: \n")
if(str(inputString) == str(inputString)[::-1]):
	print "Palindrome"
else:
	print "Not a palindrome"


