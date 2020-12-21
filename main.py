import random
from game import *
from capture_words import capture_words_from_file
from messages.lose import show_lose_message
from messages.win import show_win_message
from messages.show_info import show_information
from messages.print_meanings import print_meanings
from playsound import playsound
from PyDictionary import PyDictionary


def main():
    
    dictionary = PyDictionary()

    all_words = capture_words_from_file('./all_words.txt')

    random_chosen_word = random.choice(all_words).lower()
    random_chosen_word_meanings = dictionary.meaning(random_chosen_word)
    
    total_chances = 10
    total_plays = 0

    last_formatted_word = None

    game_over = False

    while not game_over:
        print()

        user_choice = input('Your letter: ')
        total_plays += 1
        
        random_chosen_word_to_asterisks = convert_word_to_asterisks(random_chosen_word)

        if total_plays == 1:
            last_formatted_word = random_chosen_word_to_asterisks

        last_formatted_word = get_last_formatted_word(random_chosen_word, last_formatted_word, user_choice)

        if not check_user_choice(random_chosen_word, user_choice):
            total_chances -= 1

        show_information(total_chances, last_formatted_word)

        if has_user_lost(total_chances):
            show_lose_message(random_chosen_word)
            playsound('./sounds/lose.wav')

            print_meanings(random_chosen_word, random_chosen_word_meanings)

            game_over = True
        
        if has_user_won(random_chosen_word, last_formatted_word):
            show_win_message()
            playsound('./sounds/win.wav')

            print_meanings(random_chosen_word, random_chosen_word_meanings)

            game_over = True
       
main()