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
    print(f"Attempt {j + 1}/6")

    while True:
        user = input("Your guess: ").lower()

        if len(user) > length:
            print("Your word is too long! Please enter a word with the correct number of letters.")
        elif len(user) < length:
            print("Your word is too short! Please enter a word with the correct number of letters.")
        elif not user.isalpha():
            print("Please enter only letters!")
        elif len(user) == length:
            break

    for i in range(length):
        if user[i] == randomword[i].lower():
            result += f"[{user[i]}]" 
        elif user[i] in randomword.lower() and user[i] != randomword[i].lower():
            result += f"({user[i]})"  
        else:
            result += "-"

    result += "\n"
    print(result)

    if user == randomword.lower():
        print(f"Congratulations, you won! The word was: {randomword}")
        break
else:
    print(f"You lost! The word was: {randomword}")
