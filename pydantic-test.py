from datetime import date

from pydantic import BaseModel, ValidationError


class Person(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date

while True:
    first_name = input('Enter First Name: ')
    last_name = input('Enter Last Name: ')
    date_of_birth = input('Enter date of Birth (YYYY-MM-DD): ')

    try:
        person = Person(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth) # type: ignore
    except ValidationError:
        print('Please try again')
    else:
        break

print(person)
