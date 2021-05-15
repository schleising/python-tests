import sys

while True:
    inputValue = input('Input hex number without 0x: ')

    try:
        number = int(inputValue, base=16)
    except ValueError as ve:
        print(f'\'{inputValue}\' is not a valid hex number')
        continue
    else:
        print(f'Number {number} good')
    finally:
        if inputValue.lower() in ['q', 'a']:
            sys.exit('Quitter')

    print(number)
