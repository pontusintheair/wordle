import SwedishWordle
import guess_first
import guess_counter
import guess_NO2
import update_words_in_game
game = SwedishWordle.Game(5)

words_in_game = game.words_in_game

guess_limit = 6

def make_guess(words_in_game):
    a = 2
    while game.num_guesses < guess_limit:
        if len(words_in_game) < 500:
            result = guess_NO2.make_guess_NO2(words_in_game)    
        elif game.num_guesses < guess_limit:
            result = guess_first.make_guess_first(words_in_game)
        else: 
            result = guess_counter.make_guess_counter(words_in_game)      
    words_in_game = update_words_in_game.update_words_in_game(result)
    return result
"""            
        else: 
            result = guess_counter.make_guess_counter(words_in_game)
            return result
"""
    
    
"""
def update_words_in_game(words_in_game, result):
    result = game.Guess(make_guess(words_in_game))
    result # ex  [1,2,0,0,1]
    for r in result: 
        if r == 1 or r == 2:
            words = word for word in words_in_game:


    words = [word for word in words_in_game if game.Guess(word_guess=result) == 1 or game.Guess(word_guess=result) == 2]
    return words
"""