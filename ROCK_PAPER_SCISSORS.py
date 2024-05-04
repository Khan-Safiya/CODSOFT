def comp_choice(choice):
    if choice==1:
        computer_choice="rock"
    elif choice==2: 
        computer_choice="paper"
    elif choice==3:
        computer_choice="scissors"
    return computer_choice

print("--WELCOME TO THE ROCK-PAPER-SCISSORS GAME--\n")
print("INSTRUCTIONS- You have to choose between rock, paper and scissors. \nAnd the computer will choose a random choice.")
print("It will be a multi-round game. And the winner will be based on addition of all the rounds.")
print("GAME RULE - ROCK BEATS SCISSORS, SCISSORS BEATS PAPER AND PAPER BEATS ROCK.")
print("Exit - to end the game.")
print("Let's start the game!")
c=0
u=0
round=1
while True:
    print(f"Round {round}")
    round+=1

    import random as rd
    choice=rd.randint(1,3)
    computer_choice=comp_choice(choice)

    user_choice=input("Enter your choice[rock/paper/scissors/exit] : ").lower()
    print(f"Computer's choice : {computer_choice}")

    if user_choice=='rock':
        if computer_choice=='rock':
            print("It's a tie!")
            
        elif computer_choice=='paper':
            print("You lose! Computer won")
            c+=1
            
        elif computer_choice=='scissors':
            print("You win!")
            u+=1
        continue

    elif user_choice=='paper':
        if computer_choice=='rock':
            print("You win!")
            u+=1
            
        elif computer_choice=='paper':
            print("It's a tie!")
            
        elif computer_choice=='scissors':
            print("You lose! Computer won")
            c+=1
        continue

    elif user_choice=='scissors':
        if computer_choice=='rock':
            print("You lose! Computer won")
            c+=1
            
        elif computer_choice=='paper':
            print("You win!")
            u+=1
            
        elif computer_choice=='scissors':
            print("It's a tie!")
        continue

    elif user_choice=='exit':
        print(f"Your score: {u}\nComputer's score: {c}")
        print("Thank you for playing!")
        if u>c:
            print("You won the game!")
        elif c>u:
            print("Computer won the game!")
        else:
            print("It's a tie!")
        break

    else:
        print("Invalid choice! Try again...")
        continue
