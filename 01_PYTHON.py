# # #VARIABLES :

# a='''Abhishek is a
# good boy
# '''
# b= 345
# c= 45.45
# d=False
# e=None

# #printing the variable
# print(a)
# print(b)
# print(c)
# print(d)
# #printing the type of variable 
# print(type(d))
# print(type(a))

# #OPERATORS :

a=3
b=4

#Arithmetic operators
print("the value of 3+4 is " , 3+4)
print("the value of 3-4 is " , 3-4)
print("the value of 3*4 is " , 3*4)
print("the value of 3/4 is " , 3/4)
#Assignment operators
a=34
a+=2
print(a)
a=34
a-=2
print(a)
a=34
a*=2
print(a)
a=34
a/=2
print(a)
#Camparison operator
b=(5>7)
print(b)
b=(14>7)
print(b)
b=(5<=4)
print(b)
b=(56<=4)
print(b)
b=(56==4)
print(b)
b=(56!=4)
print(b)
#logical operators
bool1 = True
bool2 = False
print("The value of bool1 and bool2 is ", (bool1 and bool2))
print("The value of bool1 or bool2 is ", (bool1 or bool2))
print("The value of bool1 not bool2 is ", (not bool2))


# #TYPE CASTING :

# a="3434"
# a=int(a)
# print(type(a))
# print(a + 345)

# #INPUT FUNCTION :

# a = input("enter any name: ")
# a = str(a)
# print(a, "hirani")
# b = input("enter any number: ")
# b = int(b)#convert a is an integer (if possible)
# print((b + 59),(type(b)))

# #STRINGS :

# a = 34
# b= '''Abhishek"s is a good boy and 
#               abhishek's is a good person'''
# print(a , b)
# print(type(a))
# print(type(b))
# # a= 34
# # b= '''Abhishek's 
# #     is a good boy'''
# # print(a,b)
# # print(type(a))
# # print(type(b))

# #STRINGS SLICING :

# greeting = "good morning, "
# Name = "ABHISHEKISGOOD"
# # Concatinating two strings 
# # c= greeting + Name 
# # print(c)
# #Name = "Abhishek"
# # print(Name[1:4])
# #name[4]="Abhishek" ----> Does not work 
# #print(Name[-4] )#is same as name [1:5]
# # Name = "Abhishekisagoodboy"
# #c=Name[-4:-1] # is same is name [1:4]
# # c=Name[1:7]
# # print(c)
# # print(Name[0:4]) # is same as [0:4]
# # print(Name[-1]) # is same as [1:8]
# c= Name[0:10:2] #  is same as opposite [4:1]and it less then the last value of colen
# print (c)

# # ESCAPE SEQUENCE CHARACTER :

# story = "Abhishek is a youtuber.\nHe\tis a good person"# (\n) is used for new line...
# print(story)
# # hello="abhishek is a good boy. as well is a go\od person"
# # print(hello)
# # if we need a back slash then we type (\\)double blaslash then we get a single backslash (\)

# # LIST :

# # Create the list using []
# a = [1 , 2 , 3 ,4 , 5]

# # Print the list using print() function

# # Access using index using a[0] , a[2] , a[3]
# print(a[2])
# a[0] = 98
# a[1] = 99
# a[2] = 100
# a[3] = 101
# a[4] = 102
# print(a)
# # We can create a different types of list
# c = [1 , "Abhishek" , 0.1 , False]
# print(c)

# # LIST SLICING :

# friends=["Harry" , "Abhishek" , "Rohan" , "Prachi" , "Ishu" , 45]
# print(friends[-4:])

# #LIST METHORD

