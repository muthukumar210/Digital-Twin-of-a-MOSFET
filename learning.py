#import stdlib_list
#print a variable of any type
x = "muthu"
print(x)
print()

a = 13
#type(a)

#to get input integer from user
b = int (input())
print(b)
print()

#to get input string from user
c = input()
print(c)
print()

#to get input float from user
i = float ( input () )
print(i)
print()

'''print 
my 
name 
as 
muthu
kumar
and 
i 
am 
learning
python'''

print("the breadth of the rectangle is :",b)
print("the number is :",b,end=' ')
print("the value is :",a)
print("i am learning python",b,"tomorrow there is a drive")
print()

#indexing of String
name = "muthukumar"
print(name[-1])
print()

#change char by index in string
#name[0] = "k"
#this is not possible since strings are immutable

#Exponent of an integer or float
print(b**i)
print(2**3)
print()

#if condtions
if(a==10):
    print("a is 10")
print()

#if-else conditions
if(a==10 or a==11 or a==12):
    print("a is 10 or 11 or 12")
else:
    print("a is not 10 or 11 or 12")
print()

#if-elif-else conditions
if(a==10):
    print("a is 10")
elif(a==11):
    print("a is 11")
elif(a==12):
    print("a is 12")
else:
    print("a is none of those")
print()

#Loops
#for loop
for x in range(0,11):
    print(x)
for x in range (11):
    print(x)
print()

#while loop
while(a>13):
    print(a)
print()

#problem for printing odd numbers
w = 1
while(w<10):
    print(w)
    w = w+2
print()

#String Manipulation
#character parsing a string and print each character
v = "muthukumar"
for x in v:
    print(x)
print(len(v))
print()

#String concatenation
m = x+v
print(m)

#String duplication
print(m*3)
print()

#in and not in String
print("muthu" in v)
print("var" in v)
print("var" not in v)
print()

#ASCII value
print(chr(65))
print(ord("B"))
print()

#String slicing
u = "Happy Morning"
print(len(u))
print(u[::-1])
r = u[::-1]
print(r[0:7])

#String in-built functions
print(u.islower())
print(u.isupper())
print(u.isdigit())
q = u.isdigit()
print(not(q))
print(u.isalnum())
print(u.upper())
print()

#Lists
#there can be any type of data in a list
#similar to an array but with diff datatypes
l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
t = "abcdefghijklmnopqrstuvwxyzabcd"
print(list(t))
l[0] = 10
print(l)
print(l[0:5])
print()

f,z = 0,5
while(f<=25 and z<=30):
    print(l[f:z])
    f = f+5
    z = z+5
print()

#sort a list
o = [45,47,89,546,21,54,32,465,5,43]
o.sort()
print(o)
#to sort in descending order
o.sort(reverse=True)
print(o)
print()

#getting list input
k = []
j = int(input())
for x in range(0,j):
    e = int(input())
    k.append(e)
print(k)
#find index of an value in an list
print(k.index(1))
print()
#insert a element
k.insert(3,29)
print(k)
print()
#reverse list
k.reverse()
print(k)

