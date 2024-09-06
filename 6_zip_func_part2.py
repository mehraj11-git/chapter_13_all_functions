# l1 = [1,3,5,7] #(2)
# l2 = [2,4,6,8] #(3)

l = [(1,2),(3,4),(5,6),(7,8)]  #(1)
# now we gonna make this (1) list into (2) and (3)
# we can use comprehension , for loop ect
# but we use *operator with zip mwthod

print(list(zip(*l)))
# with this code we will get only two tuples
# now do like this
l1,l2 =list(zip(*l))
print(list(l1))
print(list(l2)) 
# first convert them in a list and print it
# now we print the greater number first and then the lower number

m1=[11,13,15,17]
m2=[12,14,16,18]
new_list = []
for pair in zip(m1,m2):
   new_list.append(max(pair))
print(new_list)
# we can do this with other methods as well but we do with zip method