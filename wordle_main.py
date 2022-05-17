import random
import re
from collections import Counter
import SwedishWordle





game = SwedishWordle.Game(5)

guess1 = ("JAGAD")

result1 = game.Guess(guess1)

print(str(result1))

def solve():
  valid_words = wordlist
  while True:
    guess = make_guess(valid_words)
    print("Guess: " + guess.upper())
    result = collect_result()
    if result == correct:
        print("I won!")
        break
    valid_words = update_valid_words(valid_words, guess, result)

def make_guess(valid_words):
  # Räknar counts      
  counts = Counter()
  for word in valid_words:
    counts.update(word)
  # Ranka orden på deras counts    
  # lista av tuples (score, word)     
  word_scores = []
  for word in valid_words:
    unique_chars = set(word)
    word_score = sum([counts.get(c) for c in unique_chars])
    word_scores.append((word_score, word))
  # sortera listan och ta högsta värdet     
  return sorted(word_scores, reverse=True)[0][1]

 
def collect_result():
  # Collect the result of our guess from the user
  result = input("What's the result? (_/?/!) ")
  match = re.match(r'^[!?_]{5}$', result)
  if not match:
    print("Invalid response string, try again")
    return collect_result()
  return result

def get_result(guess, answer):
  # Given a guess and a known answer, return the result
  result = ""
  for pos, ch_guess, ch_answer in zip(range(5), guess, answer):
    if ch_guess == ch_answer:
      result += "!"
    elif ch_guess not in answer:
      result += "_"
    else:
      result += "?"
  return result
  
def update_valid_words(valid_words, guess, result):
  return [word for word in valid_words if get_result(guess, word) == result]
  