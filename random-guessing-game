from random import randint

class Game:

    def start(self):
        print("\nDifficulty Levels --- Easy (1 - 100) | Medium (1 - 200) | Hard (1 - 300)")
        level = input("Choose [E - Easy], [M - Medium], [H - Hard]: ").capitalize()

        if (level == "E"):
            self.__random_num = randint(1, 100)
            self.limit = 100
        elif (level == "M"):
            self.__random_num = randint(1, 200)
            self.limit = 200
        elif (level == "H"):
            self.__random_num = randint(1, 300)
            self.limit = 300
        else:
            print(f"Invalid Value, '{level}'")
            return

        self.guesses = 0
        self.check()


    def check(self):
        while True:
            try:
                user_number = int(input(f"\nGuess the number (1 - {self.limit}): "))
            except:
                raise ValueError ("Value must be 'integer'")
            else:
                if user_number > 0 and user_number <= self.limit:
                    self.guesses += 1

                    if user_number > self.__random_num:
                        print("Lower Number Please")
                    elif user_number < self.__random_num:
                        print("Higher Number Please")
                    else: 
                        print(f"Hurrahhh! Correct Guess...\nTotal no of guesses are: {self.guesses}")
                        self.play_again()
                        break

                else: 
                    print("Invalid Number!")
                    continue
            
    def play_again(self):
        play_again = input("\nDo you want to Play again [Y/N]: ").capitalize()

        if (play_again == "Y"):
            self.start()
        else:
            print("Thanks for Playing...\n")


player1 = Game()
player1.start()
