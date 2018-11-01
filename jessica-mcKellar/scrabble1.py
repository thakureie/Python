#!/usr/bin/python
import scrabble

word = "radar"
is_plaindrome = True
for index in range(len(word)):
  if word[index] != word[-(index + 1)]:
    is_panidrome=False
print(is_palindrome)
