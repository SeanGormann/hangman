# Hangman

import random

def hangman(word):
    wrong = 0
    stages = ["",
              "______      ",
              "|           ",
              "|     |     ",
              "|     O     ",
              "|    /|\    ",
              "|    / \    ",
              "|___        ",
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("\n")
    print("Welcome to Hangman.")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter:"
        char = input(msg)
        # secret hint function
        if char == "hint":
            spoil = random.randint(0, len(word) - 1)
            if rletters[spoil] != "$":
                board[spoil] = rletters[spoil]
                rletters[spoil] = "$"
        #
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print("\n")
        print((" ".join(board)))
        # Shows remaining number of guesses
        print("Guesses left: {}".format(7 - wrong))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! It was {}.".format(word))
        









