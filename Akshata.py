'''
for i in range(1,6,1):
     for j in range(1,i,1):
          print(i,end="")
     print("\r")
'''
'''
for i in range(1,6,1):
     for k in range(1,6-i,1):
          print(end=" ")
     for j in range(1,i,1):
          print(i,end="")
     print("\r")

'''
'''
for i in range(1,6,1):
     for k in range(1,6-i,1):
          print(end=" ")
     for j in range(1,i,1):
          print("*",end="")
     print("\r")
'''
'''
for i in range(1,6,1):
     for j in range(1,6,1):
        print(i,end="")
     print("\r")
'''
'''
for i in range(1,6,1):
     for j in range(1,6,1):
          print("*",end="")
     print("\r")
'''
'''
for i in range(1,6,1):
     for j in range(1,i,1):
          print(i,end="")
     print("\r")     
'''
'''
for i in range(1,6,1):
     for j in range(1,i,1):
          print("*",end="")
     print("\r")     
'''
'''
for i in range(1,6,1):
     for k in range(1,6-i,1):
          print(end="")
     for j in range(1,i,1):
          print(i,end="")
     print("\r")     
'''
'''
for i in range(1,6,1):
     for k in range(1,6-i,1):
          print(end="")
     for j in range(1,i,1):
          print(i,end="")
     print("\r")     
'''
'''
for i in range(1,6,1):
     for k in range(1,6-i,1):
          print(end="")
     for j in range(1,i,1):
          print("*",end="")
     print("\r")     
'''
'''
for i in range(6,1,-1):
     for k in range(1,6-i,1):
          print(end="")
     for j in range(1,i,1):
          print("*",end="")
     print("\r")     
'''
'''
for i in range(1,6,1):
     for k in range(1,6-i,1):
          print(end="")
     for j in range(1,i,1):
          print("*",end="")
     print("\r")
for i in range(6,1,-1):
     for k in range(1,6-i,1):
          print(end="")
     for j in range(1,i,1):
          print("*",end="")
     print("\r")
'''
'''
for i in range(1,8,1):
     for k in range(1,8-i,1):
          print(end="")
     for j in range(1,i,1):
          print("*",end="")
     print("\r")
for i in range(8,1,-1):
     for k in range(1,8-i,1):
          print(end="")
     for j in range(1,i,1):
          print("*",end="")
     print("\r")
'''
'''
for i in range(1,20,1):
     for k in range(1,20-i,1):
          print(end="")
     for j in range(1,i,1):
          print("*",end="")
     print("\r")
for i in range(20,1,-1):
     for k in range(1,20-i,1):
          print(end="")
     for j in range(1,i,1):
          print("*",end="")
     print("\r")
'''
'''
li=[1,2,3,12,45,67,34,89]
m=li[0]
for i in range (0,len(li),1):
    if(li[i]>m):
       m=li[i]
print(m)           
'''
'''
#sum of given list
li=[1,2,3,4,5,12,67,4]
s=0
for i in range(0,len(li),1):
     s=s+li[i]
print(s)     
'''
#avarage
#total/number of values
'''
li=[1,2,3,4,5,6,7,8]
s=0
for i in range(0,len(li),1):
     s=s+li[i]
print(s/li[i])     
'''
#duplicate streem
'''
x='hello'
#helo
s=''
for i in range(0,len(x),1):
     if(x[i] not in s):
          s=s+x[i]
print(s)          
'''
#Duplicate Number
'''
li=[1,2,3,1,5,6,7,8,9,3,2,1,4,5]
res=[]
for i in range(0,len(li),1):
     if (li[i] not in res):
          res.append(li[i])
print(res)          
'''
#Reverse String
'''
x='hello'
#olleh
res=''
for i in range(len(x),0,-1):
     res=res+x[i-1]
print(res)     
'''
#Reverse Number
'''
x='12345'
#54321
res=""
for i in range(len(x),0,-1):
     res=res+x[i-1]
print(res)
print(type(res))
'''
'''
x='12345'
#54321
res=""
for i in range(len(x),0,-1):
     res=res+x[i-1]
     y=int(res)
print(y)
print(type(y))
'''
#given value is palindrome or not
#the given input reverse output that is called palindrome
'''
x='hello'
res=""
for i in range(len(x),0,-1):
     res=res+x[i-1]
if(x==res):
     print(x, 'is a palindrome')
else:
     print(x, 'is not a palindrome')
'''
'''
x='malayalam'
res=""
for i in range(len(x),0,-1):
     res=res+x[i-1]
if(x==res):
     print(x, 'is a palindrome')
else:
     print(x, 'is not a palindrome')
'''
#fibanocci series
#it is used to find the next values
#0,1 are the default value of fibanocci series
#0 1 1 2 3 5 update
'''
n1=0
n2=1
#n3?
for i in range(1,6,1):
     print(n1)
     n3=n1+n2
     n1=n2
     n2=n3
'''
#prime or not
#its divisible by 1 or itself
'''
n=13
x=100
for i in range(2,n,1):
     if(n%i==0):
          x=200
if(x==100):
     print(n,'is a prime')
else:
     print(n,'is not a prime')
'''
'''
n=25
x=100
for i in range(2,n,1):
     if(n%i==0):
          x=200
if(x==100):
     print(n,'is a prime')
else:
     print(n,'is not a prime')
'''
'''
                                                13/3/2025

'''
'''
Functions
==============
it is nothing but group of ststements/block of code is called as a function
-it will perform specific task

2 types
1.Userdefined Functionis a Customised Function based on the user requirement , user can create own function based on the user requirement

2.Built in function : predefined function
def function_name(parameter)
       block a code
Calling function(Arguements)

def  => Key Functions
Function Name =>Camelcase:myNameAkshata
                Pascalcase:MyNameAkshata

Parameters       =>Keys
Arguements       =>Values
Calling Function =>Function_name
'''
'''
def myFunction():
     print('starting loop')
     i=1
     while(i<=5):
          print(i)
          i=i+1
     else:
          print('Ending Function')
myFunction()      
'''
'''
x=100 
def myData(): #Local Variable
     if(x%2==0):
          print(x,'is a even')
     else:
          print(x,'is a odd')
myData()          
'''
'''
x=100 #Global Variable
def myData():
     if(x%2==0):
          print(x,'is a even')
     else:
          print(x,'is a odd')
#myData() 
'''
'''
#Global variable/Global scope
#it is outside the function
#Global variable access anywhere
#local variable /Local scope
#it is inside the function
#it access only in local
'''
'''
a=10
def outer():
     b=20
     print(a+b)
outer()     
'''
#Global convers Local to global
'''
a=10
def outer():
     b=20
     print(a+b)
outer() 
'''
#Parameters:keys
#Arguements:Values
'''
def addData(a,b):
     print(a+b)
addData(1,2)
addData(12,10)
'''
'''
def employe(id,name,email,mobile):
    print('ID:',id)
    print('Name:',name)
    print('email:',email)
    print('Mobile:',mobile)      
employe(1,'baskar','baskar@',9876543210)
employe(2,['basker','chinni','madhu'],'basker@',9874563210)
'''
'''
Lambda Function:
================
-there is no function
-it is singlke line function
-self invoking method:it will invoke automatically-()
-lambda parameters:statements
'''
'''
def main(a,b):
    print(a+b)
main(1,2)
'''
'''
x=lambda a,b:a+b
print(x(1,2))
'''
#Lambda function with Map&filter
#lambda map:it is used to map the values
'''
li=[1,2,3,4,5]
a=list(map(lambda n:n*2,li))
print(a)

b=list(map(lambda x:x+2,li))
print(b)
'''
#Lambda Filter(): it is used to filter the values

