import random
ranNum = random.randrange(100 , 1000)

#we want the game to keep completing the game: use while loop
#back to 4.5 to see the map of the for loop
#while loop structure is on

flag = True #give sth new
#change while true to while flag
while flag:    #will completegoing for ever its loop
    playerGuess = int(input("please guess a 3-digits numbers"))

    print("The number is ")
    if playerGuess < ranNum:
        print("higher")
    elif playerGuess > ranNum:
        print("LOWER!!")  # greater than 5
    else:
        print("Congrats you won the game")
      #break #stops the loopotherwise it will complete forever.

#you can use break and make while true
#or you can simply make a varilablie called flag and assign it to true
#then while true <___ make it



