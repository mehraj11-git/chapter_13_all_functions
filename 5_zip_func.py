user_id = ["user1","user2","user3"]
names = ["mehraj","khan","sharat"]

# if u have to list with one with name and code to combine them we use zip method
# this func give zip object 
# this gives tuple or list or dict
# ("user1","merhaj") like this
# we can do more than two list 
# as like the filter and map func we use the zip func

last_names = ["uddin","kahled","shiamu"]
print(zip(user_id,names))     #this is iterator
print(list(zip(user_id,names))) #iterable (1)
print(list(zip(user_id,names,last_names))) #(2)

# (1) we can convert them in dict
# (2) we cant convert them in dict bcz for dict key and value pair required but it has three 