'''
li=[1,2,3,4,5,6,7,8,9,10]
a=list(filter(lambda y:y<=5,li))
print(a)

b=list(filter(lambda y:y>=5,li))
print(b)
'''
'''
                                                          14/3/2025
'''      
'''
Exceptional Handling:
====================
handling errors:run time errors it will handle ,try,except,else,finally-by using blocks only we can handle the errors

Try:block of code - we can pass the n number of errors
except:exceptional: handle the error
else: if try is any error except will be excute
      if try no error else will be executed
Finally:operation we are using finally

try:
       block of statements
except:
        handle the errors  
else:
       success
finally:
       always
     
'''
'''
a=20
b=0
print(a/b)
'''
'''
=>Inbuilt functions:
-----------------------
#zerodivisionerror
#valueerror
#indexerror
#nameerror
#Typeerror

'''
'''
try :
li=[1,2,3,4,5]
     print(li[6])
exceptzeroerror:
     print('it is a index error')
except:
     print('i am getting error')
a=10
b=20
print(a/b)
except index error:
    print('it is a index error')
except name errore :
    print('it is a name error')]
except zero division error:
    print('it is a zero division error')
else:
    print('executed successfully')
finally:
    print('always')
    
'''
'''
try:
def employee(id,name,email,mobile):
print('ID:',id)
print('Name:',name)
print('EMail:',email)
print('Mobile:',mobile')

employee(1,'baskar','baskar@',9876543210)
except type error:
   print('it is a typr error')
else:
   print('executed successfully')
finally:
   print('always')

'''
'''
Cll back function:
===================
-calling back function
-one function passed into another function as arguement is called as a callback function
'''
'''
def A()
   print('A function')
A()
def B():
    print('B Function')
B()
'''
#i can call only one function,remaining i can call callback
#B function can passed into A function as an arguement
'''
def A():
print A():
 print('A fun')
 A()
 
def B() 
 print B()
 A(B)
'''
#x=B
#B is send to A , receiving as a parameter,that parameter name is x , x is called as callback function of B function
'''
def A():
    print('A fun")
    second() # callback function of B fun
    third()  # callback function of c fun
def B():
    print('B fun")
def c():
    print('C fun')
A(B,C)    
'''
'''
def A(second , third):
    print('A fun')
    second(1,2) # callback function of B fun
    third(1,2,3)  # callback function of C fun
def B(x,y):
    print('B fun',x+y)
def C(x,y,z):
    print('C fun:',x+y+z)
A(B,C)    
'''

