# Program 1:
# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants 
# in the input 
# ex. input: Bahala kayo dyan
# output: words: 3
#         vowels: 6
#         consonants: 8

def vowelsConsonantsCounter():
    global consonantCount
    global vowels
    global words
    consonantCount = 0
    vowels = 0
    askSentence = input("Enter a sentence: ")
    for i in askSentence:    
        if(i == "b" or i ==  "B" or i == "c" or i == "C" or i == "d" or i == "D" or i == "f" or i == "F" or i == "g" or i == "G" or i == "h" or i == "H" or i == "j" or i == "J" or i == "k" or i == "K" or i == "l" or i == "L" or i == "m" or i == "M" or i == "n" or i == "N" or i == "p" or i == "P" or i == "q" or i == "Q" or i == "r" or i == "R" or i == "s" or i == "S" or i == "t" or i == "T" or i == "v" or i == "V" or i == "w" or i == "W" or i == "x" or i == "X" or i == "y" or i == "Y" or i == "z" or i == "Z"):
            consonantCount = consonantCount + 1 # to count consonants
        elif(i == "a" or i == "A" or i == "e" or i == "E" or i == "i" or i == "I" or i == "o" or i == "O" or i == "u" or i == "U"):
            vowels = vowels + 1 # to count vowels
    words = len(askSentence.split()) # to count words

vowelsConsonantsCounter()
print(f"Consonants = {consonantCount} \nVowels = {vowels}\nWords: {words}")
input("Program finished")