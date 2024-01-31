'''=========================functions in python===================================
abs(),aiter(),all(),anext(),any(),ascii(),
bin(),bool(),breakpoint(),bytearray(),bytes(),
callable(),chr(),classmethod(),cmpile(),complex(),
delattr(),dict(),dir(),divmod(),
enumeate(),eval(),exec(),
filter(),float(),format(),frozenset(),
getattr(),globals(),
hasatttr(),hash(),hex()
id(),input(),int(),isinstance(),issubclass(),iter()
len(),list(),locals(),
map(),max(),memoryview,min(),
next(),
object(),oct(),open(),ord()
pow(),print(),property()
range(),repr(),reversed(),round(),
set(),setattr(),slice(),sorted(),staticmethod(),str(),sum(),super(),
tuple(),type(),
vars(),
zip(),
_import_()

===============================string methods=================
capitalize(),casefold(),center(),count(),
encode(),endswith(),expandtabs(),
find(),format(),format_map(),
index(),isalnum(),isalpha(),isascii(),isdecimal(),isdigit(),isidentifier(),islower(),isnumeric(),isprintable(),isspace(),istitle(),issupper(),
join(),
ljust(),lower(),lstrip(),maketrans(),partition(),replace(),rfind(),rindex(),rjust(),rpartition(),rsplit(),rstrip(),
split(),splitlines(),startswidth(),strip(),swapcase(),
title(),translate(),upper(),zfill()

============================data types============================
numeric---int,float,complex,
text/string
boolean--true/false.

====================operators==================================
----------------arithmetic--------------------
+,-,/,*,
----------------assignment operators--------------------
=,+=,-=,/=,*=

===================Dates======================
uses:backup file,condition,metric
# from datetime import date
# date.today()

==================================datatype conversion==============================
str()
'''

print("hello world!".title())
#help()
#===============working with integers
x=5
print(type(x))
#=============working with float numbers
m=3.3
print(type(m))

#===================working with text
y="Gideon"
print(type(y))

#=============working with boolean
q=True
print(type(q))

#===========Getting text from the console
name= input("Entr your Name:")
print(name.title())


#=============Getting integer from the console
age= int(input("Enter your age:"))
print(age)


#================converting integers to string
r=22
print("This is a number " + str(r))



#building a calculator in python
FirstNumber=int(input("Enter the first number: "))
SecondNumber=int(input("Enter the second number: "))
print('The sum is ', FirstNumber + SecondNumber)

