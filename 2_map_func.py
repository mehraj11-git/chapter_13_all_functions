numbers = [1,2,3,4]    #this is iterable
def square(a):         # this is func
    return a**2
# map func
# in map func first we have to take the func and then the iterable
# suppose if print this this directly it will show the map at object but we want the map to do func 
# for that we have to convert this map into list or tuple and store in varibale 
# map func is iterable --->we can do looop in this method
# mostly we use map func with predefine func for ex:look at (1)
new_list=list(map(square,numbers))
print(new_list)

# we can do this with list comprehension method
squares = [i**2 for i in numbers]
print(squares)

# now we are using the lambda func

new_square = list(map(lambda a:a**2,numbers))
print(new_square)

# without func method
new = []
for i in numbers:
    new.append(square(i))
print(new)    

# it means that to solve the one prlbm we hava too many methods

total = ["abc","cde","efghc"]
# (1)suppose if wanna find the length of the 0 position 
# we can use index slicing method to know the particular string length
length = tuple(map(len,total))
print(length)