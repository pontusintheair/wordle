import SwedishWordle
import Guess

game = SwedishWordle.Game(5)

words_in_game = game.words_in_game 

def word_result_2(result):
    result = game.Guess(Guess.make_guess(words_in_game))
    words_2_list = []
    for i in range(0,5):
        if result[i] == 0:
            words_2_list.append(result[i])
    return words_2_list