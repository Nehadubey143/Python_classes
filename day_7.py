# append()

my_list = [11,23,44,55]
print("before operation : ", my_list)
my_list.append(66)
print("after operation: ", my_list) #   [11,23,44,55,66]

#_______________________________________

#extend()
my_list = [11,23,44,55]
print("before operation : ", my_list)
my_list.extend([111,222,333])
print("after operation: ", my_list) #  [11,23,44,55,111,222,333]

#_______________________________________

#insert()
my_list = [11,23,44,55]
print("before operation : ", my_list)
my_list.insert(2,202)
print("after operation: ", my_list) #  [11,23,202,44,55]

#_______________________________________

#remove()
my_list = [11,23,44,55]
print("before operation : ", my_list)
my_list.remove(44)
print("after operation: ", my_list)

#_______________________________________

#pop()
my_list = [11,23,44,55]
print("before operation : ", my_list)
my_list.pop()
print("after operation: ", my_list)

my_list = [11,23,44,55]
print("before operation : ", my_list)
my_list.pop(0)
print("after operation: ", my_list)

#_______________________________________

#reverse()
my_list = [11,23,44,55]
print("before operation : ", my_list)
my_list.reverse()
print("after operation: ", my_list)

#_______________________________________

# sort()
# 		Ascending order

my_list = [6,5,7,9,2,1]
print("before operation : ", my_list)
my_list.sort()
print("after operation: ", my_list)

		# Descending order
my_list = [11111,233,3, 44,55]
print("before operation : ", my_list)
my_list.sort(reverse=True)
print("after operation: ", my_list)
#_______________________________________

#count()
my_list = [11111,233,3,3,3,3,3, 44,55]
print("before operation : ", my_list)
count_number = my_list.count(3)
print("after operation: ", count_number)

#_______________________________________

#index()
#          	         0      1  2
my_list = [11111,233,3,3,3,3,3, 44,55]
print("before operation : ", my_list)
index_of_3 = my_list.index(3)
print("after operation: ", index_of_3)

#_______________________________________

#clear()

my_list = [11111,233,3,3,3,3,3, 44,55]
print("before operation : ", my_list)
my_list.clear()
print("after operation: ", my_list)
#_______________________________________

