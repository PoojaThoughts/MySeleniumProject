b=set()
b.add(1)
b.add(2)
b.add(3)
b.add(4)
b.add(5)
b.add(5) 
b.add(5)
b.add((10,20,30))

print(b)
print(type(b))
print(len(b))

b.remove(5) #removes 5 from set b
print(b)

# b.remove(15) # therows an error while try to remove 15 which is not present in set 
# print(b)

b.pop()
print(b)