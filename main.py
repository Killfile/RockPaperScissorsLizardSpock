import random


class Game:
    def __init__(self):
        self.game_won = False
        self.rounds_played = 0
        self.p1_wins = 0
        self.p2_wins = 0
        self.draw = False
        self.p1_choice = None
        self.p2_choice = None
        self.p1_throws = []
        self.p2_throws = []

    def play(self):
        while self.game_won is False:
            if self.p1_wins > self.p2_wins:
                print(f"Round {self.rounds_played + 1}: Sheldon leads Kripke {self.p1_wins} to {self.p2_wins}")
            elif self.p2_wins > self.p1_wins:
                print(f"Round {self.rounds_played + 1}: Kripke leads Sheldon {self.p2_wins} to {self.p1_wins}")
            else:
                print(f"Round {self.rounds_played + 1}: Sheldon and Kripke are tied at {self.p1_wins} wins each")

            self.p1_choice = random.choice(["Paper", "Rock", "Scissors"])
            print(f"Sheldon chose {self.p1_choice} -- previous throws are {self.p1_throws}")
            self.p2_choice = random.choice(["Paper", "Rock", "Scissors"])
            print(f"Kripke chose {self.p2_choice} -- previous throws are {self.p2_throws}")
            self.p1_throws.append(self.p1_choice)
            self.p2_throws.append(self.p2_choice)

            if self.p1_choice == "Rock" and self.p2_choice == "Paper":
                self.p2_wins += 1
                print(f"Kripke's Paper crushes Sheldon's Rock - Player 2 Wins!")
            elif self.p1_choice == "Paper" and self.p2_choice == "Rock":
                self.p1_wins += 1
                print(f"Sheldon's Paper covers Kripke's Rock - Player 1 Wins!")
            elif self.p1_choice == "Rock" and self.p2_choice == "Scissors":
                self.p1_wins += 1
                print(f"Sheldon's Rock crushes Kripke's Scissors - Player 1 Wins!")
            elif self.p1_choice == "Scissors" and self.p2_choice == "Rock":
                self.p2_wins += 1
                print(f"Kripke's Rock crushes Sheldon's Scissors - Player 2 Wins!")
            elif self.p1_choice == "Scissors" and self.p2_choice == "Paper":
                self.p1_wins += 1
                print(f"Sheldon's Scissors cuts Kripke's Paper - Player 1 Wins!")
            elif self.p1_choice == "Paper" and self.p2_choice == "Scissors":
                self.p2_wins += 1
                print(f"Kripke's Scissors cuts Sheldon's Paper - Player 2 Wins!")
            else:
                print(f"DRAW!!! Sheldon and Kripke both threw {self.p1_choice}")
                self.draw += 1
            self.rounds_played += 1
            if self.p1_wins >= 3:
                self.game_won = True
                print(f"That's a wrap! Sheldon has won the office with 3 wins in {self.rounds_played} rounds")
            if self.p2_wins >= 3:
                self.game_won = True
                print(f"That's a wrap! Kripke has won the office with 3 wins in {self.rounds_played} rounds")


if __name__ == '__main__':
    game = Game()
    game.play()
