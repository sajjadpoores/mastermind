import random
from consts import *


class game(object):
    def __init__(self, length=GUESS_LENGTH):
        self.length = length
        self.turns = 0
        self.initial_state = self.new_game()
        self.is_won = False
        self.is_end = False

    def new_game(self):
        initial = []
        while len(initial) < 4:  # generating 4 unrepeated random numbers
            r = random.randint(RAND_LOWERBOUND, RAND_UPPERBOUND)
            if r not in initial:
                initial.append(r)
        initial = [COLORS[i] for i in initial]  # change keys to values
        return initial

    def turn(self):
        guess = input()
        guess = guess.split(",")
        black, white = 0, 0

        for i in range(GUESS_LENGTH):
            if guess[i] == self.initial_state[i]:
                black += 1
            elif guess[i] in self.initial_state:
                white += 1
        print("blacks: {} and whites: {}".format(black, white))

        self.turns += 1
        self.check_status(black)

    def to_str(self, array):
        return " | ".join(array)

    def check_win(self, black):
        return black == GUESS_LENGTH

    def check_lose(self):
        return self.turns == MAX_TURNS and not self.is_won

    def check_status(self, black):
        if self.check_win(black):
            print("you won!")
            self.is_end = True
        elif self.check_lose():
            print("You lose! initial state was: " + self.to_str(self.initial_state))
            self.is_end = True

    def start(self):
        for i in range(MAX_TURNS):
            self.turn()

            if self.is_end:
                return


ngame = game()
ngame.start()