# #Case 1 for list ascending order 
# l1 = [1 , 8, 7, 2, 21, 15]
# l1.sort() #in this case sort defines the ascending order of the list . 
# print(l1)
# #Case 2 for list in ascending order 
# l1= [1 , 8, 7, 2, 21, 15]
# print(l1)
# l1.sort   ()
# print(l1)
# #Case 3 for list in Reverse
# l1 = [1 , 8, 7, 2, 21, 15]
# l1.reverse()
# print(l1)
# #Case 4 for list in Append (add in the end of the list)
# l1 = [1 , 8, 7, 2, 21, 15]
# l1.append(45)
# print(l1)
# #Case 5 for list in Insert (It inserts the no. in the position of the list )
# l1 = [1 , 8, 7, 2, 21, 15]
# l1.insert(1, 456)
# print(l1)
# #Case 6 for list in POP (It will  delete the elements in the list in the ends)
# l1 = [1 , 8, 7, 2, 21, 15]
# l1.pop()
# print(l1)
# #Case 7 for list in POP (It will delete the elements in the position of the elements)
# l1 = [1 , 8, 7, 2, 21, 15]
# l1.pop(1)
# print(l1)
# #Case 8 for list in Remove (It will also delete the elements in the list but in this methord we cant defines the position of the elememts)
# l1 = [1 , 8, 7, 2, 21, 15]
# l1.remove(21)
# print(l1)

#TUPLES : (IMPORTANT: (,)is used in the tuple)

#Creating a tuple using ()
# t = (1, 2, 3, 4, 5)

# #Printing the elements of the tuple:
# print(t[0])

# #Can't update the value of the tuple
# #t[0] = 34 #(TypeError: 'tuple' object does not support item assignment)THROUGH AN ERROR

# #Empty Tuple
# t1 = ()
# print(t1)
# t2 = (1)
# print(t2) # Wrong way to declare the Tuple with single elements 

# #TUPLES METHORDS :
# t = (1, 2, 3, 4, 5 , 1 , 1 )
# print(t.count(1)) # COUNTS IN TUPLES indicates the value how much value will come on the Tuple
# print(t.index(1)) # INDEX IN TUPLES it helps to search the index place in the Tuple 

#QUESTION PYTHON PRACTICE SET :

# f1 = input("ENTER FRUIT NAME 1")
# f2 = input("ENTER FRUIT NAME 2")
# f3 = input("ENTER FRUIT NAME 3")
# f4 = input("ENTER FRUIT NAME 4")
# f5 = input("ENTER FRUIT NAME 5")
# f6 = input("ENTER FRUIT NAME 6")
# f7 = input("ENTER FRUIT NAME 7")
# myfruitlist = [f1 , f2 , f3 , f4 , f5 , f6 , f7]
# print(myfruitlist)

# M1 = int(input("ENTER MARKS FOR STUDENT NUMBER 1"))
# M2 = int(input("ENTER MARKS FOR STUDENT NUMBER 2"))
# M3 = int(input("ENTER MARKS FOR STUDENT NUMBER 3"))
# M4 = int(input("ENTER MARKS FOR STUDENT NUMBER 4"))
# M5 = int(input("ENTER MARKS FOR STUDENT NUMBER 5"))
# M6 = int(input("ENTER MARKS FOR STUDENT NUMBER 6"))
# M7 = int(input("ENTER MARKS FOR STUDENT NUMBER 7"))
# mylist=[M1 , M2 , M3 , M4 , M5 , M6 , M7]
# mylist.sort()
# print(mylist)

# t = (1, 2, 3, 4, 5)
# t[0]=34
# print(t) #'tuple' object does not support item assignment

# a=[2 , 4 , 56 , 43 ]
# print(a[0] + a[1] + a[2] + a[3]) #methord 1
# print(sum(a)) #methord2

# a= [7, 0, 8, 0, 0, 9]
# count = a.count(0)
# print(count)

# # DICTIONARY(It is the collection of key and values ) SYNTAX IN  PYTHON : #(While using dictionary it is complsury to use (comma))

# myDict = {
#     "fast" : "IN A QUICK MANNER",
#     "Abhishek" : "A Coder",
#     "Marks" : [1 ,2, 3, 4, 5] ,
# }
# print(myDict['fast'])


#  #NEXTED DICTIONARY :

