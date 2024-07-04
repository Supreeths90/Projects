import random

def guess_number(guess_num):
  
  while True:
    num=random.randint(1,10)
    if guess_num == num:
      print("Yoohoo You Guessed Right")
      break
    else:
      print("Wrong Guess, The number was{}".format(num))
      guess_num = int(input("Enter your guess: "))

guess_num = int(input("Enter your guess number: "))
guess_number(guess_num)