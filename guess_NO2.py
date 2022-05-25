import SwedishWordle
import Guess
from update_words_in_game import update_words_in_game
game = SwedishWordle.Game(5)

words_in_game = game.words_in_game

def make_guess_NO2(words_in_game):
  guess = None
  lowest_worst_score = len(words_in_game) + 1
  lowest_total_score = len(words_in_game) ** 2
  for possible_guess in words_in_game:
    # First, figure out the worst possible and total/average remaining words for this guess
    worst_score = 0
    total_score = 0
    for possible_answer in words_in_game:
      # reuse our old get_result method from before, nice
      result = game.Guess(Guess.make_guess(words_in_game, possible_answer))
      num_new_words_in_game = len(update_words_in_game(words_in_game, possible_guess, result))
      worst_score = max(num_new_words_in_game, worst_score)
      total_score += num_new_words_in_game
      
    # If this possble guess has a lower total/average number of words remaining, use it instead
    if worst_score < lowest_worst_score:
      guess = possible_guess
      lowest_worst_score = worst_score
      lowest_total_score = total_score
    # If it's a tie in average words remaining, choose the one that doesn't have the worst case
    elif worst_score == lowest_worst_score and total_score < lowest_total_score:
      guess = possible_guess
      lowest_worst_score = worst_score
      lowest_total_score = total_score
  return guess    

