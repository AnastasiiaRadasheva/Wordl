import random

words = ["Looma", "Ratas", "Käige", "Sõber", "Laine", "Pagar", "Roosa", "Tunne", "Kalur", "Hinge"]
print('''
         RULES!
You have to guess the word.
You have 6 tries!
If you guess the word, you win!
If you see [ ], it means that the letter is in the right place.
''')
while True:
    randomword = random.choice(words)
    length = len(randomword)

    print(f"The word has {length} letters. Try to guess it!")

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

    answer1 = input("Do you want to continue? (yes/no) ").lower()
    while True:
        if answer1 == "yes":
            break  
        elif answer1 == "no":
            print("Thanks for playing!")
            break
        else:
            print("Please enter 'yes' or 'no'!")
