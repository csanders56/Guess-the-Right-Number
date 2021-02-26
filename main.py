# Generate your questions & answers below:

import random

guess = int(input("Guess a number between 1-20: "))

number = random.randint(1, 21)



while number != "guess":
  
  
  if guess < number:
    print("Too Low")
    guess = int(input("Guess a number between 1-20: "))
    

  elif guess > number:
    print("Too High")
    guess = int(input("Guess a number between 1-20: "))
      
  else:
    print("You choice the right number")

    break


  