# myDict ={
#  "fast" : "IN A QUICK MANNER",
#     "Abhishek" : "A Coder",
#     "Marks" : [1 ,2, 3, 4, 5] ,
#  "anotherdict" : {'Abhishek' : 'player'}
# }
# print(myDict['fast'])
# print(myDict['anotherdict']['Abhishek'])

# HOW TO CHANGE THE VALUE OF THE MARKS :

# myDict ={
#  "fast" : "IN A QUICK MANNER",
#     "Abhishek" : "A Coder",
#     "Marks" : [1 ,2, 3, 4, 5] ,
#  "anotherdict" : {'Abhishek' : 'player'}
# }
# myDict['Marks'] = [24 , 57,]
# print(myDict['Marks'])
# print(myDict['anotherdict']['Abhishek'])


# DICTIONARY METHORDS : 

# myDict ={
#  "fast" : "IN A QUICK MANNER",
#     "Abhishek" : "A Coder",
#     "Marks" : [1 ,2, 3, 4, 5] ,
#  "anotherdict" : {'Abhishek' : 'player'}
# }

# #METHORD FIRST (in this methords we can also do typecasting )
# print(list(myDict.keys())) # it gives all the keys in the list ex: fast , Abhishek , Marks , anotherdict etc......
# #METHORD SECOND
# print(myDict.values()) # it gives all the values of the dictionary ex : In A QUICK MANNER , A CODER etc....
# #METHORD THIRD
# print(myDict.items()) # it gives the tuples in the dictionary means = it gives keys + values ..........
# #METHORD FOURTH # if we wanna add something in the dictionary 
# print(myDict)
# updateDict= {
#     "Lovish" : "My Good Friend",
#     "Abhishek":  "THE HACKER",
# }
# myDict.update(updateDict)
# print(myDict)
# #METHORD FIFTH # diffrence between .get and [] syntax in Dictionaries
# print(myDict.get("Abhishek"))   # Returns None as (Abhishek2) is not present in the dictionary
# print(myDict["Abhishek"]) # throws an error as (Abhishek2) is not present in the dictionary

# # SET IN PYTHON :

# a = {1, 2 , 3 , 4 , 1}
# print(type(a)) # type = set 
# print(a)
# print(type(a))
# # IMPORTANT : This Syntax will create an empty dictionary and not an  empty set .....
# b={}
# print(type(b))
# #METHORDS OF EMPTY SET :

# # An empty set can be created  using the below syntax:
# c=set()
# print(type(c))
# # METHORDS OF SETS : 
# #METHORDS 1
# c.add(4)
# #c.add([6 , 7 , 8 , 9 , 10 ])#we cant add list in the python because list cant bhe hasable type of error (because can be changable)
# c.add((6 , 7 , 8 , 9 , 10 ))# we can add tuple in set 
# #c.add({3:7})#we cant add dictionary in the of set 
# print(c)
# print(len(c)) #prints the lenght of this set 

# c.remove(4)#it remove the elements in the sets 
# print(c)
# print(c.pop())#its randomly remove the elements in the set 

# #PRACTISE SET 06 : .............

# myDict={
#     "pankha" : "fan",
#     "dabba" :  "box",
#     "vastu" : "item",
# }
# print("option are " , myDict.keys())
# a=input("enter the hindi words\n")
# print("the meaning of your word is \n" ,myDict.get(a))

# num1=int(input("Enter your first no1,"))
# num2=int(input("Enter your first no2,"))
# num3=int(input("Enter your first no3,"))
# num4=int(input("Enter your first no4,"))
# num5=int(input("Enter your first no5,"))
# num6=int(input("Enter your first no6,"))
# num7=int(input("Enter your first no7,"))
# num8=int(input("Enter your first no8,"))
# s = {num1 , num2 , num3 , num4 , num5 , num6 , num7 , num8}
# print(s) # we know that in set all unique no. will come in the set 

