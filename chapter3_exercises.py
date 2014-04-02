# Exercises for chapter 3:

# Name: Tyler Wallace

#3.1

#The error says that repeat_lyrics is not defined. 

#3.2

#When print_lyrics is after repeat_lyrics it still runs.

def repeat_lyrics():
	print_lyrics()
	print_lyrics()

def print_lyrics():
	print "I'm a lumberjack, and I'm okay."
	print "I sleep all night and I work all day."

repeat_lyrics()

#3.3

def right_justify(s):
	spaces = 70 - len(s)
	print " "*spaces + s

right_justify("allen")

#3.4

#1. 
def do_twice(f):
	f()
	f()

def print_spam():
	print 'spam'

do_twice(print_spam)

#2.

def do_twice_mod(f,v): 
	f(v)
	f(v)

#3
def print_twice(s):
	print s
	print s

#4
do_twice_mod(print_twice,"spam")

#5
def do_four(f,v):
	do_twice_mod(f,v)
	do_twice_mod(f,v)

do_four(print_twice,"spam")