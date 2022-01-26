import random
from typing import List


class Hangman:
    """
    Class that manages all the methods and attributes allowing user to play the classic game 'Hangman'.
    """

    def __init__(self):
        """
        Initializes all the class attributes necessary
        then calls the spaces_display() and start_game() methods.
        """
        self.playing: bool = True
        self.possible_words: List[str] = ['becode', 'learning', 'mathematics', 'sessions', 'agreement', 'analysis',
                                          'equation', 'operation', 'computer', 'science', 'algorythm', 'probability',
                                          'intelligence', 'binary', 'keyboard', 'spreadsheet', 'function',
                                          'parameters', 'hexadecimal', 'pythonic', 'docstrings', 'machine',
                                          'artificial', 'traceback', 'boolean', 'bootcamp', 'Bouman']
        self.word_to_find: List[str] = [letter for letter in random.choice(self.possible_words)]
        self.correctly_guessed_letters: List[str] = []
        self.wrongly_guessed_letters: List[str] = []
        self.lives: int = 5
        self.error_count: int = 0
        self.turn_count: int = 1
        self.spaces_display()
        self.start_game()

    def spaces_display(self):
        """
        Appends to the correctly_guessed_letters list a number of underscore characters
        equals to the number of letters in the word to find.
        """
        for i in range(len(self.word_to_find)):
            self.correctly_guessed_letters += "_"

    def play(self):
        """
        Checks if player's guess is in the word to find and
        updates all the class attributes accordingly.
        """
        guess: str = input("Please choose a letter:\n")
        #  This will check if the input is only 1 letter
        if len(guess) == 1 and guess.lower() in "abcdefghijklmnopqrstuvwxyz":
            if guess.lower() in self.word_to_find:
                self.turn_count += 1
                #  If guess has a match in the word to find, it will find its corresponding
                #  position in the correctly_guessed_letters and replace the underscore with it
                for place in range(len(self.word_to_find)):
                    letter = self.word_to_find[place]
                    if letter == guess:
                        self.correctly_guessed_letters[place] = letter
            elif guess.lower() in self.wrongly_guessed_letters:
                print("You already tried that one.")
                self.play()
            else:
                self.error_count += 1
                self.turn_count += 1
                self.lives -= 1
                self.wrongly_guessed_letters.append(guess)
        else:
            print("Wrong input. Words are made of letters.")
            self.play()

    def start_game(self):
        """
        Displays the word to guess, the letters already tried, the number of errors,
        the score of the player and the present turn and calls the play() method
        until the player loses or until he finds the word.
        """
        while self.playing:
            print("The word to guess: ")
            print(self.correctly_guessed_letters)
            print("\nYou already tried these letters: ", self.wrongly_guessed_letters)
            print(f"You made {self.error_count} errors. You have {self.lives} chances left!")
            print(f"\nTurn {self.turn_count}")
            self.play()
            if self.lives == 0:
                self.game_over()
            #  If no more letter to guess and more than 0 lives = player wins
            if "_" not in self.correctly_guessed_letters:
                self.well_played()

    def game_over(self):
        """
        Displays the correct answer once the player has lost all his lives
        and calls the play_again() method.
        """
        print(f"I'm sorry. Game over... The correct word was '{''.join(self.word_to_find)}'.")
        self.play_again()

    def well_played(self):
        """
        Displays the final score of the player when he correctly guessed the word
        and calls the play_again() method.
        """
        print(f"Well played! You found the word '{''.join(self.word_to_find)}' "
              f"in {self.turn_count} turns with only {self.error_count} errors!")
        self.play_again()

    def play_again(self):
        """
        Asks the player if he wants to play again.
        Calls the __init__() method ad restart the whole game if the answer contains the letter 'y'.
        Any other option will quit the game.
        """
        another_game: str = input("Do you want to play again?\n")
        #  '.lower()' to include potential capital letters
        #  and 'in' so the player can type the full word 'yes' as well
        if "y" in another_game.lower():
            self.__init__()
        else:
            self.playing = False
            print("Thanks for playing Hangman!")
