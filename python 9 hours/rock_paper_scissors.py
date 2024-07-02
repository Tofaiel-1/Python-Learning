import random 
user_wins = 0
computer_win = 0
options = ['rock','paper','scissors','test']
options[0]

while True:
    user_input = input("Type Rock/paper/Scissors or q to quit:").lower()
    if user_input== "q":
         break
    if user_input not in ["rock","paper","scissors"]:
         continue
    random_number = random.randint
    computer_pick =  options[random_number]
    print("Computer picked ", computer-pick +".")
    if  user_input == 'rock' and computer_pick=='scissors':
         print("Yoou win!")
         user_wins +=1
         continue
    elif  user_input == 'paper' and computer_pick=='rock':
         print("Yoou win!")
         user_wins +=1
         continue
    elif  user_input == 'scissors' and computer_pick=='paper':
         print("Yoou win!")
         user_wins +=1
         continue
    else:
         print("You lost!")
         computer_win +=1
print("Goodbye!")
    