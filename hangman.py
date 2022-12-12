from words import words_list
import random


def get_words():
    word = random.choice(words_list)
    return word.upper()


def play(word):
    word_complete = "_", len(word)
    guessed = False
    # list for words
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("---Lets play Hangman---")
    name = input("Enter your name : ")
    print(display_hangman(tries))
    print(word_complete)
    print("\n")

    # while to loop the guess word
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word : ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("letter is already guessed. Try different!! ")
            elif guess not in word:
                print(guess, "wrong guess!!")
                tries = tries - 1
                guessed_letters.append(guess)
            else:
                print(guess, " is in the word!!")
                guessed_letters.append(guess)
                word_as_list = list(word_complete)

                # Indices
                Indices = [i for i, letter in enumerate(word) if letter == guess]
                # iteration for indices

                for index in Indices:
                    word_as_list[index] = guess
                    word_complete = "".join(word_as_list)

                    if "_" not in word_complete:
                        guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            # isalpha() used to check if all are alphabets
            if guess in guessed_words:
                print("You already guesses the word :", guess)
            elif guess != word:
                print(guess, "is not in the word")
                tries = tries - 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_complete = word

        else:
            print("Invalid Guess !!!")
            print(display_hangman(tries))
            print(word_complete)
            print("\n")

    if guessed:
        print("Congrats !!! ", name, " you guess the word! You Win!!!")
        print("the word was - ", word)
    else:
        print("Sorry, you are Hanged...\n")
        print("the word was - ", word)


# display the hangman
def display_hangman(tries):
    stages = [
        # final state: head, torso, both arms, and both legs
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # head, torso, both arms, and one leg
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # head, torso, and both arms
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # head, torso, and one arm
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # head and torso
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # head
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # initial empty state
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]

    return stages[tries]


# Main function
def main():
    word = get_words()
    play(word)
    # Code to play the game again
    while input("Wanna Play Again? (Y/N)").upper() == "Y":
        word = get_words()
        play(word)


# Python File Naming Conventions
if __name__ == "__main__":
    main()
