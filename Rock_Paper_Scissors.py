#!/usr/bin/env python
# coding: utf-8

# In[22]:


import random


# In[23]:


choices=["rock","paper","scissors"]
#We define all possible choices


# In[24]:


computer=random.choice(choices)
#We make the computer pick at random one of the available choices


# In[25]:


player = None
#We declare player as a global variable

while player not in choices:
    player=input("rock, paper or scissors? :").lower()
    #We make it so you can only pick Rock Papper or scrissors
    #we use the .lower method so the user cannot input Capitalized or upper cased choises


# In[26]:


#we define the logic behind the game
if player == computer:  
    print(f"Computer picked : {computer}")
    print(f"You picked : {player}")
    print("Tie!")
#equality
elif player == "rock":
    if computer == "paper":
        print(f"Computer picked : {computer}")
        print(f"You picked : {player}")
        print("Sorry, you lost!")
    if computer == "scissors":
        print(f"Computer picked : {computer}")
        print(f"You picked : {player}")
        print("Yay, you won!")
elif player == "paper":
    if computer == "scissors":
        print(f"Computer picked : {computer}")
        print(f"You picked : {player}")
        print("Sorry, you lost!")
    if computer == "rock":
        print(f"Computer picked : {computer}")
        print(f"You picked : {player}")
        print("Yay, you won!")
elif player == "scissors":
    if computer == "rock":
        print(f"Computer picked : {computer}")
        print(f"You picked : {player}")
        print("Sorry, you lost!")
    if computer == "paper":
        print(f"Computer picked : {computer}")
        print(f"You picked : {player}")
        print("Yay, you won!")
#differences


# In[28]:


play_again=input("Would you like to play again (Yes/No) : ").lower()


# In[33]:


#Now all we have to do it put it togheter
import random

def playGame():
    while True:
        choices=["rock","paper","scissors"]
        computer=random.choice(choices)
        player = None
        while player not in choices:
            player=input("rock, paper or scissors? :").lower()
        if player == computer:  
            print(f"Computer picked : {computer}")
            print(f"You picked : {player}")
            print("Tie!")
        elif player == "rock":
            if computer == "paper":
                print(f"Computer picked : {computer}")
                print(f"You picked : {player}")
                print("Sorry, you lost!")
            if computer == "scissors":
                print(f"Computer picked : {computer}")
                print(f"You picked : {player}")
                print("Yay, you won!")
        elif player == "paper":
            if computer == "scissors":
                print(f"Computer picked : {computer}")
                print(f"You picked : {player}")
                print("Sorry, you lost!")
            if computer == "rock":
                print(f"Computer picked : {computer}")
                print(f"You picked : {player}")
                print("Yay, you won!")
        elif player == "scissors":
            if computer == "rock":
                print(f"Computer picked : {computer}")
                print(f"You picked : {player}")
                print("Sorry, you lost!")
            if computer == "paper":
                print(f"Computer picked : {computer}")
                print(f"You picked : {player}")
                print("Yay, you won!")
                
        play_again=input("Would you like to play again (Yes/No) : ").lower()
        
        if(play_again)!="yes":
            break


# In[34]:


playGame()


# In[35]:


#Let's make a version with no if statements when deciding who wins


# In[47]:


import random

while True:
    choices=["rock","paper","scissors"]
    computer=random.choice(choices)
    player = None
    while player not in choices:
        player=input("rock, paper or scissors? :").lower()
        
    choicesDict={"rock":0,"paper":1,"scissors":2}
    
    playerIndex=choicesDict.get(player)
    computerIndex=choicesDict.get(computer)
    
    resultMatrix=[[0,2,1],
                  [1,0,2],
                  [2,1,0]]
    
    resultIdx=resultMatrix[playerIndex][computerIndex]

    resultMsg=[f"\nYou picked: {player} \n Computer picked: {computer} \n It's a tie!",
               f"\nYou picked: {player} \n Computer picked: {computer} \n Yay, you won!",
               f"\nYou picked: {player} \n Computer picked: {computer} \n Sorry, you lost!"]
    result=resultMsg[resultIdx]
    
    print(result)
    print()
    play_again=input("Would you like to play again (Yes/No) : ").lower()    
    if(play_again)!="yes":
        break
    


# In[ ]:




