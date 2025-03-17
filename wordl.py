from colorama import Fore, Back, Style
import random

words = ["Looma", "Ratas", "Käige", "Sõber", "Laine", "Pagar", "Roosa", "Tunne", "Kalur", "Hinge"]
randomword = random.choice(words)
length = len(randomword)

print('''
         RULES!
You have to guess the word.
You must enter letters from the alphabet.
You have 6 tries!
''')

print(f"The word has {length} letters. Try to guess it!")

attempts = 6  

for j in range(6):
    result = ""
    print(f"Katse {j+1}/6")

    while 1:
        try:
            user = str(input("Your guess: ")).lower()

            if len(user) > length:
                print("Your word is too long! Please enter a word with the correct number of letters.")
            elif len(user) < length:
                print("Your word is too short! Please enter a word with the correct number of letters.")
            elif user.isalpha() == False:
                print("Please enter only letters!")
            elif len(user) == length:
                break
        except:
            print("Please enter a valid word consisting only of letters!")

    for i in range(length):
        if user[i] == randomword[i].lower():
            result += Fore.GREEN + user[i] + Style.RESET_ALL
        elif user[i] in randomword.lower() and user[i] != randomword[i].lower():
            result += Fore.YELLOW + user[i] + Style.RESET_ALL
        else:
            result += "-"

    result += "\n"
    print(result)

    if user == randomword.lower():
        print(f"Palju õnne, te võitsite! Mõeldud sõna on: {randomword}")
        break
else:
    print(f"Te kaotasite! Mõeldud sõna on: {randomword}")
