number = [1,3,58,6]
print(max(number))
print(min(number))
# this is the normal max or min func 
# suppose if we wanna know what string has the highest length than other for that we have
# # to use this 
# # for ex:
# # in that case we have to def the func and return the len function
names = ["merhaj","khan","mohammed","meru"]
def func(item):
    return len(item)
print(max(names, key = func))
# print(min(names, key = func))

# # this method look like hard 
# # now we will do with lambda expression

print(min(names, key = lambda item : len(item)))
print(max(names, key = lambda item : len(item)))
print(max(names))

student = {
      "mehraj" :  {"score":90,"age":23},
      "adnan" :  {"score":80,"age":22},
      "khan" :  {"score":70, "age":28}
}
print(max(student,key= lambda item:student[item]['score']))
print(min(student,key= lambda item:student[item]['age']))
# in this code first take the dict name followed by the key as it contain dict
# use lambda exp of items now the tricky one is here we have to take the dict name containing the item in it
# and the score if u want otherwise u can compare with age as well


student2 = [
    {'name':'mehraj','score':80,'age':29},
    {'name':'omer','score':90,'age':23},
    {'name':'adnan','score':70,'age':26}

]
print(max(student2,key=lambda item:item.get('score')))
print(min(student2,key=lambda item:item.get('age')))
print(max(student2,key=lambda item:item.get('score'))['name'])
# in this code first we take list name(student2).
#  and then the dictionary we call dict as item,hence we write
# followed by checking the score the of the item. 
# we can check as per the age as well
# for print the name who has the highest score we have to add the name