import random

#print(random.randint(1,100))
#print(random.choice([1,2,3,"tops",True]))

num=random.randint(1,20)

while True:
    guess=int(input("guess a no between 1 to 20 :"))


    if guess==num:
        print("you guessed a correct no :")
        break
    elif guess>num:
        print("you guessed a greater no:")
    elif guess<num:
        print("you guessed a smaller no:")
        
