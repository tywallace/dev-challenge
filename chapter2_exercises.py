# Exercises for chapter 2:

# Name:Tyler Wallace

#2.1 
#The numbers seem to be in base 8.

#2.2
x=2
5
print 5
print x - 5
print x + 1

#I gave x the value of 2 as indicated slightly before the exercise. 

width = 17
height = 12.0
delimiter = "."

#1: Either 8 or 9 since it is an integer so it can't have a decimal. (After checking I see that it is 8)
print width/2
print type(width/2)

#2 8.5 since dividing by a float will make the result a float.
print width/2.0
print type(width/2.0)

#3 4.0 because it is a float it will have a decimal.
print height/3
print type(height/3)

#4 It should be 11 and an integer
print 1+2*5
print type(1+2*5)

#5 Since delimiter is a string it will repeat 5 times.
print delimiter*5
print type(delimiter*5)

#2.4 

#1
pi = 3.1415926535897932
print (4.0/3.0)*pi*(5**3)

#2
cover = 24.95
discount = 0.4
n = 60
shipping = 3 + .75*(n-1)

print cover*discount*n + shipping 

#The total price is $646.05

#3

import datetime

minute = 60
hour = 60*minute
pace1 = 8*minute+15
pace2 = 7*minute+12

tottime=2*pace1 + 3*pace2
print tottime
totminutes = tottime / 60.0
print totminutes

starttime = 6*hour + 52*minute
finishtime = starttime + tottime
print finishtime

finishhour = finishtime/(hour)
print finishhour
finishminute = (finishtime - (finishhour*hour))/minute
print finishminute
finishsecond = finishtime - (finishminute*minute) -(finishhour*hour)
print finishsecond

finish = datetime.time(finishhour, finishminute, finishsecond)
print finish