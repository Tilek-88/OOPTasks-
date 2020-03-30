# class Soldier():
#     def __init__(self, name):
#         self.name = name

# class Guns():
#     def __init__(self, bullets):
#         self.bullets = bullets
#         if self.bullets:
#             patron = 0
#             for x in range(0, self.bullets):
#                 patron += 1
#                 return 

# class Act_of_Shooting(soldier,Guns):
#     def __init__(self, name):
#         Soldier(self,name)
#         Guns(self)
# Soldier = Act_of_Shooting("Peter")
# Soldier.Guns()


class Soldier:
    def __init__(self,name):
        self.name = name

class Gun:
    def __init__(self):
        self.bullets = 35

    def AK47(self):
        print(f"Soldier {self.name.title()} scream 'A-ta-ta'")
        print(f"AK47 did: ")
        if self.bullets:
            piy = 0
            for x in range(self.bullets):
                piy += 1
                self.bullets -= 1
                print("ti-gi-ti-gi-tish",piy)
        else:
            print(f"No bullets!")
            self.patrons()

    def patrons(self):
        print(f"Bullets left {self.bullets} pieces")

    def reload(self):
        self.bullets = 40
        print(f"Soldier {self.name.title()} scream 'REALOAD!'")

class Act_of_Shooting(Soldier,Gun):
    def __init__(self,name):
        Soldier.__init__(self,name)
        Gun.__init__(self)
        print(f"Bullets: {self.bullets} pieces")

Soldier = Act_of_Shooting("Peter")
Soldier.AK47()