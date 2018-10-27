message = input("Please enter your word: ")
new_message = ""
VOWEL = 'aeiou'
for letter in message:
    if letter.lower() in VOWEL:
        new_message = new_message + letter
        print("A new string has been created" , new_message)

print("\nYour message without vowels is :" , new_message)
