import random 


class Player:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def roll_dice(number_of_dice) -> list:
        result = []
        roll = [random.randint(1,6) for _ in range(number_of_dice)]

        total = sum(roll)
        result.append(total)
        result.append(roll)
        return result