'''
                                                                17/3/2025

'''

'''
File Handling:used to perform CRUD Operations
#create: creat the new file and store the data 
#Read: read the data in the existing file
#update: update the data in the existing file 
#Delete: Delete the data in the existing file

Per that perspective here file handling provides some modes
# Modes
there are three types of modes
Write, Read , Append
Write-w
read-r
append-a

#Create

open()-> predefined function

open('new_file.ext')
open('new_file.ext','mode')

#mode
'''
'''
new_file=open('data.text','w')
new_file.close()
'''
'''
#now i just want to store

#1.write(): takes only one arguements
#2.writelines(): collection of values
'''
'''
new_file=open('data.text','w')
new_file.write('python\n')
new_file.write('java/n')
new_file.write('HTML/n')
new_file.write('CSS/n')

new_file.close()
'''
'''
new_file=open('dat.text','w')
li=['python/n','java/n','CSS/n']
new_file.writelines(li)
new_file.close()
'''
'''
new_file=open('data.text','w')
li=['python','css','java','AWS']
for i in li:
    new_file.writelines(i)
    new_files.writelines('\n')
'''
'''
new_file=open('data.pdf','w')

new_file.closed()
'''

#Read: per that perspective we can use some modes
#read():returns as a some existing structure
#readlines():returns as a list
#readline():returns only one row
'''
file=open('data.text','r')
res=file.read()
print(res)
'''
'''
file=open('data.text','r')
res=file.readline()
print(res)
'''
#list: we can add, update,change
'''
file=open('data.text','r')
res=file.readlines()
res.pop(1)
print(res)
'''
'''
file=open('data.text','r')
res=file.readlines()
res.insert(2,'reactjs')
print(res)
'''
'''
file=open('data.text','r')
res=file.readlines()
res.sort()
print(res)
'''
#append is used to add one more value end of the list
'''
new_file=open('data.text','w')
new_file.write('python\n')
new_file.write('java/n')
new_file.write('HTML/n')
,,new_file.write('CSS/n')

new_file.close()
'''
'''
new_file=open('data.text','w')
li=['python','css','java','AWS']
for i in li:
    new_file.writelines(i)
    new_files.writelines('\n')

new_file.closed()
'''
'''
import os
os.remove('data.text')
'''
'''

                                                                 18/3/2025
'''                                                 

'''
Generators:Functions
-it is used to generate/interate the values
-when ever user requirement that purpose we are using generators
'''

'''
li=[1,2,3,4,5,6,7,8,9,10]
for i in li:
    print('token:',i)
'''
'''
2 types
#1. infinite generator:n number of tokens we can generate
#2. custom generator: n number of tokens we can generate

,,,

as per today date we generate 10 token , we sale 5 token , remaining 5 tokens we can use tomarrow....now if use generator means we can over come that

now a days bus conductor using machine, before bundle of tickets , now we can use generator generate tickets whwnever customer requirements

that is called as generator
'''

#return:it will take only one value
#      : one function-one return

'''
def gen():
    return'hello'
    return 'hi'
print(gen())           
'''
#yeild=return
#it takes collection of values
#multiple yeild statements
'''
def gen():
    yeild 1
    yeild 2
    yeild 3
print(gen())    
'''
# i just want interate 1 by 1 whwnever user requirement
#inter(gen_fun):it is used to iterate the existing generator object
#next(iter_value):it is used to generate the values
'''
def gen():
    yield 1
    yield 2 
    yield 3
x=gen()
n=iter(x)
print(next(n))
print(next(n))
'''
#generator want return at time , generator return 1 by 1 when ever user
#requirement
'''
def custom():
 for i in range (1,10,1)
  return i 
print(cusyum())
'''
'''
def custom():
      for i in range (1,10,1):
         yield i
print(custom())
'''
'''
def custom():
    for i in range ( 1,10,1):
     yield i
y=custom()
n=inter(y)
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))

'''
''' 
def infinite():
    i=1
    while(i<=10):
        print(i)
        i=i+1
infinite()        
'''
'''
def infinite():
    i=1
    while():
        print(i)
        i=i+1
infinite()        
'''
'''
def infinite():
    i=1
    while(True):
        yield i
        i=i+1
x=infinite()
n=iter(x)
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
'''
'''
                                                 19/3/2025
'''
'''
Threading Functions:
====================
#Threading:functions
#it is used to increase the application performance
# it is used to execute the program parallely
#interpreted programming-execute step by step
#if you have a 10 lines of code it will take 2 sec time
#if you have a 1000 lines of complete applications code it will take more time
#it is used to make faster program


2 Types
#1.Multi level Threading:_Thread=> package only we can achive
#2.Multiple Threading:_Threading=>Package only we can achive

fun A+fun B + fun C
'''
#1.multi level threading
'''
def A():
    print('fun A')
def B():
    print('fun B')
def C():
    print('fun C')
'''
'''
def A():
    print('fun A')
A()    
def B():
    print('fun B')
B()    
def C():
    print('fun C')
C()
'''
#_Thread start_new_thread(function,(arguements))

