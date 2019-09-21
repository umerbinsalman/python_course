# CODED BY UMER BIN SALMAN


# #Problem 1
# L=[5,6,8,9,2,1]
# L.sort()
# print(L)
# L.pop(2)
# print(L)
# L.append(10)
# print(L)
# L.reverse()
# print(L)
# print(L.pop(2))



# #problem 2
# list=[]
# sum=0
# x=int(input("input number of elements\n"))
# for i in range(x):
# 	num=int(input("enter number: "))
# 	list.append(num)
# length=len(list)
# for j in range(length):
# 	sum+=list[j]
# print("sum is: ",sum)



# #problem 3
# list=[]
# x=int(input("input number of elements\n"))
# for i in range(x):
# 	num=int(input("enter number: "))
# 	list.append(num)
# def largestNumber(list):
# 	length=len(list)
# 	list.sort()
# 	largest=list.pop(length-1)
# 	return largest
# print(largestNumber(list))



# #problem 4
# my_tuple= ('p','r','o','g','r','a','m','m','i','n','g')
# print(my_tuple[1:4])
# print(my_tuple[0:3])
# print(my_tuple[7:11])
# print(my_tuple)



# #problem 5
# my_tuple=(4,3,"a")
# def sortReverse(my_tuple):
# 	new_tuple=my_tuple[::-1]
# 	print(new_tuple)
# sortReverse(my_tuple)



# #problem 6
# dict={1:'1',2:'b',3:'c',12:'l'}
# key=int(input("enter a key: "))
# for x in dict:
# 	if (key==x):
# 		print("it is present in dictionary")
# 		break



# #problem 7
# dict={1:1,2:2,3:3}
# num=int(input("enter number to multiply with dictionary: "))
# def multiplyDict(dict,num):
# 	for x in dict.values():
# 		print(x*num)
# multiplyDict(dict,num)



# #problem 8
# D={'CP':'COMPUTER PROGRAMMING',
# 'FCE':'FUNDAMENTALS OF COMPUTER ENGINEERING',
# 'PST':'PAKISTAN STUDIES',
# 'BEE':'BASICS OF ELECTRICAL ENGINEERING',}
# del(D['CP'])
# D['F.ENG']='FUNCTIONAL ENGLISH'
# for x in D.values():
# 	print(x)



# #problem 9
# star=int(input("enter number of lines"))
# for x in range(0,star):
# 	for i in range(0,x+1):
# 		print("*",end="")
# 	print("\n")
# for y in range(star-1,0,-1):
# 	for j in range(0,y):
# 		print("*",end="")
# 	print("\n")



# #problem 10
# num=int(input("enter a number: "))
# for x in range(0,num):
# 	for i in range(0,x+1):
# 		print(x+1,end="")
# 	print("\n")



# #problem 11
# num=int(input("enter numer of elements of list"))
# def inputList():
# 	list=[]
# 	for i in range(num):
# 		number=int(input("enter number: "))
# 		list.append(num)
# 	return list
# print("list 1")
# list1=inputList()
# print("list 2")
# list2=inputList()
# def compareList(list1,list2):
# 	list1.sort()
# 	list2.sort()
# 	if(list1==list2):
# 		print("the list element are common")
# 	else:
# 		print("the list element are not common")
# compareList(list1,list2)



# #problem 13
# list=[1,4,2]
# length=len(list)
# def evenNumbers(list):
# 	even_list=[]
# 	for x in range(length):
# 		if(list[x]%2==0):
# 			even_list.append(list[x])
# 	return(even_list)
# print(evenNumbers(list))



# #problem 14
# fact=int(input("enter a number to find factorial: "))
# def factorial(fact):
# 	num=1
# 	for x in range(1,fact+1):
# 		num=num*x
# 	return num
# print(factorial(fact))