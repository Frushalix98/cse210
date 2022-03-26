import random
from this import d
from wordListJumper import word_list

def word_getter():
    word = random.choice(word_list)
    return word.upper()

def order_of_operations(word):
    full_word = "_" * len(word)
    correctly_guessed = False
    letter_guesses = []
    attempts = 6
    print(f'You have {attempts} tries left \n')
    print(full_word)
    print("\n")
    while not correctly_guessed and attempts > 0:
        player_guess = input("Please guess a letter (a-z): ").upper()
        if len(player_guess) == 1 and player_guess.isalpha():
            if player_guess in letter_guesses:
                print("You guessed that already. Do something else: \n")
            elif player_guess not in word:
                print(player_guess, " is not in the word.")
                attempts -= 1
                letter_guesses.append(player_guess)
            else:
                print(f"{player_guess}  is in the word")
                letter_guesses.append(player_guess)
                stretched_word = list(full_word)
                index_finder = [i for i, letter in enumerate(word) if letter == player_guess]
                for index in index_finder:
                    stretched_word[index] = player_guess
                full_word = "".join(stretched_word)
                if "_" not in full_word:
                    correctly_guessed = True
        else:
            print('Try a guess within A-Z: ')
        print(f'You have {attempts} tries left \n')
        print(full_word)
        print("\n")
    if correctly_guessed == True:
        print("Good game!")
    else:
        print(f"Sorry, the word was " + word+ ", you are out of tries.")

def main():
    word = word_getter()
    order_of_operations(word)

main()