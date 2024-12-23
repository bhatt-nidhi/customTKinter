# def name():
#     print("nidhi")
# name()
from logging import exception

# parameter name same as fun name
# def name(name):
#     print("your name is :" +name)
# name("abc")


# lst = ()
# def ar(*you):
#     for a in you:
#         print(a)
#         lst.insert(a)
#         print(lst)
# ar(input("enter names : "))

# def addition(a,b):
#     sum=a+b
#     print("the sum is : ", sum)
# addition(7,7)

# a=int(input("enter number : "))
# b=int(input("enter number : "))
# def cal(a,b):
#     sum=a+b
#     print(sum)
# cal(a,b)

# def sqr(a):
#     num=a*a
#     return num
# final=sqr(7)
# print("square is ", final)

# defualt arguement

# def sqr(a,b=10):
#     num=a*a
#     sum=b*b
#     return num,sum
# final=sqr(7)
# print("square is ", final)

# def details(name,surname,age=10):
#     print(name,surname,age)
# details("abc","shah")

# def details(name,surname,age=10):
#     print(name,surname,age)
# details("abc","shah",20)
#


# def flowers(name,color,smell):
#     print(color,smell,name)
# flowers(smell="good",color="red",name="rose")

# def name(*n):
#     for i in n:
#         print(i)
# name(input("enter names: "))


#========================================================================================


# 1. Write a Python function to find the maximum of three numbers.

# def max(num1,num2,num3):
#     print(num1,num2,num3)
#     if num1>=num2:
#         if num1>num3:
#             print(f"num {num1} is big")
#         else:
#             print(f"number {num3} is big")
#     else:
#         if num2>num3:
#             print(f"number {num2} is big")
#         else:
#             print(f" {num3} is big")
# max(2,3,6)
#==========================================================================================
# 2) Write a Python function to sum all the numbers in a list.

# def summ(*num):
#     print(num)
#     total = 0
#     for i in num:
#         total+=i
#     return total
# final=summ(10,10,20,30)
# print(final)

#=================================================================================================
# 3)  Write a Python function to multiply all the numbers in a list.

# def mul(*num):
#     print(num)
#     temp = 1
#     for a in num:
#         temp*=a
#     return temp
# number=mul(10,10,10)
# print(number)

#4 Write a Python program to reverse a string.
#
# def rev(str):
#     print(str[::-1])
# rev("heyy7657")


#=============================================================================================
#5. Write a Python function to calculate the factorial of a number (a non-negative integer).
#The function accepts the number as an argument.

# def fact(num):
#     if num==0 or num<0: # necessary condition or else it will run ifinite 0,-1,-2...etc .
#         return 1
#     else:
#         return num*fact(num-1)
# ans=int(input("enter number : "))
# print(fact(ans))

#================================================================================================
#6  Write a Python function to check whether a number falls within a given range.
#
# def check_range(num):
#     if num in range(1,10):
#         print("it is in range ")
#     else:
#         print("it is out of range")
# user=int(input("enter numbers: "))
# check_range(user)
# ========================================================================================
# def check_range(num):
#     if num in range(1,10,2): # 1,3,5,7,9 in is range rest of the out of range.
#         print("it is in range ")
#     else:
#         print("it is out of range")
# check_range(8)

#==============================================================================================
#7. Write a Python function that accepts a string and counts the number of upper and lower case letters.

# def case(str):
#     print(str)
#     upper=[]
#     lower=[]
#     up=[c for c in str if c.isupper()]
#     upper.append(up)
#     print(upper)
#     low=[l for l in str if l.islower()]
#     lower.append(low)
#     print(lower)
# ans=input("enter string: ")
# case(ans)
#===========================================================================================
#
# def case(str):
#     lower=[]
#     upper=[]
#     print(str)
#     for i in str:
#         if i.isupper():
#             upper.append(i)
#         else:
#             lower.append(i)
#     print(upper)
#     print(lower)
# user=input("enter a string : ")
# case(user)

#=============================================================================================
#8. Write a Python function that takes a list and returns a new list with distinct elements from
# the first list.


# def distinct(str):
#     lst = []
#     for i in str:
#         if i not in lst:
#             lst.append(i)
#     print(lst)
# str=input("enter the string : ").split(",")
# distinct(str)
#

#===================================================================================
#9. Write a Python function that takes a number as a parameter and checks whether the number is prime or not.

# def prime(num):
#     if num==0 or num==1:
#         return 0
#     for i in range(2,num):
#         if num%i==0:
#             print(f"the number {num} is not prime")
#             break
#     else:
#         print(f"the number {num} is  prime")
# user=int(input("enter number: "))
#prime(user)
# prime(9)

#=================================================================================================
#10)  Write a Python program to print the even numbers from a given list.
# evennum=[]
# def even(*num):
#     for i in num:
#         if i%2==0:
#             evennum.append(i)
#     print(evennum)
#
# user=input("enter numbers : ").split(" ")
# user=[int(x) for x in user]
# even(*user)

# even(7,9,4,6,2)

#12. Write a Python function that checks whether a passed string is a palindrome or not.

# def palindrome(str):
#     str=str.casefold()
#     if str==str[::-1]:
#         print("string is palindrome")
#     else:
#         print("not palindrome")
# str=input("enter string: ")
# palindrome(str)


#16. Write a Python function to create and print a list
# where the values are the squares of numbers between 1 and 30 (both included).

# def sqr():
#     for i in range(1,31):
#         print(i**2 , end="  ")
# sqr()



a=input("enter the value: ")
while(True):
    try:
        a=int(a)
    except ValueError:
            a=input("enter the valid number: ")
            break
print()

