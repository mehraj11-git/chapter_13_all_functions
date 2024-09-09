# diff btw sort func and soretd func 
fruits = ["grapes","mango","apple"]
fruits.sort()
print(fruits)

fruits2 = ('grapes','kiwi','banana')
# sort will not work here bcz tuple is unchangable (immutable)
# for that we use sorted func 
sorted(fruits2)
print(fruits2)
print(sorted(fruits2))  #use the code in this manner to get the correct result



fruits3 = {"grapes","orange","apple"}
print(sorted(fruits3))

guiters = [
    {'model': 'yamaha f310','price' : 18400},
    {'model':'faith naptune','price':5000},
    {'model':'taylor 814ce','price':450000}
]
# for ex we want to sort as per the price

print(sorted(guiters,key = lambda d :d['price']))   #(1)
print(sorted(guiters,key = lambda d :d['price'],reverse = True))
print(sorted(guiters,key = lambda item:item.get('model'))) #(2)

# due to addition of reverse func they print the from high to low
# without reverse method it goes from low to high
# we can store this in a variable
# both 1 and 2 are same diff ways but the results are same
sorted_func=sorted(guiters,key = lambda item:item.get('model'))
print(sorted_func)