class Character:
    def __init__ (self,name,weapon,energy,life):
        self.name = name
        self.weapon = weapon
        self.energy = energy
        self.life = life
    
    def change_name(self,new_name):
        self.name = new_name

    def change_weapon(self,new_weapon):
        self.weapon = new_weapon

    def increse_energy(self,food_type):
        self.energy = self.energy + food_type
        if self.energy == 100:
            self.life = self.life + 1
            self.energy = 0
        else:
            pass

    def decrease_energy(self,shot):
        self.energy = self.energy - shot
        if self.energy == 0:
            self.life = self.life - 1
            self.energy = 100
        else:
            pass

    #def move_left(self):
       # self.


if __name__ == '__main__':
    food_type = {
        "A":5,
        "B":10,
        "C":15,
        "D":20
    }  
    print(food_type['A']) 