'''
import _thread

def A(msg):
    print(msg)
    
def B(msg):
    print(msg)
    
def C(msg):
    print(msg)
_thread.start_new_thread(A,('A fun',))    
_thread.start_new_thread(B,('B fun',))   
_thread.start_new_thread(C,('C fun',))   

'''
'''
def A(msg):
    i=1
    while(i<=5):
        print(msg)
        i=i+1
def B(msg):
    i=1
    while(i<=5):
        print(msg)
        i=i+1
def C(msg):
    i=1
    while(i<=5):
        print(msg)
        i=i+1
A('Thread:1')
B('Thread:2')
C('Thread:3')
'''
'''
import _thread
def A(msg):
    i=1
    while(i<=5):
        print(msg)
        i=i+1
def B(msg):
    i=1
    while(i<=5):
        print(msg)
        i=i+1
def C(msg):
    i=1
    while(i<=5):
        print(msg)
        i=i+1
_thread.start_new_thread(A,('Thread:1',))
_thread.start_new_thread(B,('Thread:2',))
_thread.start_new_thread(C,('Thread:3',))
'''
'''
import _thread
import time
def A(msg):
    i=1
    while(i<=5):
        time.sleep(1)
        print(msg)
        i=i+1
def B(msg):
    i=1
    while(i<=5):
        time.sleep(2)
        print(msg)
        i=i+1
def C(msg):
    i=1
    while(i<=5):
        time.sleep(3)
        print(msg)
        i=i+1
_thread.start_new_thread(A,('Thread:1',))
_thread.start_new_thread(B,('Thread:2',))
_thread.start_new_thread(C,('Thread:3',))
'''
'''
#2.multiple threading
-fun main=we can pass multiple arguements
-x=threading.Thread(target=function,args=(Arguements))
x.start()
'''
'''
import time
def main(r,s,msg):
    for i in range(1,r):
        time.sleep(s)
        print(msg)
main(5,2,'Thread-1')        
main(5,1,'Thread-2')
main(5,3,'Thread-3')
'''
'''
import threading
import time
def main(r,s,msg):
    for i in range(1,r):
        time.sleep(s)
        print(msg)
x=threading.Thread(target=main,args=(5,2,'Thread-1',))
x.start()
y=threading.Thread(target=main,args=(5,1,'Thread-2',))
y.start()
z=threading.Thread(target=main,args=(5,3,'Thread-3',))
z.start()
'''
'''
                                                           20/3/2025
'''
'''
Collections
-collections are store multiple elements like lists,sets,tuple,dictionaries
-python provides more data structures that can used as an alternative build in data types tha module name is called collections

4 types
#1. counter
#2.Named Tuple
#3.deque
#4.chainmap

#1.Counter:
============
-it takes input string,list,tuple
-it will count each and every value
-it makes decending order
'''

'''
from collections import Counter
li=[1,2,3,4,5,1,2,35,7,8,9,4,5,7]
res=Counter(li)
print(res)


x=[1,2,3,4,5,1,8,7,4,3,9,10,'hello','good']
res1=Counter(x)
print(res)

y='hello good morning'
res2=Counter(y)
print(res2)
'''

'''
#2. namedtuple:
-namedtuple takes unstructured tuples and dictionaries
-which makes better structure for the data
-it is used to accessing the data
'''

'''
employe={
    "name":'baskar',
    "email":'baskar@',
    "city":'bangalore',
    "mobile":9876543210
    }
from collections import namedtuple
x=namedtuple('employe',['name','email','city','mobile'])
y=x('baskar','baskar@','bangalore',9876543210)             

#keys,index
print(y.name)
print(y[0])
'''

'''
#3.deque:
-deque is choosen over the list when we need faster pop and append
-it is used to make faster program at a time
'''
'''
from collections import deque
li=[1,2,3,4,5,6,7]
x=deque(li)
x.pop()
x.popleft()
print(x)


from collections import deque
li=[1,2,3,4,5,6,7]
x=deque(li)
x.append('hello')
x.appendleft('hi')
print(x)
'''

