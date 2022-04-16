# while(True):
#     try:
#         x = int(input('Input Number: '))
#     except ValueError as e:
#         print(e)
#         continue

#     match x:
#         case 1 | 2 as y:
#             print(f'{y} is One or Two')
#         case 3 | 4 as y:
#             print(f'{y} is Three or Four')
#         case 5 | 6 as y:
#             print(f'{y} is Five or Six')
#         case _ as y:
#             print(f'{y} is None of the expected values')
#             break

# class Testing:

#     def UpdateScore(self, teamScore: int, oppositionScore: int):
#         match teamScore - oppositionScore:
#             case 0:
#                 print(f'Still drawing {__class__.__name__}')
#             case 1:
#                 print(f'Team lead by one {teamScore} - {oppositionScore}')
#             case -1:
#                 print('Team deficit of one')
#             case x if x > 1:
#                 print('Huh 1 !!?')
#             # case x if x < -1:
#             #     print('Huh 2 !!?')
#             case _:
#                 raise ValueError(f'Error in {__class__.__name__}, {teamScore} - {oppositionScore}')

# testing1 = Testing()
# testing1.UpdateScore(1, 9)

list1 = ['Liverpool', 'Man City', 'Chelsea']
list1 = [team.lower() for team in list1]

def HandleCan(inputList: list[str]) -> None:
    match inputList:
        case [teamA, 'beat', teamB] | [teamA, 'still', 'beat', teamB]:
            if teamA in list1 and teamB in list1:
                print(f'{teamA} can beat {teamB}')
            else:
                print("Don't ask stupid questions")
        case _:
            print("Can't work it out")

inputString = '/can Liverpool stilL beat Chelsea'.lower()

match inputString.split():
    case ['/can', *request]:
        HandleCan(request)
    case _:
        print('Number not in list')

