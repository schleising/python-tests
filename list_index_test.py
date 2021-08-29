new_list = [1,2,3,1,4,5,6,1,7,8,9,1]

index = 0

while True:
    try:
        index = new_list.index(1, index)
        print(index)
        index += 1
    except ValueError:
        break
