# my_friend_list = ["Ankit","Gulam","Aditya","Anirudh"]
# print(my_friend_list)
# for i in my_friend_list:
# print(i)
# ______________
# Loop with String
# my_language = "Python"
# for i in my_language:
#  print(i)
# ______________
# 1. Mutable :-
# ➢ Changeable
# ➢ in this case we can change entirely as well as specifically . ➢ Example : List , dictionary etc.
# ______________
# 2. Immutable :-
# ➢ Not changeable
# ➢ In this case we can change Entirely only not specifically.
# ➢ Example : string , tuple etc.
# ______________
# Why is string immutable? (Proof)
# my_language = "Python"
# print("before", my_language)
# my_language = "java"
# print("after: ",my_language)
# my_language = "Python"
# print("before", my_language)
# my_language[0] = "S"
# print("after: ",my_language)
# ______________
# Why is List mutable? (Proof)
# my_friend_list = ["Ankit","Gulam","Aditya","Anirudh"]
# print("before", my_friend_list)
# my_friend_list.remove("Ankit")
# print("after", my_friend_list)
# ______________ Tuple :-
# ➢ Tuple is a data structure , it is immutable ( it can be changed only
# entirely not specifically)
# ➢ It is a collection of items , just like a list .
# ➢ It can store any type of value just like a list.
# ➢ it is enclosed with parentheses ().
# my_tuple = ("Ankit",55, 6.6, True)
# print(my_tuple)
# ______________
# How to apply a loop in Tuple :-
# my_tuple = ("Ankit",55, 6.6, True)
# for i in my_tuple:
# print(i)
# Tuple Methods:
# ➢ count()
# ➢ index()
# 0 1 2 3 4 5 6 7
# my_tuple = (11,22,333,33,33,44,33,33)
# print(my_tuple.count(33)) 4
# print(my_tuple.index(33)) 3
# ______________
# Task:
# ➢ task 1 : give me 5 example of list , in which you have to
# use for loop to print list elements
# ➢ task 2 : give me 5 example of string , in which you have to
# use for loop to print string elements
# ➢ task 3 : Prove this statement , tuple is Immutable