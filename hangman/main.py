import random
import os
import time
# let hangman = [" 
# ____
# |/   |
# |   
# |    
# |    
# |    
# |
# |_____
# ";
# "
#  ____
# |/   |
# |   (_)
# |    
# |    
# |    
# |
# |_____
# ";
# "
#  ____
# |/   |
# |   (_)
# |    |
# |    |    
# |    
# |
# |_____
# ";
# "
#  ____
# |/   |
# |   (_)
# |   \|
# |    |
# |    
# |
# |_____
# ";
# "
#  ____
# |/   |
# |   (_)
# |   \|/
# |    |
# |    
# |
# |_____
# ";
# "
#  ____
# |/   |
# |   (_)
# |   \|/
# |    |
# |   / 
# |
# |_____
# ";
# "
#  ____
# |/   |
# |   (_)
# |   \|/
# |    |
# |   / \
# |
# |_____
# ";
# "
#  ____
# |/   |
# |   (_)
# |   /|\
# |    |
# |   | |
# |
# |_____
# "]
hanglist = ["stephen", "sam", "code"]
klist = []
# for i in range(len (hanglist)):
#     print(hanglist[i])
#     time.sleep(1)
#     index = i
for word in hanglist:
    for i in range(len(word)):
        index = i
        print("_ ", end="")
        
    print()

while True:
    guessed = input("guess: a")