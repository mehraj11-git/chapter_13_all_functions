# for ex if u have a func 
def is_even(a):
    return a%2==0
numbers = [1,2,3,4,6,8,9,10]

# if u wanna filter the even number from this number list we use filter func
# like map func we use this filter func,first take the func and then the iterable
# we can convert this in list or tuple as like the map func
# filter func is iterable
# we can use loop in this func but if we convert them in list or tuple we can do more than one loop
even = list((filter(is_even,numbers)))
print(even)

# lambda func
evens = list(filter(lambda a:a%2==0,numbers))
print(evens)

# comprehension method

evenss = [i for i in numbers if i%2==0]
print(evenss)