Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=[0,1,2,3,4,5,6,7,8,9]
>>> x.append(3.5)
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 3.5]
>>> x.extend([6,7,4,5])
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 3.5, 6, 7, 4, 5]
>>> x.insert(23,43)
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 3.5, 6, 7, 4, 5, 43]
>>> x.remove(43)
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 3.5, 6, 7, 4, 5]
>>> x.index(3.5)
10
>>> x.count(4)
2
>>> x.reverse()
>>> x
[5, 4, 7, 6, 3.5, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> x.sort()
>>> x
[0, 1, 2, 3, 3.5, 4, 4, 5, 5, 6, 6, 7, 7, 8, 9]
>>> y= p*10 in x:
	
SyntaxError: invalid syntax
>>> y = [p*10 for p in x]
>>> y
[0, 10, 20, 30, 35.0, 40, 40, 50, 50, 60, 60, 70, 70, 80, 90]
>>> for p in x:
	print(p*10)

	
0
10
20
30
35.0
40
40
50
50
60
60
70
70
80
90
>>> k=x[ :5]
>>> k
[0, 1, 2, 3, 3.5]
>>> u=[k=x[ :4]
       
SyntaxError: invalid syntax
>>> k=x[ :4]
       
>>> k
       
[0, 1, 2, 3]
>>> k=[ :5]
       
SyntaxError: invalid syntax
>>> k=[ :5]
       
SyntaxError: invalid syntax
>>> k=x[ :5]
       
>>> k
       
[0, 1, 2, 3, 3.5]
>>> u=x[10: ]
       
>>> x
       
[0, 1, 2, 3, 3.5, 4, 4, 5, 5, 6, 6, 7, 7, 8, 9]
>>> n=[1,2,3],[4,5,6],[7,8,9]
       
>>> m[]
       
SyntaxError: invalid syntax
>>> m[]
       
SyntaxError: invalid syntax
>>> n=[[1,2,3],[4,5,6],[7,8,9]]SyntaxError: invalid syntax
       
SyntaxError: invalid syntax
>>> n=[[1,2,3],[4,5,6],[7,8,9]]
       
>>> n=[[1,2,3],[4,5,6],[7,8,9]]
       
>>> m[]
       
SyntaxError: invalid syntax
>>> m=[]
       
>>> for sublist in n:
       for x in sublist:
       m.append(x)
       
SyntaxError: expected an indented block
>>> for sublist in n:
       for x in sublist:
       m.append(x)
       
SyntaxError: expected an indented block
>>> for sublist in n:
       for x in sublist:
       m.append(x)
       
SyntaxError: expected an indented block
>>> n=[[1,2,3],[4,5,6],[7,8,9]]
       
>>> m=[]
       
>>> for sublist in n:
       for x in sublist:
       m.append(x)
       
SyntaxError: expected an indented block
>>> for sublist in n:
       for x in sublist:
	       m.append(x)

       
>>> m
       
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
