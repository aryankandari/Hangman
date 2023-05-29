#This was one of my favorite games in childhood
import random
from words import guess_word
import string
from hanged_man import lives_visual_dict

# print(guess_word)

def valid_word(guess_word):

    word = random.choice(guess_word)

    while '-' in guess_word or ' ' in guess_word:
        word = random.choice(guess_word)

    return word.upper()

def hangman():
    word = valid_word(guess_word)
    word_letters = set(word)    #letter in the word
    alphabet = set(string.ascii_uppercase)  #gets all the alphabet in the uppercase
    used_letters = set()    #user guesses this letter

    lives = 7

    #taking user input
    while len(word_letters) > 0 and lives > 0:
        # current status of the hanged man
        print(lives_visual_dict[lives])

        #letters used 
        print("You have", lives,"lives left and you have used these letters:",' '.join(used_letters))

        #status of the current word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        
        print('Current status : ',' '.join(word_list))

        user_letter = input("Guess a letter : ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                # print('')

            else:
                lives = lives - 1   #one life gone when wrong prediction
                print('\nYour letter,', user_letter, 'is not in the word.')


        elif user_letter in used_letters:
            print("\nYou have already uesd that letter. Please try again.")

        else:
            print("\nInvalid character. Please try again.")


    # gets here when len(word_letters) == 0 OR when lives == 0    
    if lives == 0:
        print(lives_visual_dict[lives])
        print("You died, Sorry. The word was ", word)
    else:
        print("You guessed it right buddy,",word,'!!')
        

if __name__ == '__main__':
    hangman()
