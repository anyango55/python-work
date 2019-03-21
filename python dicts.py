Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> courses = [maths,english,science,history]
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    courses = [maths,english,science,history]
NameError: name 'maths' is not defined
>>> courses = ['maths','english','science','history']
>>> courses.append('art')
>>> print(courses)
['maths', 'english', 'science', 'history', 'art']
>>> courses.insert(0,'computer')
>>> print(courses)
['computer', 'maths', 'english', 'science', 'history', 'art']
>>> print(courses)
['computer', 'maths', 'english', 'science', 'history', 'art']
>>> 
>>> courses.insert(2,'computer')
>>> print(courses)
['computer', 'maths', 'computer', 'english', 'science', 'history', 'art']
>>> courses 2 = ['electronics','hardware',]
SyntaxError: invalid syntax
>>> courses_2 = ['electronics','hardware',]
>>> courses.insert(0,'courses_2')
>>> print(courses_2)
['electronics', 'hardware']
>>> print(courses2)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(courses2)
NameError: name 'courses2' is not defined
>>> print(courses)
['courses_2', 'computer', 'maths', 'computer', 'english', 'science', 'history', 'art']
>>> print(courses_2)
['electronics', 'hardware']
>>> courses.insert(0,'courses_2')
>>> print(courses)
['courses_2', 'courses_2', 'computer', 'maths', 'computer', 'english', 'science', 'history', 'art']
>>> courses.insert(0,courses_2)
>>> print(courses)
[['electronics', 'hardware'], 'courses_2', 'courses_2', 'computer', 'maths', 'computer', 'english', 'science', 'history', 'art']
>>> 
============ RESTART: C:/Users/student/Documents/PYTHON/charm.py ============
>>> courses = ['maths','english','science','history']
>>> print(courses)
['maths', 'english', 'science', 'history']
>>> courses.append(art)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    courses.append(art)
NameError: name 'art' is not defined
>>> courses.append('art')
>>> print(courses)
['maths', 'english', 'science', 'history', 'art']
>>> courses.insert(0,'geography')
>>> print(courses)
['geography', 'maths', 'english', 'science', 'history', 'art']
>>> courses2 = ['kiswahili','religious']
>>> courses_2 = ['kiswahili','religious']
>>> print(courses_2)
['kiswahili', 'religious']
>>> courses.insert(0,courses_2)
>>> print(courses)
[['kiswahili', 'religious'], 'geography', 'maths', 'english', 'science', 'history', 'art']
>>> [['kiswahili', 'religious'], 'geography', 'maths', 'english', 'science', 'history', 'art']
[['kiswahili', 'religious'], 'geography', 'maths', 'english', 'science', 'history', 'art']
>>> courses.append(courses_2)
>>> print(courses)
[['kiswahili', 'religious'], 'geography', 'maths', 'english', 'science', 'history', 'art', ['kiswahili', 'religious']]
>>> [['kiswahili', 'religious'], 'geography', 'maths', 'english', 'science', 'history', 'art', ['kiswahili', 'religious']]
[['kiswahili', 'religious'], 'geography', 'maths', 'english', 'science', 'history', 'art', ['kiswahili', 'religious']]
>>> courses.extend(courses_2)
>>> print(courses_2)
['kiswahili', 'religious']
>>> courses.extend(courses)
>>> courses.extend(courses_2)
>>> print(courses)
[['kiswahili', 'religious'], 'geography', 'maths', 'english', 'science', 'history', 'art', ['kiswahili', 'religious'], 'kiswahili', 'religious', ['kiswahili', 'religious'], 'geography', 'maths', 'english', 'science', 'history', 'art', ['kiswahili', 'religious'], 'kiswahili', 'religious', 'kiswahili', 'religious']
>>> courses.extend(courses_2)
>>> print(courses)
[['kiswahili', 'religious'], 'geography', 'maths', 'english', 'science', 'history', 'art', ['kiswahili', 'religious'], 'kiswahili', 'religious', ['kiswahili', 'religious'], 'geography', 'maths', 'english', 'science', 'history', 'art', ['kiswahili', 'religious'], 'kiswahili', 'religious', 'kiswahili', 'religious', 'kiswahili', 'religious']
>>> 
>>> 
>>> 
>>> 
>>> student={"name":"Natasha","age":18}
>>> student={"name":"Natasha","age":18}
>>> student={"name":"Natasha","age":18}
>>> student={"name":"Natasha","age":18}
>>> student={"name":"Natasha","age":18}
>>> student={"name":"Natasha","age":18}
>>> student={"name":"Joy","age":20}
>>> student={"name":"Grace","age":18}
>>> student={"name":"Dee","age":39}
>>> student={"name":"Nikki","age":9}
>>> student1={"name":"Natasha","age":18}
>>> 
>>> 
>>> student1={"name":"Natasha","age":18}
>>> student=2{"name":"Joy","age":20}
SyntaxError: invalid syntax
>>> student=2{"name":"Joy","age":20}
SyntaxError: invalid syntax
>>> 
>>> 
>>> student1={"name":"Natasha","age":18}
>>> student2={"name":"Joy","age":20}
>>> student3={"name":"Grace","age":18}
>>> student4={"name":"Dee","age":39}
>>> student5={"name":"Nikki","age":9}
>>> student1
{'name': 'Natasha', 'age': 18}
>>> students=[student1,student2,student3,student4,student5]
>>> students
[{'name': 'Natasha', 'age': 18}, {'name': 'Joy', 'age': 20}, {'name': 'Grace', 'age': 18}, {'name': 'Dee', 'age': 39}, {'name': 'Nikki', 'age': 9}]
>>> for student in students:
	print(student["name"])

	
