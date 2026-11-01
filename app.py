#this file is to learn python and syntax for a beginner

import random
# module to randomize 
import time
# module for time

num = random.randint(1, 6)
msg = "Roll a dice!"
dice = "The dice you rolled are: "

#shows the message before the 2 dice rolls
print("Hello World!" + " " + msg)

# No need to manually seed; Python handles it on import
for i in range(1):
    print (dice) + (i, random.randint(1, 6), sep=(", "))