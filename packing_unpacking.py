Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
=== RESTART: C:/Users/Pavanj/Desktop/python bible/argumentandpyarameter.py ===
>>> about("pavan",20,"python")
'Meet pavan! They are 20 years old and they like python'
>>> #packing and unpacking aruguments
>>> print(1,2,3,4,5)
1 2 3 4 5
>>> numbers=[1,2,3,4,5]
>>> print(numbers)
[1, 2, 3, 4, 5]
>>> print(*numbers)
1 2 3 4 5
>>> #the above one is unpacking
>>> # Now the packing
>>> def add(*numbers)
SyntaxError: invalid syntax
>>> def add(*numbers):
	total=0
	for number in numbers:
		total = total+numbers
		return(total)

	
>>> add(1,2,3,4,5)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    add(1,2,3,4,5)
  File "<pyshell#14>", line 4, in add
    total = total+numbers
TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
>>> def add(*numbers):
	total=0
	for number in numbers:
		total = total+numbers
		return(total)

	
>>> add(1,2,3)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    add(1,2,3)
  File "<pyshell#17>", line 4, in add
    total = total+numbers
TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
>>> 
