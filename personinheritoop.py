class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def person_info(self):
           pass


class Employee(Person):
    def __init__(self, name, age,gender,dept,sal):
        super(). __init__(name,age,gender)
        self.sal = sal
        self.dept = dept

    def person_info(self):

        return f'{self.name} {self.age} {self.gender} {self.sal} {self.dept}'


# person = Employee('john',22, 'male', 3456667, 'IT')
# info = person.person_info()
# print(info)