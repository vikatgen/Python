import random

userInput = int(input("Arva ära, mis number tuleb järgmisena (1 - 20): "))
randomNumber = random.randint(1, 20)


if userInput < 1:
    print("Kahjuks sisestasite liiga väikse arvu (1-20), proovi uuesti!")
elif userInput > 20:
    print("Kahjuks sisestasite liiga suure arvu (1-20), proovi uuesti!")
elif userInput != randomNumber:
    print("Õnn ei olnud sinu poolel, proovi uuesti!")
else:
    print("Pihtas, põhjas! ", userInput, " on õige vastus! Sa mõtled peagut nagu arvuti.")

