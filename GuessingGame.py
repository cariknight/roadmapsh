import random
import time
levels = ['Easy','Medium','Hard']
chances = [10, 5, 3]
def generateNum():
    num = random.randrange(1,100)
    return num
#prompt
def prompt():
    print(f'''Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
''')
    try:
        choice = int(input('Enter your choice: '))
        print(f'''
Great! You have selected the {levels[choice-1]} difficulty level.
Let's start the game!''')
        return choice
    except ValueError:
        print('Invalid choice.')
        prompt()
def main():
    # main game
    decision = 'y'
    while decision != 'n':
        choice = prompt()
        num = generateNum()
        tries = 1
        start = time.time()
        while tries != chances[choice-1]:
            print()
            guess = int(input('Enter your guess: '))
            if guess != num:      
                if guess < num:
                    val = 'greater'
                if guess > num:
                    val = 'less'
                print(f'Incorrect! The number is {val} than {guess}')
            else:
                end = time.time()
                timer = end - start
                print(f'Congratulations! You guessed the correct number in {tries} attempts at {timer:.2f}.')
                break
            tries += 1
        if guess != num:
            print()
            print(f'The correct number is {num}. Better luck next time!')
        # tracking high score
        if guess == num:
            try:
                with open('highScore.txt', 'r') as f:
                    highScore = f.readline().split(' | ')
                    if int(highScore[0]) > tries:
                        highScore = f'{tries} | {timer:.2f}s'
                        with open('highScore.txt', 'w') as f1:
                            f1.write(highScore)
            except FileNotFoundError:
                highScore = f'{tries} | {timer:.2f}s'
                with open('highScore.txt', 'w') as f:
                    f.write(highScore)
                print(f'Your Highest Score: {tries} attempts, {timer:.2f}s')

        decision = input('Wanna play again? [y/n]').lower()
        


if __name__=='__main__':
    main()
    