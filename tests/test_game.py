import pytest
from game import *

def test_find_letter_indexes():
    examples = {
        ('l', 'Hello') : [2,3],
        ('o', 'Hello') : [4],
        ('a', 'Abstract') : [5],
        ('Ab', 'Abstract') : [],
        ('c', 'CARROT') : []
    }

    for parameters, result in examples.items():
        letter, word = parameters

        assert find_letter_indexes(letter, word) == result

def test_convert_word_to_asterisks():
    examples = {
        'Hello' : '*****',
        'Strong' : '******',
        'STRANGER' : '********',
        'hell' : '****'
    }

    for parameter, result in examples.items():
        assert convert_word_to_asterisks(parameter) == result

def test_check_user_choice():
    examples = {
        ('hello', 'h') : True,
        ('hello', 'i') : False,
        ('strong', 'g') : True 
    }

    for parameters, result in examples.items():
        word, user_choice = parameters

        assert check_user_choice(word, user_choice) == result

def test_get_last_formatted_word():
    examples = {
        ('hello', '*****', 'l') : '**ll*',
        ('hello', '*****', 'o') : '****o',
        ('hello', '**ll*', 'h') : 'h*ll*',
        ('hello', '*e***', 'l') : '*ell*',
        ('hello', '*****', 'p') : '*****',
        ('hello', '**ll*', 'p') : '**ll*'
    }

    for parameters, result in examples.items():
        real_word, new_formatted_word, user_choice = parameters

        assert get_last_formatted_word(real_word, new_formatted_word, user_choice) == result

def test_has_user_lost():
    examples = {
        10 : False,
        5 : False,
        1 : False,
        0 : True,
        -1 : True,
        -10 : True
    }

    for parameter, result in examples.items():
        assert has_user_lost(parameter) == result

def test_has_user_won():
    examples = {
        ('hello', 'hello') : True,
        ('berry', '*****') : False,
        ('hello', '*ell*') : False,
        ('strong', '******') : False,
        ('strong', 'stron*') : False,
    }

    for parameters, result in examples.items():
        real_word, user_word = parameters

        assert has_user_won(real_word, user_word) == result