# s={18 , "18"}#this set is print because as we know that set have unique no soo both are diffrent 
# print(s)

# s=set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# print(len(s))

# favlang ={}
# a=input("enter your favorite language hiten")
# b=input("enter your favorite language ishika")
# c=input("enter your favorite language mayuri")
# d=input("enter your favorite language tarun")
# favlang["hiten"] = a
# favlang["ishika"] = b
# favlang["mayuri"] = c
# favlang["tarun"] = d
# print(favlang)

# CONDITIONAL IN PYTHON : ..............

#IF , ELSE , ELIF LADDER IN  PYTHON : 

# a=47
# if(a>8):
#     print("the value of a greater then 8")
# elif(a>9):
#     print("the value of a greater then 9")
# else:
#     print("a is not greater then 8 or 9 ")

#MULTIPLE IF STATEMENTS : (then all if statements have its own value in the python they dont interfair each of them)
# a=47
# if(a>8):
#     print("the value of a greater then 8")
# if(a>9):
#     print("the value of a greater then 9")
# if(a>10):
#     print("the value of a greater then 10")
# else:
#     print("a is not greater then 8 or 9 ")
    
# QUESTION 1 : 

# a=22
# if(a>9):
#     print("greter")
# else:
#     print("lesser")

# QUESTION 2 : 

# a=int(input("ENTER YOUR AGE"))
# if(a>=18):
#     print("yes")
# else:
#     print("you are above 18 you cant fill this")

# RELATIONAL OPERATORS :
# WE CAN USE THIS (IF) STATEMENTS FOR DIFFERENT DIFFERENT CONDITIONS 
# (==) -> equals # Single equal(=) defines that it assign the values & while double equals (==) defines that it is equal to any number
# (>=) -> greater/equals 
# (<=) -> ,etc

# LOGICAL OPERATORS :
# AND (True if both operators are true else false)
# age=int(input("enter your age"))
# if(age>45) and (age>66):
#     print("you can fill this form ")
# else:
#     print("you cant fill this form ")

# OR(True if any one operator is true else false )
# age=int(input("enter your age"))
# if(age>45) or (age>66):
#     print("you can fill this form ")
# else:
#     print("you cant fill this form ")

# NOT (it inverts the condition if condition is true then if changes into false if false then it changes into true )

#  (in) & (is) statement : ............
# is operator see the first storing value in the if condition if it has then it gives true either it gives false 
# a = None
# if(a is None):
#     print("it is true ")
# else:
#     print("it is not true")

# in operator check the list if the number in the list then it gives true either it gives false 
# a=[2, 3, 4, 5]
# print(2 in a)
# it gives true because 2 is the list 

# QUESTION 1 
# WRITE A PYTHON PROGRAM TO FIND THE GREATEST OF FOUR NO. ENTER BY THE USER ?
# num1=int(input("enter the number 1\n"))
# num2=int(input("enter the number 2\n"))
# num3=int(input("enter the number 3\n"))
# num4=int(input("enter the number 4\n"))
# if(num1>num4):
#     f1 = num1
# else:
#     f1 = num4

# if(num2>num3):
#     f2 = num2
# else:
#     f2=num3

# if(f1>f2):
#     print(str(f1) + "it is greater")
# else:
#     print(str(f2) + "it is greater")

# QUESTION 2 ?
# write a programe to find out a wheater student is pass or fail ,if it requires 40%  and atleast 33%and each subject to pass . assume 3 subjects and take marks as an input from the user ?
# sub1=int(input("enter your sub1 marks "))
# sub2=int(input("enter your sub2 marks "))
# sub3=int(input("enter your sub3 marks "))
# if(sub1<33 or sub2<33 or sub3<33):
#     print("you are fail in class 12th")

# elif (sub1 + sub2 + sub3)/3 <40:
#     print("you are fail because of less percentage in class 12TH ")
# else:
#     print("CONGRATULATION YOU ARE PASS IN CLASS 12TH")

# QUESTION 3 ?

