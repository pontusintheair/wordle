import SwedishWordle
from collections import Counter

from update_words_in_game import update_words_in_game

game = SwedishWordle.Game(5)

words_in_game = game.words_in_game

def make_guess_counter(words_in_game):
  # Figure out the counts first     
  counts = Counter()
  for word in words_in_game:
    counts.update(word)
  # Now score the words based on their counts     
  # This will be a list of tuples (score, word)     
  word_scores = []
  for word in words_in_game:
    unique_chars = set(word)
    word_score = sum([counts.get(c) for c in unique_chars])
    word_scores.append((word_score, word))
  # Sort the list and pick the highest score     
  return sorted(word_scores, reverse=True)[0][1]
words_in_game = update_words_in_game