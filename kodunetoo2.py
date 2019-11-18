number = int(input("Kirjutage siia üks number: "))

if number % 2 == 0 and number < 6:
    print("Sobib")
elif number % 2 == 0 and number > 6 and number < 21:
    print("Ei sobi")
elif number % 2 == 0 and number > 21:
    print("Sobib")
else:
    print("Ei sobi")