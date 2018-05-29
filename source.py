import random

colors = {
    1: 'red',
    2: 'blue',
    3: 'green',
    4: 'yellow',
    5: 'white'
}

initial = []
win = False
while len(initial) < 4:  # generating 4 unrepeated random numbers
    r = random.randint(1, 5)
    if r not in initial:
        initial.append(r)

initial = [colors[i] for i in initial]  # change keys to values
# print(initial)  # CHEAT!
for turn in range(4):
    guess = input()
    guess = guess.split(",")
    black, white = 0, 0

    for i in range(len(initial)):
        if guess[i] == initial[i]:
            black += 1
        elif guess[i] in initial:
            white += 1
    print("blacks: {} and whites: {}".format(black, white))
    if black == 4:
        win = True
        print("you won!")
        break

if not win:
    initial = "][".join(initial)
    print("You lose! initial state was: ["+initial+"]")
