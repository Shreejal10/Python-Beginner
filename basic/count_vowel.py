inputString = input("Enter a string: ")
inputString = inputString.casefold()

vowels = "aeiou"

# create a dictionary for storing the count of vowels
vowelsData = {}.fromkeys(vowels, 0)


for character in inputString:
    if character in vowels:
        vowelsData[character] += 1

print("Vowel count: ")
for vowel in vowelsData:
    print(vowel, "-", vowelsData[vowel])
