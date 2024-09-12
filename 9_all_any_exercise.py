def my_sum(*args):
    if all([type(arg) == int or type(arg)==float for arg in args]):
     total = 0
     for num in args:
         total +=num
     return total
    else:
       return "wrong input"
print(my_sum(1,2,3,5,"mehraj",["sharat"]))

print(my_sum(1,2,3,4.5,9.5))

# now first we have to check the type and 
# check the condition of the list whether does it meets the condition or not