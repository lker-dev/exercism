import random

def modifier(number):

    return (number - 10) // 2

class Character:

    @staticmethod
    def ability():  
        return Character.baseStat()

    def __init__(self):

        """
        Initialize strength, dexterity, constitution, intelligence, wisdom and charisma.
        """

        self.strength = Character.baseStat()
        self.dexterity = Character.baseStat()
        self.constitution = Character.baseStat()
        self.intelligence = Character.baseStat()
        self.wisdom = Character.baseStat()
        self.charisma = Character.baseStat()
        self.hitpoints = 10 + modifier(self.constitution)

    @staticmethod
    def baseStat():

        
        rolls = [random.randint(1,6) for _ in range(4)]
        print(rolls)
        rolls.remove(min(rolls))
        print(rolls)
        return sum(rolls)

