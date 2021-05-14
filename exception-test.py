import sys

while True:
    inputValue = input('Input hex number without 0x: ')

    try:
        number = int(inputValue, base=16)
    except ValueError as ve:
        print(ve)
        continue
    else:
        print('Number good...')
    finally:
        if inputValue.lower() in ['quit', 'a']:
            sys.exit('Quitter')

    print(number)
