from capture_words import capture_words_from_file
import random


def find_letter_indexes(letter, word):
    indexes = []

    for index, l in enumerate(word):
        if l == letter:
            indexes.append(index)

    return indexes

def convert_word_to_asterisks(word):
    final_word = '*' * len(word)

    return final_word

def check_user_choice(word, user_choice):
    if user_choice in word:
        return True
    
    return False

def get_last_formatted_word(real_word, new_formatted_word, user_choice):
    new_formatted_word = list(new_formatted_word)

    if check_user_choice(real_word, user_choice):
        indexes = find_letter_indexes(user_choice, real_word)

        for index in indexes:
            new_formatted_word[index] = user_choice

    return "".join(new_formatted_word)

def has_user_lost(user_chances):
    if user_chances <= 0:
        return True
    
    return False

def has_user_won(real_word, user_word):
    if real_word == user_word:
        return True
    
    return False
  