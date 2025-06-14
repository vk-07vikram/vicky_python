# 1. print your name 

# print("Hello , my name is vikram!!!!")

# # Ask name and Print 
# name  = input (" What is your name : ") 

# print ("Nice to meet you, " , name)

# #3. sum of two numbber 

# a = 20 
# b = 30 

# sum = a + b

# print ('This sum is: ' , sum)

# # 4. simple calcuter 

# a = int(input("Enter first number : "))
# b = int(input("Enter secound number : "))

# print("addition : " , a + b )
# print("substraction : " , a - b )
# print("multiplication : " , a * b )
# print("division : " , a / b )

# 5. make a vadapav 

# bread = input("Choose Your bread (sado / olili)")
# filling = input("Choose Your filling (potato / batter / onion / chatni )")

# print("Here you silly vadapav: 🍔")

# print("[" + bread + " bread " + filling + " spice silly vadapav 🥵" + " ]") 
 
# rock , paper and scissors game 

import random 

chocies = ["rock" , "paper" , "scissors"]
computer = random.choice (chocies)
player = input("choose rock , paper and scissors : ")
if player  == computer:
 print("😂 it's a tie!!!")
elif (player == "rock" and computer == "scissors") or \
     (player == "paper" and computer == "rock") or \
     (player == "scissors" and computer == "paper"):
    print("🎉✨ You Win.....")
else:
    print("🎉✨ computer win.....")
