import random

userInput = int(input("Arva ära, mis number tuleb järgmisena (1 - 20): "))
randomNumber = random.randint(1, 20)

if userInput != randomNumber:
    print("Õnn ei olnud sinu poolel, proovi uuesti!")
else:
    print("Pihtas, põhjas! ", userInput, " on õige vastus!")

