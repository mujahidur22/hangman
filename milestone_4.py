word_list = ["banana", "orange", "strawberry", "apple", "grape"]

class Hangman:
    def __init__(self, word_list, num_lives=5):
        import random
        word = random.choice(word_list)
        self.word = word
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        self.ask_for_input()
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for letter in self.word:
                if letter == guess:
                    self.word_guessed[letter] = guess
            num_letters -= 1
        else:
            num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {num_lives} lives left.")
    
    def ask_for_input(self):
        while True:
            guess = input("Enter a single letter: ")
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in list_of_guesses:
                print("You already tried that letter!")
            else: 
                self.check_guess(guess)
                self.list_of_guesses.append(guess)