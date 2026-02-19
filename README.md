"# tatapower202601" 


https://codeshare.io/tatapower



Python is a general-purpose interpreted, interactive, object-oriented, and high-level programming language. 
The creator was very specific that he has to create an easy language, so he removed the concepts of braces and introduced indentations.
It was created by Guido van Rossum during 1985- 1990.
Like Perl, Python source code is also available under the GNU General Public License (GPL).

Initially , python doesn’t get much success because it was slow compared to other languages.
But when people started using it for ML and AI, then it gained momentum.

Install Python
https://www.python.org/downloads/
https://www.python.org/ftp/python/3.14.2/python-3.14.2-amd64.exe

Important:
Check the box “Add Python to PATH” during installation.

Install Visual Studio Code
https://code.visualstudio.com/download

Install the Python Extension in VS Code

Open VS Code
Go to Extensions (left sidebar or press Ctrl+Shift+X)
Search for Python
Install the extension published by Microsoft



Why is Python so Popular?
1) Easy to Learn and Use
2) Mature and Supportive Python Community
3) Support from Renowned Corporate Sponsors
4) Hundreds of Python Libraries and Frameworks
5) Versatility, Efficiency, Reliability
6) Big data, Machine Learning and Cloud Computing
7) Use of python in academics
8) Automation 









Variable
-----------------











str= "Hello Rakuten"
name ="Tufail"
salary = 98000
print(str);
print(str[0]);
print(str[2:5]);
print(salary+2000);	#legal
print("Company name is : "+str);	#legal
print("Heartiest :"+name)
print(" Heartiest :",name)
print("Salary of Rakuten interns are :", salary);
#Hello Rakuten , your intern salary is 98000
print(str, " , your intern salary is ",salary); 

#using f
print(f"{str}  , your intern salary is {salary}");


















Python Identifiers

A Python identifier is a name used to identify a variable, function, class, module, or other object. 

An identifier starts with a letter A to Z or a to z, or an underscore (_) followed by zero or more letters, underscores and digits (0 to 9).
Python does not allow punctuation characters such as @, $, and % within identifiers. Python is a case sensitive programming language

Here are naming conventions for Python identifiers:
Class names start with an uppercase letter. All other identifiers start with a lowercase letter.
Starting an identifier with a single leading underscore indicates that the identifier is private. ( _num )
Starting an identifier with two leading underscores indicates a strongly private identifier. ( __num)
If the identifier also ends with two trailing underscores, the identifier is a language-defined special name. ( __num__ )


Python Keywords - special words in a langauges

And
exec
Not
Assert
finally
or
Break
for
pass
Class
from
print
Continue
global
raise
def
if
return
del
import
try
elif
in
while
else
is
with
except
lambda
yield



Variables and Literals
A variable is a named location used to store data in the memory. 


Here's an example:
Python supports int and float
num1=90
marks=90.8
marks: float = 171.87
num1: int =918
print("num1 is ",num1);
print("marks is ",marks);

num = 5  
Here, num is a variable. We have assigned 5 to variable num

We do not need to define variable type in Python. You can do something like this:

>>> num=5
>>> print("Num=",5)
Num= 5
>>> num="Welcome, Tufail"
>>> print("Num=",num)
Num= Welcome, Tufail


-------


Strings are defined either with a single quote or a double quotes.
mystring = 'tufail'
print(mystring)
mystring = "ahmed"
print(mystring)

Another way : ( we have to import string  from string modules) ** builtin module is by default available. 
import string

mystring = 'tufail'
print(mystring)
mystring = "ahmed"
print(mystring)

num1:int

mystring: string ="mohammad"
print(mystring)




-------

Assignments can be done on more than one variable "simultaneously" on the same line like this

num1:int
num2:int

num1,num2,num3 = 39,433,98

print(num1+num2+num3)


** No difference in the way of declaring num1 and num3

print(type(num1))  # <class 'int'>
print(type(num3))  # <class 'int'>


----

Operators are special symbols that carry out operations on operands (variables and values).
Arithmetic and assignment operators :
Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication etc.
x = 14
y = 4
# Add two operands
print('x + y =', x+y) # Output: x + y = 18
# Subtract right operand from the left
print('x - y =', x-y) # Output: x - y = 10
# Multiply two operands
print('x * y =', x*y) # Output: x * y = 56
# Divide left operand by the right one 
print('x / y =', x/y) # Output: x / y = 3.5


