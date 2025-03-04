from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    name:str = 'Swati'  # default can be made
    age:Optional[int] = None
    
new_student = {'name':'Ekansh'}

# 'name':32 (error) pydantic validates  
student = Student(**new_student)

def_student = {}
student_1 = Student(**def_student)
print(student_1)

# pydantic handles itself whenever possible suppose age passed as string so it will handle itself
# many builtin valdiations eg EmailStr email : EmailStr
# cgpa:float = Field(gt=a, lt=b, default=c, description='ssdcsc')