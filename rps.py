#!/usr/bin/env python3
#Title: RPS
#Author: MyTH

import random
import time

Computer_choice = [ "R", "S", "P" ]

name = input("\nHi! Whats your name?...")
print("Hey",name,"wanna play a game?")
time.sleep(1.0)
print("\nLet's play (R)ock (P)aper (S)cissors. Where ; rock beats scissors, paper beats rock and scissors beats paper")
time.sleep(1.0)
print("\nFive(5) rounds to go")
time.sleep(1.0)

player_score = 0
computer_score = 0

print("\n"+name+"'s score:", player_score)
time.sleep(0.5)
print("Computer's score:", computer_score)
time.sleep(1.0)

game_time = [0, 0, 0, 0, 0]

while True:
    for rounds_time in game_time:
        print("\nPick...")
        time.sleep(0.5)
        print("(R) for Rock")
        time.sleep(0.5)
        print("(P) for Paper")
        time.sleep(0.5)
        print("(S) for Scissors")
        Player = input(": ")
        Computer = random.choice(Computer_choice)

        if Player == Computer :
            print("\nComputer:", Computer)
            time.sleep(0.5)
            print("We have a Tie")
            time.sleep(0.5)
            game_time.append(0)
            print(name+"'s score:", player_score)
            time.sleep(0.5)
            print("Computer's score:", computer_score)
            time.sleep(1.5)

        elif Player == "R" :
            if Computer == "S" :
                print("\nComputer: Scissors")
                time.sleep(0.5)
                print("You win this round")
                time.sleep(0.5)
                player_score = player_score + 1
                print(name+"'s score:", player_score)
                time.sleep(0.5)
                print("Computer's score:", computer_score)
                time.sleep(1.5)
            elif Computer == "P" :
                print("\nComputer: Paper")
                time.sleep(0.5)
                print("Computer wins this round")
                time.sleep(0.5)
                computer_score = computer_score + 1
                print(name+"'s score:", player_score)
                time.sleep(0.5)
                print("Computer's score:", computer_score)
                time.sleep(1.5)
            
        elif Player == "S" :
            if Computer == "P" :
                print("\nComputer: Paper")
                time.sleep(0.5)
                print("You win this round")
                time.sleep(0.5)
                player_score = player_score + 1
                print(name+"'s score:", player_score)
                time.sleep(0.5)
                print("Computer-score:", computer_score)
                time.sleep(1.5)
            elif Computer == "R" :
                print("\nComputer: Rock")
                time.sleep(0.5)
                print("Computer wins this round")
                time.sleep(0.5)
                computer_score = computer_score + 1
                print(name+"'s score:", player_score)
                time.sleep(0.5)
                print("Computer's score:", computer_score)
                time.sleep(1.5)
            
        elif Player == "P" :
            if Computer == "S" :
                print("\nComputer: Scissors")
                time.sleep(0.5)
                print("Computer wins this round")
                time.sleep(0.5)
                computer_score = computer_score + 1
                print(name+"'s score:", player_score)
                time.sleep(0.5)
                print("Computer's score:", computer_score)
                time.sleep(1.5)
            elif Computer == "R" :
                print("\nComputer: Rock")
                time.sleep(0.5)
                print("You win this round")
                time.sleep(0.5)
                player_score = player_score + 1
                print(name+"'s score:", player_score)
                time.sleep(0.5)
                print("Computer's score:", computer_score)
                time.sleep(1.5)
            
        else:
            print("""\nInvalid input!
Input 'R' , 'P' or 'S'""")
            time.sleep(1.0)
            game_time.append(0)

    print("\nGame-Over!")
    time.sleep(1.0)
    if player_score > computer_score :
        print("You win with ",player_score,"-",        computer_score,"against computer")
        time.sleep(1.0)
    elif computer_score > player_score :
        print("Computer wins with",computer_score,"-",player_score,"against you")
        time.sleep(1.0)
        
    print("\nDo you still want to play?")
    answer = input("Yes (Y) or No (N)?: ")
    if answer == "N" or answer == "n" :
        print("\nBye",name+'"!")
        break
    elif answer == "Y" or answer == "y" :
        player_score = 0
        computer_score = 0
        continue
    else:
        print("Invalid input!")
        time.sleep(0.5)
        print("input 'Y' or input 'N'")
        time.sleep(0.5)