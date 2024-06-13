import random
from questions import questions


class Game:
    def __init__(self, current_player_index, points_to_win, players):
        self.score = [0, 0]
        self.players = players
        self.current_player_index = current_player_index
        self.points_to_win = points_to_win

    @staticmethod
    def check_answer(user_answer: str, correct_answer: str) -> bool:
        if user_answer == correct_answer:
            return True
        else:
            return False

    def play_game(self) -> None:
        print(f"First to {self.points_to_win} points wins")
        print("-- LETS PLAY --")
        while True:
            current_player = self.players[self.current_player_index]
            input(f"{current_player.name.upper()} press enter to roll ->  ")
            roll = current_player.roll_dice(2)
            print(f"{roll[1]}...You rolled a {roll[0]}")

            if roll[0] + self.score[self.current_player_index] >= self.points_to_win:
                print("** THIS WILL WIN THE GAME! **")

            q = random.choice(questions)
            print(f"Q. {q["question"]} (true/false)")
            answer = input("Answer: ")

            if self.check_answer(answer.capitalize(), q["answer"]):
                print("That's Correct")
                self.score[self.current_player_index] += roll[0]
            else:
                print(f"That's Incorrect! You need {self.points_to_win - self.score[0]} points to win")

            if self.score[self.current_player_index] >= self.points_to_win:
                print(f"🎉🎉 {current_player.name.upper()} WINS! 🎉🎉")
                break

            print(f"<<< Score: {self.score[0]} - {self.score[1]} >>>")
            questions.remove(q)
            self.current_player_index = (self.current_player_index + 1) % 2
