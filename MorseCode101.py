import random
import time

codes = {


"a" : ".-",
"b" : "-...",
"c" : "-.-.",
"d" : "-..",
"e" : ".",
"f" : "..-.",
"g" : "--.",
"h" : "....",
"i" : "..",
"j" : ".---",
"k" : "-.-",
"l" : ".-..",
"m" : "--",
"n" : "-.",
"o" : "---",
"p" : ".--.",
"q" : "--.-",
"r" : ".-.",
"s" : "...",
"t" : "-",
"u" : "..-",
"v" : "...-",
"w" : ".--",
"x" : "-..-",
"y" : "-.--",
"z" : "--..",

"A" : ".-",
"B" : "-...",
"C" : "-.-.",
"D" : "-..",
"E" : ".",
"F" : "..-.",
"G" : "--.",
"H" : "....",
"I" : "..",
"J" : ".---",
"K" : "-.-",
"L" : ".-..",
"M" : "--",
"N" : "-.",
"O" : "---",
"P" : ".--.",
"Q" : "--.-",
"R" : ".-.",
"S" : "...",
"T" : "-",
"U" : "..-",
"V" : "...-",
"W" : ".--",
"X" : "-..-",
"Y" : "-.--",
"Z" : "--..",
}

#
#
#

morseLetter = ""
letter = "e"
targetLetter = ""
targetMorse = ""
inputLetter = ""
inputMorse = ""
targetWord = ""
inputWord = ""
whichProgram = 0

letterList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u",
"v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
wordList = ["bird","plane","house","lawyer", "head","blue","red","purple","yellow","tomato,","potato","rabies","kidney","bacon","hippo",
"the","that","in","can","tuna","fish","piano","viola","violin","cello","bass","oboe","vibes","pipe","run","fear","love","hate",
"sand","human","why","what","who","when","where","how","cat","dog","fish","six","seven","single","alone","sad","deep","high",
"sky","words","plural","unique", "royal","loyal","king","queen","court","judge","jury","peer","pier","pear"]
#
#
#

def clearConsole():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def letterPractice():
    print("Enter the morse code equivalent of the letter, exit to exit\n\n\n\n")
    while 1==1:
        targetLetter = random.choice(letterList)
        targetMorse = codes[targetLetter]
        inputMorse = input("   " + targetLetter + "\n\n\n\n")
        if inputMorse == targetMorse:
            clearConsole()
            print("   Correct!\n\n\n\n")
            print(targetMorse + "\n\n\n\n")
        elif inputMorse == "exit":
            break
        else:
            clearConsole()
            print("Incorrect\n\n\n\n")
            print("Answer: " + targetMorse + "\n\n\n\n")
        #random letter generator
    #checks if user input is correct

def wordPractice():
    print("Enter the morse code equivalent of the word, add a space between morse letters, type exit to exit.\n\n\n\n")
    while 1==1:
 #       targetWord = random.choice(wordList)
        targetWord = random.choice(wordList)
        targetMorse = createTargetMorse(targetWord)
        inputMorse = input("   " + targetWord + "\n\n\n\n")
        if inputMorse == targetMorse:
            clearConsole()
            print("   Correct!\n\n\n\n")
        elif inputMorse == "exit":
            break
        else:
            clearConsole()
            print("Incorrect\n\n\n\n")
            print("Answer: " + targetMorse + "\n\n\n\n")
        #random word generator
    #checks if user input is correct

def createTargetMorse(word):
    targetMorse = ""
    for letter in word:
        targetMorse += convertletter(letter)
        targetMorse += " "
    targetMorse = targetMorse[:-1]
    return targetMorse
        

def convertletter(let):
    targetLetter = ""
    if len(let)>1:
        print("Please give a single letter")
    else:
        targetLetter = codes[let]
    return targetLetter

def dictionary():
    print("\n\n\n                     Dictionary\n\n")
    print("a .-         b -...      c -.-.      d -..       e .         f ..-.\n")
    print("g --.        h ....      i ..        j .---      k -.-       l .-..\n")
    print("m --         n -.        o ---       p .--.      q --.-      r .-.\n")
    print("s ...        t -         u ..-       v ...-      w .--       x-..-\n")
    print("y -.--       z --..\n")
    

#
#
#

print("\n\n\n                     WELCOME TO\n\n")
print("  __  __    ____    _____     _____   ______     __    ___    __ ")
print(" |  \/  |  / __ \  |  __ \   / ____| |  ____|   /_ |  / _ \  /_ |")
print(" | \  / | | |  | | | |__) | | (___   | |__       | | | | | |  | |")
print(" | |\/| | | |  | | |  _  /   \___ \  |  __|      | | | | | |  | |")
print(" | |  | | | |__| | | | \ \   ____) | | |____     | | | |_| |  | |")
print(" |_|  |_|  \____/  |_|  \_\ |_____/  |______|    |_|  \___/   |_|\n\n")
print("A Cole Parks Creation (featuring contributions from Alex Skeldon)\n\n\n\n\n\n\n\n\n\n\n")
time.sleep(1)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nwhat would you like to do today?\n\n\n")
whichProgram = input("Enter 1 for letter practice\nEnter 2 for word practice\nEnter 3 for the morse dictionary\n")
clearConsole()
if whichProgram == "1":
    letterPractice()
elif whichProgram == "2":
    wordPractice()
else:
    while whichProgram != "1" or whichProgram != "2":
        if whichProgram == "1":
            letterPractice()
            break
        elif whichProgram == "2":
            wordPractice()
            break
        elif whichProgram == "3":
            dictionary()
        whichProgram = input("Enter 1 for letter practice\nEnter 2 for word practice\n")
