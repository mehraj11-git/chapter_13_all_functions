# def a func and take no. of list in it containing numbers 
# [1,2,3],[4,5,6],[7,8,9]
# return average of the list 
# (1+4+7)/3,(2+5+8)/3,(3+6+9)/3
# fisrt thing if u can do this with two list then you can do no.of list
def new_list(l1,l2):
    average = []
    for pair in  zip(l1,l2):
        average.append(sum(pair)/len(pair))
    return average
print(new_list([1,2,3],[4,5,6]))

# first ypu have to do zip and do loop in it.
# then you have to do sum of the pair
# and divide them with length of pair
# and append this in a created variable(average) and return it.

# now number of list
def new_list(*args):
    average = []
    for pair in zip(*args):
        average.append(sum(pair)/len(pair))
    return average
print(new_list([1,2,3],[4,5,6],[7,8,9]))

# we use *args for that 
# args take result i tuple and for unpack tuple we use *agrs in for loop

# now convert it in one line by using lambda expression

anonymous = lambda *args:[sum(pair)/len(pair)for pair in zip(*args)]
print(anonymous([1,2,3],[4,5,6],[7,8,9]))
# first func take the *args and return the list
# and then ypu have to sum devide by length


# read the code 
# first we will check the func in this code we used lambda
# we can see that there is a zip method and we use args method to unpack the list 