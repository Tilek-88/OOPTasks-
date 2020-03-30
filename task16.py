import random
 
class unit:
    def __init__(self, id, team):
        self.id = id
        self.team = team
 
class soldier(unit):
    def follow(self, hero):
        print ("Soldier with ID {} is following Hero with ID {}".format(self.id, hero.id)
 
    
    class hero(unit):
        def init(self, id, team):
            unit.init(self, id, team)
            self.level = 0
    
        def levelup(self, team_size):
            self.level = team_size / 10
    
    teams = ['good_team', 'bad_team']
    gandalf = hero(1, teams[0])
    sauron = hero(2, teams[1])
    
    soldiers = []
    good_team = [gandalf]
    bad_team = [sauron]
    
    for i in range(1,1000):
        soldiers.append(soldier(i, random.choice(teams)))
    
    for warrior in soldiers:
        if warrior.team == 'good_team':
            good_team.append(warrior)
        else:
            bad_team.append(warrior)
    
    print ("Good team size: {}, Bad team size: {}".format(len(good_team), len(bad_team))
    
gandalf.levelup(len(good_team))
sauron.levelup(len(bad_team))
    
    print "Gandalf lvl {}, Sauron lvl {}".format(gandalf.level, sauron.level)
    
random.choice(good_team).follow(gandalf)