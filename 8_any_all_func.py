# any is diff func and all is diff func 
number1 = [2,4,6,8]
number2 = [1,3,5,7]
even1 = []
for num in number1:
    if num%2==0:
        even1.append(True)

print(even1)
# this all func check whether all the strings are same or not like the 'and' func

print(all([True, True, False, True]))
print(all([True, True, True, True]))
print(any([True, True, False, True]))

# now using comprehension method with all func
print(all([num%2==0 for num in number1]))

# any func is like the 'or' method if there is one string meets the condition then the condition true



def my_sum(*args):
    total = 0
    for num in args:
        total +=num
    return total