'''
from collections import deque
li=[1,2,3,4,5,6,7]
x=deque(li)
x.pop()
x.popleft()
#print(x)


#from collections import deque
#li=[1,2,3,4,5,6,7]
#x=deque(li)
x.append('hello')
x.appendleft('hi')
print(x)
'''

'''
#4.chainmap:
-python has a container called chainmap.it combines many dictionaries into a single unit
'''

'''
from collections import ChainMap
d1={'a':'baskar','b':'chinni'}
d2={'c':'bangalore','d':'vizag'}
d3={'e':9876543210,'f':1234567890}
res=ChainMap(d1,d2,d3)
print(res)
print(res.maps)
print(list(res.keys()))
print(list(res.values()))
'''
'''
                                                              21/3/2025

'''
'''
String Methods:
===============
-it is a group of alphanumeric characters
-string should be declare '' or ""
-we cant able to do mathematical calculations

#indexing():we want particular values is called indexing
#positive indexing:consider left to right:starts from 0
#negative indexing:consider right to left:starts from -1
'''

'''
x='Besanttechonology'
print(x[4])

x='Besanttechnology'
print(x[-4])

'''
'''
#slicing():range of values we can use slicing
#str(start:end:step)

'''

#split: it is used to convert string to list

'''
x='hello good morning'
y=x.split()
print(y)
'''

#join():it is used to convert list to string

'''
x='hello good morning'
y=x.split()
z=str.join(' , ',y)
print(z)


x='hello good morning'
y=x.split()
y.pop()
z=str.join(' , ',y)
print(z)
'''



#upper(): it is used to convert lower to upper

'''
x='hello good morning'
y=x.upper()
print(y)
'''



#lower(): it is used to convert the upper to lower

'''
x='HELLO GOOD MORNING'
y=x.lower()
print(y)
'''



#title():every word first letter upper

'''
x='hello good morning'
y=x.title()
print(y)
'''


#capitalize(): first word first letter upper

'''
x='hi good morning'
y=x.capitalize()
print(y)
'''


#Swapcase(): it is used to convert lower to upper , upper to lower

'''
x='Hello Good Morning'
y=x.swapcase()
print(y)
'''

#format()
#format_map()
#it is used to make default templates with different values
#{}

'''
x="my name is {},i am from {}"
y=x.format('baskar','vizag')
y=x.format('chinni','chennai')
print(y)
'''

#format_map(): it is used to make existing dict values

'''
x= "my name is {name[0]}, i am from {city[0]} , state {state[0]}"
d={
    "name":['baskar','chinni','madhu'],
    "city":['vizag','chennai','bangalore'],
    "state":['AP','TN','KA'],
    }
y=x.format_map(d)
print(y)


x= "my name is {name[1]}, i am from {city[1]} , state {state[1]}"
d={
    "name":['baskar','chinni','madhu'],
    "city":['vizag','chennai','bangalore'],
    "state":['AP','TN','KA'],
    }
y=x.format_map(d)
print(y)


x= "my name is {name[2]}, i am from {city[2]} , state {state[2]}"
d={
    "name":['baskar','chinni','madhu'],
    "city":['vizag','chennai','bangalore'],
    "state":['AP','TN','KA'],
    }
y=x.format_map(d)
print(y)

'''

#index(): it consider left to right
#rindex(): it consider right to left
#it is used to find the positions based on the values

'''
x='hello good morning'
y=x.index('o')
print(y)
'''
'''
x='hi good morning'
y=x.rindex('g')
print(y)
'''

#count(): it is used to count the values how many times present in the string

'''
x='hello good morning'
y=x.count('o')
print(y)
'''

#center(): it is used to make center of the string , it will fill remaining values elements
'''
x='hello good morning'
y=x.center(60 , '*')
print(y)


x='hello good morning'
y=x.center(60 , '$')
print(y)
'''

#replace:it is used to replace string values

'''
x='hello good morning'
y=x.replace('hello','hi')
print(y)
'''
'''
                                                                     24/3/2025

'''
'''
#class
- group of functions/group of object is called as class
- inside class describe n no of functions

class class_name:
    group of functions

calling_object()

class         => keyword
class_name    => anything
calling_obj() =>class name
'''

'''
class main:
    print('this is the first class')
main()
'''
'''
class main:
    print('this is the first class')
    def show(self):
        print('this is the show run')
obj=main()
obj.show()
'''
'''
class main:
    print('this is the first class')
    def show(self):
        print('this is the show run')
    def display(self):
        print('this is a display function')
obj=main()
obj.show()
obj.display()
'''
'''
class main:
    print('this is the first class')
    def show(self,a,b):
        print('this is the show fun:', a+b)
    def display(self,x,y,z):
        print('this is a display function:',x+y+z)
obj=main()
obj.show(1,2)
obj.display(1,2,3)
'''

