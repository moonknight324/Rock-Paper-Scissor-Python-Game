import random
options=["Rock", "Paper", "Scissor"]
player_name=input("Enter your name:")
computer_score=0
player_score=0
rounds=0
game_start=True
print("Welcome",player_name)
while rounds<6:
  comp_option=random.choice(options)
  player_option=input("Enter your choice:").title()
  print("Computer option:",comp_option)
  print("Player option:",player_option)
  rounds+=1
  if comp_option==player_option:
    print("It's a Tie!")
  elif (player_option=="Rock" and comp_option=="Scissor") or (player_option=="Scissor" and comp_option=="Paper") or (player_option=="Paper" and comp_option=="Rock"):
    print(player_name,"Won!")
    player_score+=1
  elif (comp_option=="Rock" and player_option=="Scissor") or (comp_option=="Paper" and player_option=="Rock") or (comp_option=="Scissor" and player_option=="Paper"):
    print("Computer Won")
    computer_score+=1
  else:
    print("Enter a valid option")
  print("")
  print("Rounds:",rounds)
  print("")
  print("Score:")
  print(player_name,player_score,end="")
  print(" |","Computer",computer_score)
  print("")
  if rounds==6:
    game_start=False
    break
if player_score==computer_score:
  print("Tie")
elif player_score>computer_score:
  print("Yay!,",player_name,"Won!")
else:
  print("Computer won the game..Better luck next time!")