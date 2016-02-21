
## Types
#1
print "This is a string"

#2
print 2
#2a
print float(2)
#2b
print str(2)

#3
print 2.5
#3a
print int(2.5)
#3b
print str(2.5)

#4
print 2 == 2
#4a
print int (2 == 2)
#4b
print str(2 == 2)

#5
my_name = "Julie"
#5a
print type(my_name)

#6
my_height = 66
#6a
print type(my_height)

#7
print my_name + " is " + str(my_height) + " inches tall"
#7a
print my_name, "is", str(my_height), "inches tall"
#7b
print "%s is %i inches tall" % (my_name,my_height)


## Fuctions
#1
def convert_to_seconds(h,m,s):
	return h*3600 + m*60 + s
#2
def convert_to_hours(s):
	h = s/3600
	m = (s%3600)/60
	s = s-(h*3600)-(m*60)
	return (h,m,s)
#2a	
def print_time(tuple):
	print "Hours: %i, Minutes: %i, Seconds: %i" % (tuple[0],tuple[1],tuple[2])

#3
def convert_to_inches(f,i):
	return f*12 + i

#4
def convert_to_feet(i):
	feet = i/12
	inches = i-(feet*12)
	return (feet,inches)

#4a
def print_feet(tuple):
	print "Feet: %i, Inches: %i" % (tuple[0],tuple[1])

#5
def recursive_fxn():
	i = 0
	for x in range(6):
		print i
		i += 2

#6
def crazy_count_for():
	x = 0
	for i in range(20):
		if x < 10:
			print x 
			x += 1
		elif x == 10:
			print x
			x += 10
		else:
			print x
			x += 10
#6a
def crazy_count_while():
	x = 0
	while x < 101:
		if x < 10:
			print x 
		
		elif x == 10:
			print x
			x += 10
		else:
			print x
			x += 10

#6b

#7
def unique_letters(first,last):
	full_name = first.lower() + last.lower()
	count = []
	for x in full_name:
		if x not in count:
			count.append(x)
	return len(count)

## Conditionals
#1
num1 = 75
if num1 > 50:
	print "too high!"
else:
	print "too low!"

#1a
num1 = 50
if num1 > 50:
	print "too high!"
elif num1 == 50:
	print "just right!"
else:
	print "too low!"

#2
str1 = "2"
if type(str1) != str:
	print str(str1)

## List & Tuples
#1
primary_colors = ("red","yellow","blue")

#1a
print primary_colors[2]
print primary_colors[-1]

#1b
secondary_colors = ("orange","green","purple")

#1c
all_colors = primary_colors + secondary_colors

#2
full_name = ("Julie", "Truong")
full_name = list(full_name)
full_name = full_name[::-1]

## Loops
#1
for x in range(100):
	print x
	x +=1

#2
x = 0
while x <= 1000:
	print x
	x += 100

#3
x = 1000
while x > 99:
	print x
	x -= 100


