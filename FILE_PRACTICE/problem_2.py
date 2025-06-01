'''
The game() function in a program lets a user play a game and returns the score as an integer.
You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. 
You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.
'''
import random


def game():
    print("You're playing the game...")
    score = random.randint(1, 100)
    with open("Hi-score.txt") as f:
        hi_score = f.read()
        if (hi_score == ""):  # if hi_score is blank thn hi_score=0
            hi_score = 0
        else:
            hi_score = int(hi_score)

        print(f"Your score: {score}")
        if (score > hi_score):
            # write the hi_score to the file
            with open("Hi-score.txt", "w") as f:
                # in file we need to write as str. so convert the int to str
                f.write(str(score))

    return score


game()