Natasha
Joy
Grace
Dee
Nikki
>>> for student in students:
	print(student["age"])

	
18
20
18
39
9
>>> for student in students:
	print(student["year of birth"])

	
Traceback (most recent call last):
  File "<pyshell#80>", line 2, in <module>
    print(student["year of birth"])
KeyError: 'year of birth'
>>> for student in students:
	print(student["2018-"age"])
		      
SyntaxError: invalid syntax
>>> 
		      
>>> for student in students:
	print(student[2018-"age"])

		      
Traceback (most recent call last):
  File "<pyshell#84>", line 2, in <module>
    print(student[2018-"age"])
TypeError: unsupported operand type(s) for -: 'int' and 'str'
>>> for student in students:
	print(2019- student["age"])

		      
2001
1999
2001
1980
2010
>>> customer1={"name":"Stella""balance":2000}
		      
SyntaxError: invalid syntax
>>> customer1={"name":"Stella","balance":2000}
		      
>>> customer2={"name":"larry","balance":3400}
		      
>>> customer3={"name":"Sasha","balance":5698}
		      
>>> customer4={"name":"John","balance":4560}
		      
>>> customer=[customer1,customer2,customer3,customer4]
		      
>>> 
		      
>>> customers=[customer1,customer2,customer3,customer4]
		      
>>> customers
		      
[{'name': 'Stella', 'balance': 2000}, {'name': 'larry', 'balance': 3400}, {'name': 'Sasha', 'balance': 5698}, {'name': 'John', 'balance': 4560}]
>>> message= " 'Hello' {} 'your curent balance is' {}".format(name,balance)
		      
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    message= " 'Hello' {} 'your curent balance is' {}".format(name,balance)
NameError: name 'name' is not defined
>>> message= " 'Hello' {} 'your curent balance is' {}".format('name','balance')
		      
>>> message=  'Hello {} your curent balance is {}'.format('name','balance')
		      
>>> print(message)
		      
Hello name your curent balance is balance
>>> message=  'Hello {} your curent balance is {}'.format(name,balance)
		      
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    message=  'Hello {} your curent balance is {}'.format(name,balance)
NameError: name 'name' is not defined
>>> message= " 'Hello' {} 'your curent balance is' {}".format(name,balance)
		      
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    message= " 'Hello' {} 'your curent balance is' {}".format(name,balance)
NameError: name 'name' is not defined
>>> message= 'Hello {} your curent balance is {}'.format(customer 'name','balance')
		      
SyntaxError: invalid syntax
>>> message= 'Hello {} your curent balance is {}'.format( 'name','balance')
		      
>>> for customer in customers:
		      message="Hello{},your balance is{}".format(customer["name"],customer["balance"])

		      
>>> for customer in customers:
		      message="Hello{},your balance is{}".format(customer["name"],customer["balance"])
		      print(message)

		      
HelloStella,your balance is2000
Hellolarry,your balance is3400
HelloSasha,your balance is5698
HelloJohn,your balance is4560
>>> for customer in customers:
		      print(customer["balance"]/2.6)

		      
769.2307692307692
1307.6923076923076
2191.5384615384614
1753.8461538461538
>>> for customer
		      
SyntaxError: invalid syntax
>>> SyntaxError: invalid syntax
		      
SyntaxError: invalid syntax
>>> 
		      
>>> for customer in customers:
		      message="Hello{},your balance is{}.\n and you qualify for a loan of{}".format(customer["name"],customer["balance"],customer["balance"]/2.6)
		      print(message)

		      
HelloStella,your balance is2000.
 and you qualify for a loan of769.2307692307692
Hellolarry,your balance is3400.
 and you qualify for a loan of1307.6923076923076
HelloSasha,your balance is5698.
 and you qualify for a loan of2191.5384615384614
HelloJohn,your balance is4560.
 and you qualify for a loan of1753.8461538461538
>>> 
