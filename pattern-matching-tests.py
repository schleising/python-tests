while(True):
    try:
        x = int(input('Input Number: '))
    except ValueError as e:
        print(e)
        continue

    match x:
        case 1 | 2 as y:
            print(f'{y} is One or Two')
        case 3 | 4 as y:
            print(f'{y} is Three or Four')
        case 5 | 6 as y:
            print(f'{y} is Five or Six')
        case _ as y:
            print(f'{y} is None of the expected values')
            break