# text=input("enter the text")
# spam = False

# if("make a lot of money " in text):
#     spam=True
# elif("Watch This" in text):
#     spam=True
# elif("click this " in text):
#     spam = True
# elif("subscribe this  " in text):
#     spam = True
# else:
#     spam = False

# if(spam):
#     print("this text is spam ")
# else:
#     print("this text is not spam ")

# # QUESTION 4?
# # WRITE A PROGRAM TO FIND WHEATHER A GIVEN USERNAME CONTAIN LESS THAN 10 CHARACTER OR NOT ?

# a=input("enter the username ")
# if(len(a)<10):
#     print("no cant do anything ")
# else:
#     print("nothing") 
# WRITE A PYTHON PROGRAM WHICH FINDS OUT WHEATHER A GIVEN NAME IS PRESENT IN THE LIST OR NOT ?
# names=["abhishek" , "harry" , "hiten"]
# name=input("enter the name to check\n")
# if name in names:
#     print("you are present in the list")
# else:
#     print("your name is not present in the list")

# english=int(input("enter your english marks\n"))
# hindi =int(input("enter your hindi marks\n"))
# maths =int(input("enter your maths marks\n"))
# computer=int(input("enter your computer marks\n"))
# science =int(input("enter your science marks\n"))

# percentage=(english + hindi + maths + computer + science )/5
# print(percentage)
# if(percentage>=90):
#     print("excellent result")
# elif percentage<90 and percentage>79:
#     print("fair result")
# elif percentage<80:
#     print("try to work hard")   
# else:
#     print("focus on your studies you are fail")

# Question 6 ?
# write a program to find out a wheather a given post is talking about "string" or not ?
# post=("harry")
# p=post.casefold() # casefold = (it compares all the strings in the same way )
# name=input("enter your name\n")
# if(post in name.casefold()):
#     print("yes your string is present")
# else:
#     print("not prsent")



# LOOPS :................

# primary there are two types of loops in python 
# 1. while
# 2. for 

#WRITE A PROGRAM TO PRINT 1 TO 50 USING A WHILE LOOP ?

# i =0
# while i<5:
#     print("harry")
#     i=1+i

#WRITE A PROGRAM TO PRINT THE CONTENT OF A LIST USING WHILE LOOPS ?
# fruits =['apple' , 'mango' , 'banana' , 'grapes']
# i=0
# while i<len(fruits): 
#     print(fruits[i])
#     i=i+1

# WRITE A PROGRAM TO PRINT THE CONTENT OF A LIST USING FOR LOOPS ?
# fruits =['apple' , 'mango' , 'banana' , 'grapes']
# i=0
# for items in fruits:
#     print(items)
#     i=i+1

# RANGE FUNTION IN FOR LOOPS : ----------

# for i in range(8):#(where i start , where i stop , how many digits skip)
#     print(i)

# for i in range(0,8):#(where i start , where i stop , how many digits skip)
#     print(i)

# for i in range(1,8,2):#(where i start , where i stop , how many digits skip)
#     print(i)

# FOR LOOP WITH ELSE :------

# for i in range (1 , 10 , 3):
#     print(i)
# else:
#     print   ("this is inside else for ")

# FOR LOOP WITH ELSE : ---------
# l = [1 , 7 , 8 ]
# for items in l: 
#     print(items)
# else:
#     ("done")

# BREAK STATEMENT FOR LOOPS :------(in this statements break loops breakes the code )
# #condition 1
# for i in range (10): 
#     print(i)
#     if i==6:
#         break
# #condition 2
# for i in range (1,10): 
#     print(i)
#     if i==8:
#         break 
# #condition 3 
# for i in range (1,10,5): 
#     print(i)
#     if i==9:
#         break

# CONTINUE STATEMENT IN PYTHON : ------
# for i in range (10):
#    if i==5:
#     continue # continue statement cant print the value of 5 it skips the 5 
#    print(i)