'''
class main:
    print('this is the first class')
    def show(self,a,b):
        print('this is the show fun:', a+b)
    def display(self,x,y,z):
        print('this is a display function:',x+y+z)
    def display(self,a,b,c):
        print('total:',a+b+c)
obj=main()
obj.show(1,2)
obj.display(1,2,3)
'''

#class provides basically constructor function
#it is used to define instance of object/collection of objects
#it will call automatically when we call main class
#__int__=> constructor function

'''
class main:
    print('this is first class')
    def __init__(self):
        print('this is a constructor function')
    def show(self,a,b):
        print('this is a show fun:',a+b)
    def display(self,x,y,z):
        print('this is display fun:',x+y+z)
obj=main()
obj.show(1,2)
obj.display(1,2,3)
'''
'''
class main:
    print('this is first class')
    def __init__(self):
        print('this is a constructor function')
    def __init__(self):
        print('this is a constructor function:1')    
    def show(self,a,b):
        print('this is a show fun:',a+b)
    def display(self,x,y,z):
        print('this is display fun:',x+y+z)
obj=main()
obj.show(1,2)
obj.display(1,2,3)
'''

#main class only we can pass arguements
#main class automatically,this is constructor fun will be triggered

'''
class main:
    print('this is first class')
    def __init__(self,name,email):
        print('this is a constructor function')
        print(name,email)
    def show(self,a,b):
        print('this is a show fun:',a+b)
    def display(self,x,y,z):
        print('this is display fun:',x+y+z)
obj=main('baskar','baskar@')
obj.show(1,2)
obj.display(1,2,3)
'''

'''
#in the presence of constructor function values name,email those information , i just want to push into show fun,display fun
#instance of object describe self only
#self.key=values
#self.a=name
#self.b=email
'''
'''
class main:
    print('this is first class')
    def __init__(self,name,email):
        self.a=name
        self.b=email
        print('this is a constructor function')
        print(name,email)
        print('Name:',self.a)
        print('Email:',self.b)
    def show(self,a,b):
            print('this is a show fun:',a+b)
    def display(self,x,y,z):
            print('this is display fun:',x+y+z)
obj=main('baskar','baskar@')
obj.show(1,2)
obj.display(1,2,3)
'''
'''
class person:
    def __init__(self,name,age,gender):
        self.x=name
        self.y=age
        self.z=gender
    def data(self):
        print('Name:',self.x)
        print('age:',self.y)
        print('gender:',self.z)
    def vote(self):
        if self.y<18:
            print('you are not eligible for vote')
        else:
            print('your eligible for vote')
        
          
a=person('baskar',20,'Male')
a.data()
a.vote()
'''

'''
class employe:
    def __init__(self,id,name,city,mobile):
        self.a=id
        self.b=name
        self.c=city
        self.d=mobile
    def display(self,state):
        print('ID:',self.a)
        print('Name:',self.b)
        print('City:',self.c)
        print('Mobile:',self.d)
x=employe(1,'chinni','vizag',987654321)
x.display('AP')
'''

'''
class employe:
    def __init__(self,id,name,city,*mobile):
        self.a=id
        self.b=name
        self.c=city
        self.d=mobile
    def display(self,state):
        print('ID:',self.a)
        print('Name:',self.b)
        print('City:',self.c)
        print('Mobile:',self.d)
x=employe(1,'chinni','vizag',987654321, 9867543421)
x.display('AP')
'''
'''

                                                         25/3/2025

'''

'''
Inheritance:
-used to one class derived into another class
callback:one function passed into another function as an arguement
callback:only functions
inheritance:only class

Drawbacks:
-parent class derived inside child class
-child class not access parent class

4 Types :
#1.Single inheritance
#2.Multilevel inheritance
#3.Multiple inheritance
#4.Herachical inheritance


#1.Single inheritance: derived inside child class
class A -> class B(A) only one time 


#2.Multilevel inheritance :
class A -> class B(A) -> class C(B) -> class D(C) ...


#3.Multiple inheritance :
class A -> class B -> class C -> class D(A,B,C)
Multiple parents and one child


#4.Herachical inheritance :
class A => class B(A) + class C(A) + class D(A)
one parent and multiple inheritance

'''

#single inheritance:
'''
class A:
    def show(self):
        print('this is a class A')
class B(A): # with the help of B access A
    def show1(self):
        print('this is class B')
obj=B()
obj.show()
obj.show1()
'''

#multiple inheritance:
'''
class A:
    def show(self):
        print('this is class A')
class B(A): #with the help of B access A
    def show1(self):
        print('this is class B')
class C(B): #with the help of c access A,B
    def show2(self):
        print('this is class C')
class D(C): #with the help of D access A,B,C
    def show3(self):
        print('this is class D')
obj=D()
obj.show()
obj.show1()
obj.show2()
obj.show3()
'''


