import SwedishWordle
import Guess
import update_words_in_game

game = SwedishWordle.Game(5)
# det finns en bugg i SwedishWrdle du behöver fixa 
# om ordet är vänta och du gissar på banan ger spelet [0,1,2,1,1]

words_in_game = game.words_in_game

guess_limit = 6

while game.num_guesses < guess_limit:
    guess = Guess.make_guess(words_in_game)
    result = game.Guess()
    words_in_game = update_words_in_game.update_words_in_game(result)
    print(f'Du gissade {Guess.make_guess(words_in_game)}. ' + f'Det resulterade i {result}. ')
    print(game.num_guesses)
    if result == [2,2,2,2,2]:
        print ("I won !!!")
        break





