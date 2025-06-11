import random
computer=random.randrange(1,100)
 #randrange is use to define a range for computer to choose a random number 
print("Enter number")
#Comperision 
while True:
    user=int(input())
    if user>computer: 
      
        print("Your Guess number is too High") 
    elif computer>user: 
  
        print("Your Guess number is too Low ") 
    else: 
        print ("Computer number : " ,computer) 
        print("Your Guess number is equal ! You win !!")
        break

print("Game Over")