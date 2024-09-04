# iterable vs iterator
# iterable---> 


# In Python, an iterator is an object which is obtained from an iterable object by passing it to the iter() function. 
# An iterator holds a countable number of values that can be iterated upon. 
# An iterator is used to iterate over the iterable objects like lists, strings, tuples, etc. 
# in Python. On the iteration of an iterator, it returns each element one by one.
# for ex :
numbers = [1,2,3,4]     #iterables   (iterable objects like lists, strings, tuples, etc.) (1)
square = map(lambda a:a**2,numbers)    #iterator

# for loop behind the scene 
# for i in numbers:
#     print(i)

# step 1 : for loop call iter func 
# iter(numbers)--->iterator 
# atfer this next(iter(number)) this func run 
number_iter = iter(numbers)
print(next(number_iter))  #1
print(next(number_iter))  #2
print(next(number_iter))  #3
print(next(number_iter))  #4
# print(next(number_iter))  #stop iteration#

# this is how for loop work on iterable objects (1)

# iterator
print(iter(numbers)) #iterator object
print(next(numbers))  #not iterator
