from typing import TypedDict

class Person(TypedDict):
    
    name:str
    age:int
    
new_person = Person = {'name':'Ekansh', 'age':21}

# will also work if 'age':'21' (str) so no validation

print(new_person)