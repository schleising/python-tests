# newList = (i for i in range(10))
newList = (0,1,2,3,4,5,6,7,8,9)

print(newList) 
# print(*newList)

x, y, *rest = newList

print(x)
print(y)
print(rest)
