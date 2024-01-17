import random

print("Welcome to the HANGMAN GAME")
print("In this game, there is a list of words present, \nout of which our interpreter will choose 1 random word. \nThe user first has to input their names and then, will be asked to guess any alphabet. \nIf the random word contains that alphabet, it will be shown as the output(with correct placement) else the program will ask you to guess another alphabet. \nThe user will be given 12 turns(which can be changed accordingly) to guess the complete word.")
name=input("Please enter your name:")
print("Lets play Hangman")
print("Best Of Luck!!!", name)

words = ['rainbow', 'computer', 'science', 'programming', 
         'air', 'play', 'game', 'mathematics', 'player', 'condition', 
         'reverse', 'water', 'fire', 'player']
word=random.choice(words)


print('\nGuess the characters')
guesses=''

turns=12

if replay==1:
    while turns>0:
        failed=0
        for char in word:
            if char in guesses:
                print("\n",char,end='')
            else:
                print('_')
                failed+=1
        
        
        if failed == 0:
            print('\nYOU WIN!!!:)')
            
            print("\nThe Word is :",word)
            break
        print()
        guess=input("\nGuess a character:")
        guesses+=guess
        
        
        if guess not in word:
            turns-=1
            print("Wrong Guess")
            print("You Have" ,+turns ,"More Guesses")
        
        
        if turns==0:
            print("\nYOU LOSE!!!!!:|")
replay=input("Do you want to play again? (type 1 if 'yes')")
