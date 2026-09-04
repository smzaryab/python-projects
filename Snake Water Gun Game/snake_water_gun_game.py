import random

game_values = ["S", "W", "G"]

def game (game_values):
    print("\nPick one of them...")
    user = input("Choose 'S - Snake', 'W - Water', 'G - Gun': ").capitalize()
    comp = random.choice(game_values)

    if (user == "S") or (user == "W") or (user == "G"):
        
        if (user == "S" and comp == "W") or (user == "W" and comp == "G") or (user == "G" and comp == "S"):
            return (f"\nYou choose: {user}\nComputer choose: {comp}\nYou Win!\n")
        elif (user == "S" and comp == "G") or (user == "W" and comp == "S") or (user == "G" and comp == "W"):
            return (f"\nYou choose: {user}\nComputer choose: {comp}\nYou Lose!\n")
        else:
            return (f"\nYou choose: {user}\nComputer choose: {comp}\nMatch Draw!\n")
  
    else:
        return f"Invalid value!...Value must be 'S', 'W', 'G'"


game_result = game(game_values)
print(game_result)


while True:
    user_play = input("Do you want to Play again (y/n): ").lower()

    if (user_play == "y"):
        game_result = game(game_values)
        print(game_result)

    elif (user_play == "n"):
        break
    else:
        print ("Invalid value!")
        break
