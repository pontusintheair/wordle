import json
import os, sys
import random
import re

def solve_for_words():
    valid_words = wordlist
    while True:
        guess = make_guess(valid_words)
        print("Guess: " + guess())
        result = collect_result()
        if result == correct:
            print("I won!")
            break
    valid_words= update_valid_words(valid_words, guess, result)

def make_guess(valid_words):
    return random.choice(valid_words)

def collect_result():
  # Collect the result of our guess from the user
  result = input("What's the result? (_/1/2) ")
  match = re.match(r'^[21_]{5}$', result)
  if not match:
    print("Invalid response string, try again")
    return collect_result()
  return result

def get_result(guess, answer):
  # Given a guess and a known answer, return the result
  result = ""
  for pos, ch_guess, ch_answer in zip(range(5), guess, answer):
    if ch_guess == ch_answer:
      result += "2"
    elif ch_guess not in answer:
      result += "_"
    else:
      result += "1"
  return result
  
def update_valid_words(valid_words, guess, result):
  return [word for word in valid_words if get_result(guess, word) == result]