# PASS STATEMENT IN PYTHON : --------
# pass is the null statement in python (it instructs "DO NOTHING")
# l =[1 , 3 , 4 , 5]
# for items in l:
#   print(items)
#   pass


# PRACTICE SET OF LOOPS : -----
# QUESTION 1 
# WRITE A PROGRAM TO PRINT  MULTIPLICATION TABLE OF A GIVEN NUMBER USING FOR LOOPS ?
# num=int(input("enter the number"))
# for i in range (1,11):
#     print(num ,"X" , i , "=" , num*i)

# F STRING : -------
# num=int(input("enter the number"))
# for i in range(1,11):
#     print(f"{num}X{i}={num*i}")
# QUESTION 2 ?
# l1=[input("enter you name") ]
# for name in l1:
#     k=name.casefold()
#     if k.startswith("s"):
#         print("hello" + name)
#     else:
#         print("you are not in the list")


# WRITE A PROGRAM TO FIND WHEATHER A GIVEN NUMBER IS PRIME OR NOT ?
# num=int(input("enter the number"))
# prime=True

# for i in range(2,num):
#     if(num%i ==0):
#         prime=False
#         break
# if prime:
#     print("this number is prime")
# else:
#     print("this number is not prime ")

#    &

# count = 0
# num = int(input("Enter your number: "))
# for i in range(1, num + 1):
#     if num % i == 0:
#         count = count + 1
# if count == 2:
#     print("Prime number")
# else:
#     print("Not Prime number")

# WRITE A PROGRAM TO FIND THE SUM OF FIRST N NATURAL NUMBER USING WHILE LOOP?
# num1=int(input("enter the number"))
# i=1
# while i<=num1:
#     print(i)
#     i=1+i

# WRITE A PROGRAM TO CALCULATE THE FACTORIAL OF A GIVEN NUMBER USING FOR LOOP ?
# num1=int(input("enter the number: "))
# factorial = 1
# for i in range(1 ,num1+1):
#     factorial=factorial*i
#     print(f"THE FACTORIAL OF THIS NUMBER IS {factorial}")

# WRITE A PROGRAM TO PRINT THE FOLLOWING STAR PATTERN ? for n=3
#    *
#  * * *
# * * * * *
# n = 3

# for i in range (3):
#     print(" " * (n-i-1), end="")
#     print("*" *(2*i+1) , end="")
#     print(" "  * (n-i-1))       

# WRITE A PYTHON PROGRAM TO PRINT MULTIPLICATION TABLE OF N USING LOOP IN REVERSE ORDER?
# num=int(input("enter the number"))
# for i in range (10,0,-1):
#     print(num ,"X" , i , "=" , num*i)


# FUNCTIONS IN PYTHON: -------------

# SUM FUNCTION IN PYTHON (sum is a declare function in python who )
# Marks=[12 , 34 , 45 , 45]
# percentage=(sum(Marks)/400)*100
# print(percentage)

# def & return FUNCTION IN PYTHON : ---
# def percent(marks):
#     return((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
# marks1=[23 , 34 , 58 , 69]
# percentage1=percent(marks1)

# marks2=[23 , 38 , 59 , 69]
# percentage2=percent(marks2)

# marks3=[23 , 45 , 69 , 68]
# percentage3=percent(marks3)

# marks4=[63 , 94 , 98 , 99]  
# percentage4=percent(marks4)
# print(percentage1 , percentage2 , percentage3 , percentage4)
# def greet(name):
#     print("good day " + name)

# def mysum(sum1 , sum2):
#     return(sum1+ sum2)


# greet("abhishek")
# s=mysum(6,5)
# print(s)
    
# DEFAULT ARGUMENTS PYTHON :------(in this def function name is automatically defined when can give any name then they give name which we have give or entered)
# def greet(name):
#     print("good day ," + name)

# greet("abhishek")
# greet()
# def mysum ( sum1,sum2):
#     return sum1+sum2
# s = mysum(6, 32)
# print(s)
# # DEFAULT PARAMETER VALUE :---
# # we can give a defalt value when no argument is passed     
# def greet(name="Stranger"):
#     print("good day ," + name)

