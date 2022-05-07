from bisect import bisect_right, bisect_left, bisect

list1 = [i for i in range(10)]

result_right = bisect_right(list1, 9.5)
result_left = bisect_left(list1, 9.5)
result = bisect(list1, 9.5)

print(list1)
print()
print(result_right)
print(result_left)
print(result)

if result > len(list1) - 1:
    result = len(list1) - 1

print(list1[result-1], list1[result])