#Multiple inheritance
'''
class A:
    def show(self):
        print('this is class A')
class B: 
    def show1(self):
        print('this is class B')
class C:
    def show2(self):
        print('this is class C')
class D(A,B,C): #with the help of D access A,B,C
    def show3(self):
        print('this is class D')
obj=D()
obj.show()
obj.show1()
obj.show2()
obj.show3()
'''

#Herachical inheritance
'''
class A:
    def show(self):
        print('this is class A')
class B(A): #B is a object access A
    def show1(self):
        print('this is class B')
class C(A): # c is a object access A 
    def show2(self):
        print('this is a class C')
class D(A):
    def show3(self):
        print('this is a class D')
obj=D()
obj.show()
obj.show3()

'''

'''
#super() -> it is used to call the parameters
class student:
    def __init__(self,name,marks):
        self.a=name
        self.b=marks
    def display(self):
        print('Name:',self.a)
        print('Marks:',self.b)
#obj=student('baskar',50)
#obj.display()
class child(student):
    def __init__(self,name,marks,mobile):
        super().__init__(name,marks)
        self.c=mobile
    def contact(self):
        print('Mobile:',self.c)
obj=child('baskar',50,987654321)
obj.display()
obj.contact()
'''

'''

polymorphism:
polymorphism contains two "poly" and "morphs" . poly means many and marphs means shape
-it is used one task performs multiple types

'''

#method overriding:
#different class + same method + different parameters

'''
class perent:
    def show(self,a,b):
        print('total:',a+b)
class child(perent):
    def show(self,x,y,z):
        super().show(x,y)  #x=a,y=b
        print('total:',x+y+z)
obj=child()
obj.show(1,2,3)
'''

#method overload:
#same class + same method + different parameters


'''
class parent:
    def show(self,a,b):
        print('total:',a+b)
    def show(self,x,y,z):
        print('total:',x+y+z)
obj=parent()
obj.show(1,2,3)
'''

#we have the same methods it always overload last one
#that we can over come by using overriding method 


'''

                                                               27/3/2025
'''

'''
Encapsulation:
=> accessible from anywhere , both inside and outside the class
=> encapsulation is the process of hiding the internal data of an object
'''

'''
class public :
    def __init__(self):
        self.x='baskar'
    def display(self):
        print(self.x)
obj=public()
obj.display()
print(obj.x)
'''

'''
=>Decorators: Functions, used to add some more functionalities without distributing exiting functions
#Whatsapp - without distributing existing struction there we need to push some more features is called as decorators

=> Decorator symbol-> @
#Decorator
#Nested Functions
#callback
#parameter & arguements

'''

'''
def main():
     return 'hello good morning'
print(main())
'''

#upper():used to convert lower to upper
#split():used to convert string to list


'''
def dec(x): #call back
    def inner(): #access the parameters
        return x().upper() #callback for main function
    return inner
@dec
def main():
    return 'hello good morning'
print(main())
'''

'''
def dec(x):
    def inner():
        return x().upper()
    return inner
def dec1(y):
    def inner():
        return y().split()
    return inner
@dec1
@dec
def main():
    return 'hello good morning'
print(main())
'''

'''
Data Abstraction :
internal data is hinding , show only functionalities
if any one application backend we cant able to see that is called as Data abstraction

Example: ATM: able to see screen , get cash all
we cant able to see data , process , code how it will work and all
'''

'''
class person:
    def _init_(self,name,age,gender):
        self.x=name
        self.y=age
        self.z=gender
    def data(self):
        print('Name:',self.x)
    def vote(self):
        if self.y<18:
            print('your not eligible for vote...')
            print('Gender:',self.z)
        else:
            print('your eligible for vote....')
            print('Gender:',self.z)
            
from chinni import person
obj=person('bhaskar',10,'Male')
obj.data()
obj.vote()
'''

'''
                                                               28/3/2025

'''
'''
Regular Expression : Regex=re
- It is used to make pattern matching

Operators :
#1.Quantity Operator : +,*,?
                       + : it will take min 1 to max infinite
                         ex:aaaaaaaaaaaaa
                       * : it will take min 0 to max infinite
                        ex:aaaaaaaaaaaaaaa
                       ? : it will take min 0 to max 1
                         ex:a

#2. Group Operators: []
                   :[0-9a-zA-Z]
                   :[0-9a-zA-z]+
                   :Defaultly Quantity ?

#3.Digits: \d
         :\d+
         :[0-9]+
         : it consider only numbers

#4.Words : \w
         : [0-9a-zA-Z]+

#5.Range Operator:{start,end}


#6.Escape Operator : \
                   : it will consider special characters
                   : @,#,$,%.&

'''
'''                
import re
re.compile('pattern')

import re
pattern=re.compile('[a-z]=')
user='12345'

i want to check pattern and user matching or not
#search(): it takes only one value
#findall:it search all the values
         returns as a list
'''
'''
import re
pattern=re.compile('[a-z]')
user='12345'
re=pattern.search(user)
print(res)
'''