# greet("abhishek")
# greet()
# RECURSION :----
# FACTORIAL OF ANY VALUE :
# def factorial_iter(n):
#     product = 1
#     for i in range (n):
#         product= product * (i+1)
#     return product

# def factorial_recursive(n):
#     return n * factorial_recusive(n-1)
# f=factorial_iter(5)
# print(f)

# WRITE A PROGRAM USING FUNCTION TO FIND THE GREATEST OF THREE NUMBERS ?
# def maximum(num1 , num2 , num3 ):
#     if (num1 > num2):
#         if(num1>num3):
#             return num1
#         else:   
#             return num3
#     else:
#         if(num2>num3):
#             return num2
#         else:
#             return num3
# m = maximum(2 , 3, 4)
# print("the value of maximum is " + str(m))

# WRITE A PYTHON PROGRAM USING FUNCTION TO CONVERT CELCIUS TO FEHRANHIT ?
# def farh(cel):
#     return (cel * (9/5)) + 32 

# c = 37
# f = farh(c)
# print("fahreheit temperature is " + str(f))

# HOW DO YOU PREVENT A PYTHON PRINT()FUNCTION TO PRINT A NEW LINE AT THE END ?
# print("hello" , end=" ")
# print("how" , end=" ")
# print("are" , end=" ")
# print("you" , end=" ")
# WRITE A RECUSIVE FUNCTION TO CALCULATE THE SUM OF FIRST N NATURAL NUMBER ?







# WRITE A PYTHON FUNCTION TO PRINT FIRST N LINES OF THE FOLLOWING PATTERN ?
# ***
# **    FOR N =3
# *
# n =  4 
# for i in range(n):
#     print("*" * (n+i+1))

# WRITE A PYTHON FUNCTION  TO PRINT MULLTIPLICATION TABLE OF A GIVEN NUMBER?
# def multiply(num,count):
#     return num * count

# n = int(input("enter any number :"));
# i=1
# for i in range(1,11):
#     print(n," * " , i , " = " , multiply( n , i ))
#     i = i + 1  


# FILE HANDLING :------
# USE OPEN FUNCTION TO READ THE CONTENT OF A FILE 
# f = open('C:\\Users\\Abhishek\\OneDrive\\python full\\sample.txt' , 'r')
# f = open('C:\\Users\\Abhishek\\OneDrive\\python full\\sample.txt') if we can write 'r' it automatic read the document by defaault it will takes 'r'
# data = f.read(4)
# if we wants to read only only some character then we write the character 
# print(data)
# f.close()


# READLINE function reads the function line by line :-------
# f = open('C:\\Users\\Abhishek\\OneDrive\\python full\\sample.txt')
# Read first line
# data = f.readline()
# print(data)
# Read Second line
# data = f.readline()
# print(data)
# Read Third line
# data = f.readline()
# print(data)
# f.close()
# Modes of Opening file :
# r = opening for reading 
# w = opening for writing 
# a = opening for appending 
# + = opening for updating 

# This Writes the function create a txt file & starts from write mode 
# f = open('abhishek.txt' , 'a')
# f.write("iam appending")
# f.close()

# With statement automatically close the function 
# with open('abhishek.txt', 'r') as f:
#     a= f.read()
# print(a)
# f=open('abhishek.txt')
# t=f.read()
# if 'twinkle' in t:
#     print("twinkle is present")
# else:
#     print("twinkle is not present ")
#     f.close()

# for i in range (2 , 21):
#     with open (f"Multiplication_table_of_{i}" , 'w' ) as f:
#         for j in range(1 , 11):
#             f.write(f"{i}X{j}={i*j}\n")
#     break  
# num = int (input("Enter any number to test whether it is odd or even: ""))

# if (num % 2) == 0

#      print (“The number is even”)

# else:

#       print (“The number is odd”)


