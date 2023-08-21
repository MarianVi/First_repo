from dataclasses import dataclass
from typing import List


@dataclass
class Person:
    name: str
    age: int


@dataclass
class Student(Person):
    university: str
    grades: List[float]


s = Student('Valentin', 45, 'Babes', [7.0, 8.3, 9.5])
print(s)
p = Person('Adrian', 37)
print(p)
'''
O clasa de tip dataclass, defineste automat functiile:
__init__ , __repr__ , __eq__
'''
