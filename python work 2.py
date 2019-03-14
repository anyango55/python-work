Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> person{'name':'Nikki','age':'8'}
SyntaxError: invalid syntax
>>> person={'name':'Nikki','age':'8'}
>>> person
{'name': 'Nikki', 'age': '8'}
>>> name
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    name
NameError: name 'name' is not defined
>>> person={'name':'Nikki','age':'8'}
>>> statement='Her name is {} she is {} years old.format(person['name'],['age'])
SyntaxError: invalid syntax
>>> statement='Her is {} she is {} years old.format(person['name'],['age'])
SyntaxError: invalid syntax
>>> statement='Her name is {} she is {} years old.format(person['name'],person['age'])
SyntaxError: invalid syntax
>>> sentence = 'Her name is {} she is {} years old.format(person['name'],person['age'])
SyntaxError: invalid syntax
>>> name = Nikki
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    name = Nikki
NameError: name 'Nikki' is not defined
>>> name='Nikki'
>>> name
'Nikki'
>>> age=8
>>> age
8
>>> message='My name is{}and I am{}years old'.format('name','age')
>>> print(message)
My name isnameand I amageyears old
>>> message='My name is {} and I am {} years old'.format('name','age')
>>> print(message)
My name is name and I am age years old
>>> My name is name and I am age years old
SyntaxError: invalid syntax
>>> message='My dentity is {} and I am {} years old'.format('name','age')
>>> print(message)
My dentity is name and I am age years old
>>> message='My dentity is {} and I am {} years old'.format(name,age)
>>> print(message)
My dentity is Nikki and I am 8 years old
>>> courses = ['History','Math','Physics','CompSci']
>>> print(courses)
['History', 'Math', 'Physics', 'CompSci']
>>> 
