import random 
import SwedishWordle
from update_words_in_game import update_words_in_game


game = SwedishWordle.Game(5)

words_in_game = game.words_in_game

guess_limit = 6
def make_guess_first(words_in_game):
    words_in_game = game.words_in_game
    while game.num_guesses < guess_limit:
        return random.choice(words_in_game)
words_in_game =update_words_in_game
