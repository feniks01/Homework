class Gameplay:
    def __init__(self,name,health,nickname):
        self.name = name
        self.health = health
        self.nickname = nickname
    def __str__(self):
        return str(self.name) + ' the ' + str(self.nickname)

    def is_alive(self):
        if self.health < 0:
            return False
        else : 
            return True
    def get_health(self):
        return self.health

    def take_damage(self, damage_point):
        if damage_point > self.get_health():
            self.health = 0
        else:
            self.get_health - damage_point

    def take_healing(self , healing_point):
        max_health = 100
        currect_health = 80

        if not self.is_alive(): return False 
        print("It's too late to heal our hero") 
        if self.is_alive(): return True
        print("Our hero is not dead")
        if healing_point > 0:
            self.health = max_health
        else: self.health = currect_health



        