class Student():
    def __init__(self, name, age, magor):
        self.name = name
        self.age = age
        self.magor = magor

    def boy(self):
        print(f'name: {self.name}    age: {self.age}    magor: {self.magor}')    


Steve = Student("Steven Schultz", 23, "English")
Johnny = Student("Jonathan Rosenberg", 24, "Biology")
Penny = Student("Penelope Meramveliotakis", 21, "Physics")   
Student.boy(Steve)
Student.boy(Johnny)
Student.boy(Penny)