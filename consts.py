COLORS = {
    1: 'red',
    2: 'blue',
    3: 'green',
    4: 'yellow',
    5: 'white'
}

MAX_TURNS = 10
GUESS_LENGTH = 4
RAND_UPPERBOUND = max(COLORS.keys())
RAND_LOWERBOUND = min(COLORS.keys())

WON_MESSAGE = "You won!"
LOSE_MESSAGE = "You lose! initial state was: "