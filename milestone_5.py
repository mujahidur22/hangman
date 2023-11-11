# word_list = ["banana", "orange", "strawberry", "apple", "grape"]

# from hangman.hangman_Template import play_game


class Hangman:
    def __init__(self, word_list, num_lives=5):
        import random
        word = random.choice(word_list)
        self.word = word
        self.word_guessed = ['_'] * len(self.word)
        num_letters = len(set(self.word))
        self.num_letters = num_letters
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        self.ask_for_input()
        
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
            print(f"You have guessed: \n{''.join(self.word_guessed)}")
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            print(f"You have guessed: \n{''.join(self.word_guessed)}")
    
    def ask_for_input(self):
        print(f"The word to guess is: \n{''.join(self.word_guessed)}")
        while True:
            guess = input("Enter a single letter: ")
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else: 
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

def play_game(word_list):
    #num_lives = 5
    game = Hangman(word_list, num_lives=0)
    while True:
        if game.num_lives == 5:
            print("You lost!")
            print(f"The word was {game.word}")
            break
        elif game.num_lives != 0 and game.num_letters == 0:
            print("Congratulations. You won the game!")
            break
        elif game.num_letters > 0:
            print(game.num_letters)
            Hangman.ask_for_input()


if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)