# Floor division (quotient)
print('x // y =', x//y) # Output: x // y = 3

# Remainder of the division of left operand by the right
print('x % y =', x%y) # Output: x % y = 2

# Left operand raised to the power of right (x^y)
print('x ** y =', x**y) # Output: x ** y = 38416


---------------

Assignment operators are used to assign values to variables. You have already seen the use of = operator. Let's try some more assignment operators.

x = 5

# x += 5 ----> x = x + 5
x +=5
print(x) # Output: 10

# x /= 5 ----> x = x / 5
x /= 5
print(x) # Output: 2.0
Run Code
Other commonly used assignment operators: -=, *=, %=, //= and **=.


------------------

Get Input from User
In Python, you can use input() function to take input from user. For example:

inputString = input('Enter a sentence:')
print('The inputted string is:', inputString)

When you run the program, the output will be:

Enter a sentence: Hello there.
The inputted string is: Hello there. 

Another program
name = input("Enter your name : ")
print("Welcome : ",name)


-----------------------

num1 = input("Enter first number")
num2 = input("Enter second number")
result = num1 + num2
print("The result is :"+result)

#converting to int
num1 = input("Enter first number")
num2 = input("Enter second number")
result = int(num1) + int(num2)
print("The result is :",result)


------------------------

There are 3 ways of creating comments in Python.

# This is a comment
  """This is a 
    multiline
    comment."""
  '''This is also a
     multiline
     comment.'''


-----------------------
Hands On 

Create a python program to input name and age of an employee and print the details as follows :

Enter your name : Richard
Enter your age : 21

Richard you are 21 years old.


-----------------------
Type Conversion
The process of converting the value of one data type (integer, string, float, etc.) to another is called type conversion. Python has two types of type conversion.
Implicit Type Conversion
#This is a simple case of Implicit type conversion in Python.
num1 =10
print("num1 is of type :",type(num1))
num2=98.6
print("num2 is of type :",type(num2))

result = num1+num2
print(result)

print("result is of type :",type(result))

Here, num result new has float data type because Python always converts smaller data type to larger data type to avoid the loss of data.



-----------------------

Same variable can hold multiple types of data


num1=100
print('num1 is of type :',type(num1))
num1=100.90
print('num1 is of type :',type(num1))
num1='Richard'
print('num1 is of type :',type(num1))


---------------
Here is an example where Python interpreter cannot implicitly type convert.
num_int = 123     # int type
num_str = "456"   # str type

print(num_int+num_str)

Run Code
When you run the program, you will get

TypeError: unsupported operand type(s) for +: 'int' and 'str'
However, Python has a solution for this type of situation which is know as explicit conversion.


Explicit Conversion

In case of explicit conversion, you convert the datatype of an object to the required data type. We use predefined functions like int(), float(), str() etc. to perform explicit type conversion. For example:

#This is a simple case of Explicit type conversion in Python.
num_int = 123     # int type
num_str = "456"   # str type

num_str= int(num_str)
print(num_int+num_str)

What if string contains “four” as a string ?? 

**will give error



---------------------------------Python Data types----------------------------



Data types in Python

Built-in data types in Python are fundamental data structures provided by the Python programming language. They are pre-defined and available for use without requiring any additional libraries or modules. Python offers several built-in data types, including:

Numeric Data Types: Numeric data types in Python are used to represent numerical values. Python provides three primary numeric data types:

Integer (int): Integers are whole numbers without any decimal points. They can be positive or negative.
Floating-Point (float): Floating-point numbers represent decimal values. They can be positive or negative and may contain a decimal point.

String Data Type(str): Represents a sequence of characters enclosed in single quotes (‘ ‘) or double quotes (” “), such as “Hello, World!”, ‘Python’.

Boolean Data Type(bool): Represents either True or False, used for logical operations and conditions.

Complex (complex): Complex numbers are used to represent numbers with a real and imaginary part. They are written in the form of a + bj, where a is the real part and b is the imaginary part.

Collection Data Types:
list: Represents an ordered and mutable collection of items, enclosed in square brackets ([]).
tuple: Represents an ordered and immutable collection of items, enclosed in parentheses ().
dict: Represents a collection of key-value pairs enclosed in curly braces ({}) with unique keys, mutable












set: Represents an unordered and mutable collection of unique elements, enclosed in curly braces ({}) or using the set() function.


Consumer

consumerName
cost
offPeakUnits
unitsConsumed
peakConsumption
billingMonth
consumerId
contactNumber
	[]
address
	[]
lastDate
billStatus


Python offers a range of compound datatypes often referred to as sequences. 

Lists
A list is created by placing all the items (elements) inside a square bracket [] separated by commas.

It can have any number of items and they may be of different types (integer, float, string etc.)

# empty list
my_list = []

# list of integers
my_list = [1, 2, 3]

# list with mixed data types
my_list = [1, "Hello", 3.4]
print(my_list);


Here's how you can access elements of a list.

language = ["French", "German", "English", "Polish"]

# Accessing first element
print(language[0])


# Accessing fourth element
print(language[3])

You use the index operator [] to access an item in a list. Index starts from 0. So, a list having 10 elements will have index from 0 to 9.

Python also allows negative indexing for its sequences. The index of -1 refers to the last item, -2 to the second last item and so on.


---Deleting an item from list

language = ["French","German","English","Polish"]
print(language[1])

language.__delitem__(1)

print(language[1])


-------------------------------------------


Tuple is similar to a list except you cannot change elements of a tuple once it is defined. Whereas in a list, items can be modified.
Basically, list is mutable whereas tuple is immutable.
language = ("French", "German", "English", "Polish")
print(language)
You can also use tuple() function to create tuples.
You can access elements of a tuple in a similar way like a list.

language = ("French", "German", "English", "Polish")
print(language[1]) #Output: German
print(language[3]) #Output: Polish
print(language[-1]) # Output: Polish

You cannot delete elements of a tuple, however, you can entirely delete a tuple itself using del operator.
language = ("French", "German", "English", "Polish")
del language
# NameError: name 'language' is not defined
print(language)



----------------------------

Python Control Flow
if...else Statement
The if...else statement is used if you want perform different action (run different code) on different condition. For example:

num = -1

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
    
# Output: Negative number



Taking input and performing if else 

num1 = int(input('Enter a number: ‘))	# converting to int to perform comparison
if num1 > 80:
    print("You passed the test")
else:
    print("You need to reappear for the test")




Like most programming languages, while loop is used to iterate over a block of code as long as the test expression (condition) is true. Here is an example to find the sum of natural numbers:
In Python, the increment operator is not supported as a standalone operator (++)

n=1
while n<=5:
    print(n, " Hi")
    n = n + 1

For Loop

#For Loop in Python

for i in range(1,5):
    print(i, " ", end="")





break




pip install python-docx




Reading from docx file - word file


from docx import Document

doc = Document("h:\\hello.docx")

for para in doc.paragraphs:
    print(para.text)
































