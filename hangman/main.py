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
    guessed_word = ["_"] * len(word)s
    print(" ".join(guessed_word))
        
    print()

while True:
    guessed = input("guess: ")