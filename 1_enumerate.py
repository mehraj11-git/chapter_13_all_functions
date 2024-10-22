# we use enumerate func with for loop 
# when we use for loop with list and tuples we track the item but we donot tract the position 
# for that we use enumerate func
# first we will do without the enumerate func 

names = ['abc','abcd','efg']
pos = 0
for name in names:
    print(f"{pos}---->{name}")
    pos +=1
# in this method first we make variable with 0 value and start the loop 
# print it and then increase the variable value

# now with enumerate func

for pos,name in enumerate(names):
    print(f"{pos}---->{name}")

# with this method we make our code short 
# what we did in this method is we make [pos] as variable but in enumerate we use pos in for loop and with item 
# thats all we have to do.

# exercise 
# define a func that take two arguments
# list containing string
# string that need to find in your list
# and this func will return the index of string in your list and
# if string is not present then return -1

def new_list(l,l1):
    for pos,name in enumerate(l):
        if name ==l1:
         return pos
    return -1
           
print(new_list(names,'abcde'))