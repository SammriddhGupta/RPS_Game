#coding=utf-8

import random

winner = False
valid_moves = ["rock", "paper", "scissors"]
state = [""]
winners = []

def ask_move():
  move = input("🤔 What move do you want to play?\n Type rock, paper or scissors!\nMove: ")
  
  if move not in valid_moves:
      print("That is not a valid move")
  else:
    return move
  
def most_common(list):
  rock_count = 0
  paper_count = 0
  scissors_count = 0

  for move in list:
    if move == "rock":
      rock_count += 1 
    elif move == "paper":
      paper_count += 1
    elif move == "scissors":
      scissors_count += 1
    
  if rock_count >= scissors_count and rock_count >= paper_count:
    return "rock"
  elif paper_count >= rock_count and paper_count >= scissors_count:
    return "paper"
  else:
    return "scissors"

def make_move():
  number = len(state) % 3
  catchphrases = [ "Bazinga!" , "Yee-haw!" , "suck it loser"]
  print(catchphrases[number])
  last_move = state[-1]
  
  if random.randint(0,1)==0:
    if most_common(state)=="rock":
      move="paper"
    elif most_common(state)=="paper":
      move="scissors"
    else:
      move="rock"
  else:
    move=random.choices(valid_moves)
  return move
  
def check_winner(player_move, computer_move):
  if player_move == computer_move:
    return "draw"
  
  elif player_move == "rock":
    if computer_move == "scissors":
      return "player"
    else:
      return "opponent"
    
  elif player_move == "paper":
    if computer_move == "rock":
      return "player"
    else:
      return "opponent"
      
  elif player_move == "scissors":
    if computer_move == "paper":
      return "player"
    else:
      return "opponent"

def most_common(list):
  return max(set(list), key=list.count)

while not winner:
  player_move = ask_move()
  computer_move = make_move()
  
  state.append(player_move)
  
  round_winner = check_winner(player_move, computer_move)
  
  if round_winner == "player":
    print("🏆 Congratulations, you won!")
  elif round_winner == "opponent":
    print("❌ Oh no! You lost!")
  else:
    print("🏁 You drew with your opponent! It's a tie!")
  
  winners.append(round_winner)
  
  if len(winners) == 5:
    winner = most_common(winners)
    print("🎉 The winner of the five games was: {}".format(winner))
