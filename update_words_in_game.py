import word_result_0
import word_result_2
import word_result_1

import SwedishWordle

game = SwedishWordle.Game(5)
words_in_game = game.words_in_game
"""
result = game.Guess(Guess.make_guess)
"""

def update_words_in_game(result):
    wrong_letters = word_result_0.word_result_0(result)
    partial_letters = word_result_1.word_result_1(result)
    correct_letters = word_result_2.word_result_2(result)
    good_letters = []
    for g in correct_letters:
        good_letters.append(g)
    for p in partial_letters:
        good_letters.append(p)
    
    for w in wrong_letters:
        if w in good_letters:
            good_letters.append(w)

    new_words_in_game =[]
    for word in words_in_game:
        for good in good_letters:
            if str(good) in str(word):
                new_words_in_game.append(word)
    
    return new_words_in_game