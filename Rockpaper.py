import random
flag=True
choices = ["Rock", "paper", "scissor"]
computer_score=0
user_score=0
no_of_draws=0
while flag:
    computer_choice = random.choice(choices)
    computer_choice1 = computer_choice[0]
    computer_choice1=computer_choice1.lower()
    user_choice = input("Enter (R)ock (P)aper or (S)cissors OR Enter (q) to quit :").lower()
    if user_choice=="q":
        print(f"You won {user_score} times")
        print(f"Computer won {computer_score} times")
        print(f"There were {no_of_draws} draws")
        with open('score.txt','w') as score_file:
            score_file.write(f"You won {user_score} times\n")
            score_file.write(f"Computer won {computer_score} times\n")
            score_file.write(f"There were {no_of_draws} draws")
        break
    if user_choice not in ["r", "p", "s"]:
        print("Enter only from options given!")
        continue
    else:
        if computer_choice1=="r" and user_choice=="p":
            print(f"The computer chose {computer_choice}")
            print("YOU WON")
            user_score+=1
        if computer_choice1=="r" and user_choice=="s":
            print(f"The computer chose {computer_choice}")
            print("YOU LOST")
            computer_score+=1
        if computer_choice1=="s" and user_choice=="p":
            print(f"The computer chose {computer_choice}")
            print("YOU LOST")
            computer_score += 1
        if computer_choice1=="s" and user_choice=="r":
            print(f"The computer chose {computer_choice}")
            print("YOU WON")
            user_score += 1
        if computer_choice1=="p" and user_choice=="r":
            print(f"The computer chose {computer_choice}")
            print("YOU LOST")
            computer_score += 1
        if computer_choice1=="p" and user_choice=="s":
            print(f"The computer chose {computer_choice}")
            print("YOU WON")
            user_score += 1
        if computer_choice1==user_choice:
            print("DRAW")
            no_of_draws+=1