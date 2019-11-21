#Lase kasutajal sisestada arvud ning salvesta need muutujasse, samuti muuda kohe stringid numbriteks - int()
number1 = int(input("Sisesta esimene number: "))
number2 = int(input("Sisesta teine number: "))
number3 = int(input("Sisesta kolmas number: "))

#kasutan andmetüüpi "array", et salvestada numbrid üheks muutujaks
numberArray = [number1, number2, number3]

#lisan summa funktsiooni "numberArray" listile ja salvestan need muutujasse "summary"
summary = sum(numberArray)

#kasutan tingimuslauset, et kontrollida, kas sisestatud andmed on võrdsed(tõene) või ei ole võrdsed(väär)
#kui tingimus on õige, siis prindi välja numbrite korrutis
if number1 == number2 and number1 == number3:
    print((number1 * number2) * number3)
    
#kui tingimus on väär, siis prindi välja muutuja "summary", kus me tegime liitmise juba ära
elif number1 != number2 and number1 != number3:
    print(summary)
    





