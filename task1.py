class student():
    def __init__(self,name,lastname,department,year_of_entrance):
        self.name = name
        self.lastname = lastname
        self.department = department
        self.year_of_entrance = year_of_entrance
    def get_students_info(self):
        print(self.name,self.lastname, self.department,self.year_of_entrance)

        
student1 = student('Вася', 'Иванов' ,'Программирование', 'поступил в 2017 г')
student1.get_students_info()
student2 = student('Isa', 'Ysonov', 'Buhchet', 'postupil v 2006 g')
student2.get_students_info()




       