'''
import re
pattern=re.compile('[a-z]')
user='Hello good morning'
res=pattern.search(user)
print(res)
'''

'''
import re
pattern=re.compile('[a-z]')
user='Hello all good morning'
res=pattern.findall(user)
print(res)
'''

'''
import re
pattern=re.compile('[a-zA-Z]')
user='Hello all good morning'
res=pattern.findall(user)
print(res)
'''

'''
import re
pattern=re.compile('[\d+]')
user='Hello 27867 good 83626 morning 3262'
res=pattern.findall(user)
print(res)
'''


'''
import re
pattern=re.compile('\w+')
user='Hello 25425 good 377653 morning 263 all'
res=pattern.findall(user)
print(res)
'''

'''
import re
pattern=re.compile('\&+[A-Za-z]+\@+\d+\#+[0-9]+')
user='&Baskar@7582#632832'
res=pattern.findall(user)
print(res)
'''
'''
import re
pattern=re.compile('\#+[a-z]+\%+\d+\&+\@+[0-9]+[a-z]+\$+[0-9]+')
user='#baskar%6578&@86162chinni$5765765'
res=pattern.findall(user)
print(res)
'''

'''

                                                                 1/4/2025

'''
'''
Tkinter: it is also called as a library, framework/modules
-just import it and we can use it

Widgets : we can create user interface
-we can pass n number of functions

1. import tkinter module
2. create root window
3.add widgets
4.start main root
'''
'''
from tkinter import *
from PIL import Image, ImageTk
#pip install pillow

root=Tk() #tool kit
root.title('Whatsapp App')
ico = Image.open('Whatsapp.jpg')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

root.mainloop()
'''

'''
from tkinter import *
from PIL import Image, ImageTk
#pip install pillow

root=Tk() #tool kit
root.title('Whatsapp App')
ico = Image.open('Whatsapp.jpg')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

def red_btn():
    print('I am Red')
def yellow_btn():
    print('I am Yellow')
def blue_btn():
    print('I am Blue')
def lightgreen_btn():
    print('I am Lightgreen')

Button(root,text='submit',command=red_btn,activebackground='orange',activeforeground='brown',bg='red',fg='white',font=('times',20,'bold'),width=15,height=4).grid(row=0,column=0)
Button(root,text='Register',command=yellow_btn,activebackground='orange',activeforeground='brown',bg='yellow',fg='white',font=('times',20,'bold'),width=15,height=4).grid(row=0,column=1)
Button(root,text='login',command=blue_btn,activebackground='orange',activeforeground='brown',bg='blue',fg='white',font=('times',20,'bold'),width=15,height=4).grid(row=1,column=0)
Button(root,text='clear',command=lightgreen_btn,activebackground='orange',activeforeground='brown',bg='lightgreen',fg='white',font=('times',20,'bold'),width=15,height=4).grid(row=1,column=1)

Label(root,text='Welcome Besant Technologies',font=('times',20,'bold')).grid(row=2,column=0)

root.mainloop()
'''

'''

                                                                 2/4/2025

'''
'''
#checkbutton:

'''
'''
from tkinter import *



root=Tk()
checkbutton(root,text='Gender').grid(row=0)
checkbutton(root,text='Male').grid(row=1)
checkbutton(root,text='Female').grid(row=2)

root.mainloop()
'''
'''
#Radiobutton:
from tkinter import *
root=Tk()
Radiobutton(root,text='Gender').grid(row=0)
Radiobutton(root,text='Male').grid(row=1)
Radiobutton(root,text='Female').grid(row=2)

root.mainloop()
'''
#Listbox: it is offer list to the user which user can accept any number of options


'''
from tkinter import *

root=Tk()
Lb=Listbox(root)
Lb.insert(1,'python')
Lb.insert(2,'HTML')
Lb.insert(3,'CSS')
Lb.pack()
root.mainloop()
'''

#Scale: it is used to provide graphical slides , it allows to select values from the
  #sacale
'''
from tkinter import *
root=Tk()
w=Scale(root,from_=0,to=50)
w.grid()
w=Scale(root,from_=0,to=200,orient=HORIZONTAL)
w.grid()

root.mainloop()
'''

#Spinbox: it is an entry of 'ENTRY' widget . values can allow selecting fixed
 #values for the numbers
'''
from tkinter import *
root=Tk()
w=Spinbox(root,from_=-10,to=10)
w.grid()
rootmainloop()
'''
#Messagebox : it is used to create a msgbox


'''
import tkinter
from tkinter import messagebox

root=tkinter.Tk()
root.geometry('150x150')
messagebox.showinfo('information','information for user')
root.mainloop()
'''







































     




















          












































































































































