import random 
from player import Player
from questions import questions

class Game:
    def __init__(self, current_player_index, points_to_win, players):
        self.score = [0, 0]
        self.players = players
        self.current_player_index = current_player_index
        self.points_to_win = points_to_win
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            return True
        else: 
            return False

    def play_game(self, points_to_win, current_player_index):
        print(f"First to {points_to_win} points wins")
        print("-- LETS PLAY --")
        while True:
            current_player = self.players[current_player_index]
            a = input(f"{current_player.name.upper()} press enter to roll -> ")
            roll = current_player.roll_dice(2)
            print(f"{roll[1]}...You rolled a {roll[0]}")

            q = random.choice(questions)
            print(f"Q. {q["question"]} (true/false)")
            answer = input("Answer: ")

            if self.check_answer(answer.capitalize(), q["answer"]):
                print("correct")
                self.score[current_player_index] += roll[0]
            else:
                print(f"That's incorrect! You need {points_to_win - self.score[0]} points to win")
        
            if self.score[current_player_index] >= points_to_win:
                print(f"{current_player.name.upper()} wins!!")
                break
            
            print(f"<<< Score: {self.score[0]} - {self.score[1]} >>>")
            questions.remove(q)
            current_player_index = (current_player_index + 1) % 2

