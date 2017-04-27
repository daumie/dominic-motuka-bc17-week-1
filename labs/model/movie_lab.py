#!/usr/bin/python

def canIWatch(age):
	'''Confirms whether a user is allowed to watch Deadpool'''
	if (age > 0 and age <6):
		return("You are not allowed to watch Deadpool after 6.00pm.")
	elif (age>=6 and age <17):
		return("You must be accompanied by a guardian who is 21 or older.")
	elif (age>=17 and age<25):
		return("You are allowed to watch Deadpool, right after you show some ID.")
	elif (age >= 25):
		return("Yay! You can watch Deadpool with no strings attached!")
	else:
		return("Invalid age")
canIWatch(5)