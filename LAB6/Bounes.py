import random

# Character class
class Character:
    def __init__(self, name, weapon, energy, life):
        self.name = name
        self.weapon = weapon
        self.energy = energy
        self.life = life
    
    def change_name(self, new_name):
        self.name = new_name

    def change_weapon(self, new_weapon):
        self.weapon = new_weapon

    def increase_energy(self, food_type):
        self.energy += food_type
        if self.energy >= 100:
            self.life += 1
            self.energy = 0
        elif self.energy > 100:  # Prevent energy from exceeding 100
            self.energy = 100

    def decrease_energy(self, shot):
        self.energy -= shot
        if self.energy <= 0:
            if self.life > 0:
                self.life -= 1
                self.energy = 100  # Reset energy to 100 if life is available
            else:
                self.energy = 0  # Keep energy at 0 if no life is left

# Attack another character, randomly decreasing their energy
def attack(source, target):
    damage = random.randint(5, 20)  # Random damage between 5 and 20
    print(f"{source.name} attacks {target.name} with {damage} damage!")
    target.decrease_energy(damage)

# Use your creativity to simulate combat between two selected characters
def combat(source, opponent):
    while source.life > 0 and opponent.life > 0:
        attack(source, opponent)
        if opponent.life > 0:
            attack(opponent, source)
        else:
            print(f"{opponent.name} has been defeated!")
            break
        if source.life <= 0:
            print(f"{source.name} has been defeated!")
            break

# Game class
class Game:
    # Initialize an empty list to store characters
    def __init__(self):
        self.characters = []

    # Method to add a character to the game
    def add_character(self, character):
        self.characters.append(character)
    
    # Method to view all characters in the game
    def view_characters(self):
        for index, character in enumerate(self.characters):
            print(f"{index}: {character.name} (Weapon: {character.weapon}, Energy: {character.energy}, Life: {character.life})")

    # Method to select a character from the list based on its index
    def select_character(self, index):
        if 0 <= index < len(self.characters):
            return self.characters[index]
        else:
            print("Invalid index.")
            return None

if __name__ == '__main__':
    # Food type dictionary for increasing energy
    food_type = {
        "A": 5,
        "B": 10,
        "C": 15,
        "D": 20
    }
    
    # Example of accessing and printing values from food_type dictionary
    print(f"Energy provided by food type 'A': {food_type['A']}")  # Prints: 5

    # Create a game instance and 5 characters
    game = Game()

    char1 = Character("Warrior", "Sword", 80, 3)
    char2 = Character("Archer", "Bow", 70, 3)
    char3 = Character("Mage", "Staff", 90, 3)
    char4 = Character("Knight", "Spear", 85, 3)
    char5 = Character("Assassin", "Dagger", 75, 3)

    game.add_character(char1)
    game.add_character(char2)
    game.add_character(char3)
    game.add_character(char4)
    game.add_character(char5)

    # View all characters
    game.view_characters()

    # Select two characters to fight
    source = game.select_character(0)  # Warrior
    opponent = game.select_character(1)  # Archer

    # Start the combat between the two characters
    if source and opponent:
        combat(source, opponent)
