set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
list1 = [4, 5, 6, 10]
set2 = {5, 6, 7}

print(set1 & set(list1)) # 4, 5, 6
print(set1 | set(list1)) # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(set1 ^ set(list1)) # 1, 2, 3, 7, 8, 9, 10
print(set1 - set(list1)) # 1, 2, 3, 7, 8, 9
print(set1 > set2) # True (all items of set2 are in set1)
print(set1 >= set2) # True (all items of set2 are in set1 and set2 != set1)
print(set1 >= set1) # True (all items of set1 are in set1 and set1 == set1)
print(set1 > set1) # False (all items of set1 are in set1 but set1 == set1)
