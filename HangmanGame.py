import random


def hangman():
    words_list = ["Ware", "Beware", "Weak", "franchise", "refund", "telecom", "Refund", "Recorder", "towns", "hunt",
                  "Use", "complaints", "environments", "angles", "Towns", "facing", "divided", "deputy", "Environments",
                  "promotions", "customize", "indicators", "Tremble", "passion", "tradition", "physicians", "Divided",
                  "maintaining", "candy"]

    word = random.choice(words_list)
    attempt = 10
    guesses_made = ''
    valid_entry = set('abcdefghijklmnopqrstuvwxyz')

    while len(word) > 0:
        game_word = ""

        for letter in word:
            if letter in guesses_made:
                game_word = game_word + letter
            else:
                game_word = game_word + "_ "

        if game_word == word:
            print(game_word)
            print("Congrats!!! you guessed correctly.")
            break

        print("Guess the word: ", game_word)
        guess = input()

        if guess in valid_entry:
            guesses_made = guesses_made + guess
        else:
            print("enter valid character")
            guess = input()

        if guess not in word:
            attempt = attempt - 1

            if attempt == 9:
                print("Attempt left: 9")
                print("---------------------")

            if attempt == 8:
                print("Attempt left: 8")
                print("---------------------")
                print("           O         ")

            if attempt == 7:
                print("Attempt left: 7")
                print("---------------------")
                print("           O         ")
                print("           |         ")

            if attempt == 6:
                print("Attempt left: 6")
                print("---------------------")
                print("           O         ")
                print("           |         ")
                print("          /          ")

            if attempt == 5:
                print("Attempt left: 5")
                print("---------------------")
                print("           O         ")
                print("           |         ")
                print("          / \        ")

            if attempt == 4:
                print("Attempt left: 4")
                print("---------------------")
                print("          \O         ")
                print("           |         ")
                print("          / \        ")

            if attempt == 3:
                print("Attempt left: 3")
                print("---------------------")
                print("          \O/        ")
                print("           |         ")
                print("          / \        ")

            if attempt == 2:
                print("Attempt left: 2")
                print("---------------------")
                print("          \O/ |      ")
                print("           |         ")
                print("          / \        ")

            if attempt == 1:
                print("Last Attempt!!!")
                print("---------------------")
                print("          \O/_|      ")
                print("           |         ")
                print("          / \        ")

            if attempt == 0:
                print("You are hanged!!!")
                print("---------------------")
                print("           O_|      ")
                print("          /|\        ")
                print("          / \        ")
                break


p_name = input("Enter your Name: ")
print("Welcome,", p_name, "!!!")
print("------------------------------------------------")
print("Guess the word in less than 10 attempts")
hangman()
