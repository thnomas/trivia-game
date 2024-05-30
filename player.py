import random 

class Player():
    def __init__(self, name):
        self.name = name

    def roll_dice(self, number_of_dice) -> list:
        result = []
        roll = [random.randint(1,6) for i in range(number_of_dice)]

        total = sum(roll)
        result.append(total)
        result.append(roll)
        return result
