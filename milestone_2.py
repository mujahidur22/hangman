import random

word_list = ["banana", "orange", "strawberry", "apple", "grape"]

word = random.choice(word_list)

print(word_list)
print(word)

guess = input("Enter a single letter: ")

if len(guess) == 1 and guess.isalpha() == True:
    print("Good Guess!")
else:
    print("Oops! That is not a valid input.")