import random

print("---- Welcome to the Game of Cricket ----")

print("\nInstructions:")
print("1. You have to select any number from 1 to 6.")
print("2. The computer will also select a number.")
print("3. While batting, if your number and computer's number are different, you'll add to your runs.")
print("   If they are the same, you'll lose a wicket.")
print("4. While bowling, if your number and computer's number are different, the computer adds to its runs.")
print("   If they are the same, the computer loses a wicket.")
print("5. Each player will get 2 wickets and 2 overs (12 balls) for batting and bowling.")
print("6. The innings will end after either 2 wickets fall or the overs end.")
print("7. The player with the maximum runs wins.")

print("\n---------- Start Game ----------")


toss_result = random.choice(["Heads", "Tails"])
user_toss_choice = input("Choose heads or tails: ").capitalize()
toss_winner = "User" if user_toss_choice == toss_result else "Computer"

print(f"\nToss Result: {toss_result}")
print(f"{toss_winner} won the toss")

if toss_winner == "User":
    user_choice = input("Choose to bat or bowl: ").lower()
    computer_choice = "bowl" if user_choice == "bat" else "bat"
else:
    computer_choice = random.choice(["bat", "bowl"])
    user_choice = "bowl" if computer_choice == "bat" else "bat"

print(f"You chose to {user_choice} and the computer chose to {computer_choice}")


if user_choice == "bat":
    print("\n Innings Begins")
    runs = 0
    wickets = 0
    balls = 0 
    
    while wickets < 2 and balls < 12 :
        try:
            user_input = int(input("Choose any numbers from 1 to 6 :"))
            if user_input < 1 or user_input > 6:
                print("Please choose number from 1 to 6. ")
                continue
            computer_input = random.randint(1,6)
            print(f" Your choice: {user_input} | Computer's choice: {computer_input}")
            if user_input == computer_input:
                wickets += 1
                print("OUT!")
            else:
                runs += user_input

            balls += 1
            if balls % 6 == 0:
                over_number = balls // 6
                print(f"End of Over {over_number} | Score: {runs}/{wickets}")
                
            print(f"Total Score: {runs}/{wickets} | Balls left: {12 - balls}")

        except ValueError:
            print("Invalid input . Enter a number 1 to 6.")
    user_runs = runs
    print(f"\nYour Inning Over. Final Score: {user_runs}/{wickets}")

    print("\nComputer's Innings Begins")
    runs = 0
    wickets = 0
    balls = 0
    while wickets < 2 and balls < 12 and runs <= user_runs:
        try:
            user_input = int(input("Choose any numbers from 1 to 6 :"))
            if user_input < 1 or user_input > 6:
                print("Please choose number from 1 to 6. ")
                continue
            computer_input = random.randint(1,6)
            print(f" Your choice: {user_input} | Computer's choice: {computer_input}")
            if user_input == computer_input:
                wickets += 1
                print(" Computer is OUT!")
            else:
                runs += computer_input

            balls += 1
            if balls % 6 == 0:
                over_number = balls // 6
                print(f"End of Over {over_number} | Score: {runs}/{wickets}")
                
            print(f"Total Score: {runs}/{wickets} | Balls left: {12 - balls}")

        except ValueError:
            print("Invalid input . Enter a number 1-6.")
    
    computer_runs = runs
    print(f"\nComputer's Inning Over. Final Score: {computer_runs}/{wickets} ")
else:
    print("\nComputer's Innings Begins")
    runs = 0
    wickets = 0
    balls = 0
    while wickets < 2 and balls < 12:
        try:
            user_input = int(input("Choose any number from 1 to 6: "))
            if user_input < 1 or user_input > 6:
                print("Please choose a number from 1 to 6.")
                continue
            computer_input = random.randint(1, 6)
            print(f"Your choice: {user_input} | Computer's choice: {computer_input}")

            if user_input == computer_input:
                wickets += 1
                print("Computer is OUT!")
            else:
                runs += computer_input

            balls += 1
            if balls % 6 == 0:
                over_number = balls // 6
                print(f"End of Over {over_number} | Score: {runs}/{wickets}")
            

            print(f"Total Score: {runs}/{wickets} | Balls left: {12 - balls}")

        except ValueError:
            print("Invalid input. Enter a number 1-6.")

    computer_runs = runs
    print(f"\nComputer's Inning Over. Final Score: {computer_runs}/{wickets}")

    print("\nYour Inning Begins")
    runs = 0
    wickets = 0
    balls = 0
    while wickets <2 and balls < 12 and runs <= computer_runs:
        try:
            user_input = int(input("Choose any number from 1 to 6: "))
            if user_input < 1 or user_input > 6:
                print("Please choose a number form 1 to 6: ")
                continue
            computer_input = random.randint(1,6)
            print(f"Your choice : {user_input} | Computer's choice: {computer_input}")


            if user_input == computer_input:
                wickets += 1
                print("OUT")
            else:
                runs += user_input

            balls += 1
            if balls % 6 == 0:
                over_number = balls // 6
                print(f"End of over {over_number} | Score: {runs}/{wickets}")
            
            print(f"Total Score: {runs}/{wickets} | Balls left: {12 - balls}")
        
        except ValueError:
            print("Invalid input. Enter a number 1-6.")
    
    
    user_runs = runs
    print(f"\nYour Innings Over. Final Score: {user_runs}/{wickets}")

print("\n----Result----")
print(f"Your total runs: {user_runs}")
print(f"Computer's total runs: {computer_runs}")

if user_runs > computer_runs:
    print(f"Congratulations! You won the Match by {user_runs - computer_runs} runs.")

elif user_runs < computer_runs:
    print(f"Better luck next time! Computer won the Match by {computer_runs - user_runs} runs.")
else:
    print("The match is tie. No one wins ")








                
