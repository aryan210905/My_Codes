# import random
# from collections import Counter

# print("Welcome to hangman!!")
# print("You need to guess the word")

# def chooseWord():
#     # Choosing a random word
    
#     # l = ["Tiger","Panda","Lion","Dog","Cat","Cow","Goat"]
    
#     # word = random.choice(l)
#     word = "panda"
#     word = word.lower()
#     print(f"You have a {len(word)} letter word and you have {len(word)} lives")
#     return word

# word = chooseWord()

# # Create a list of characters of word
# l2 = list(word)
# lives = len(l2)

# # taking input letters
# ans = []
# available = ["_"] * l2
# l3 = l2.copy()
# for i in range(len(l2)):
#     available.append("_") 
# while Counter(ans)!=Counter(l2):
#     ch = input("\nEnter a character: ").lower()
#     if len(ch) != 1 or (not ch.isalpha()):
#         print("Enter only valid characters")
#         continue
#     if ch in l2:
#         if ans.count(ch) != l2.count(ch):
#             print(f"{ch} is present in the word! Keep Going!")
            
#             if(l3.count(ch)>1):
#                 for i in range(l3.count(ch)):
#                     idx = l3.index(ch)
#                     available[idx] = l3[idx]
#                     l3.pop(idx)
#             else:
#                 idx = l3.index(ch)
#                 available[idx] = l3[idx]
#                 l3.pop(idx)
#             ans.append(ch)         
#             if Counter(ans)==Counter(l2):
#                 print(f"\nYou won! Your word was {word}")
#                 break
#             s2 = ""
#             for i in range(len(available)):
#                 s2 = s2 + available[i]
#             print(s2)
#         elif ans.count(ch) >= l2.count(ch):
#                 print("\nYou have already guessed all occurances of this character")
#     else:
#         lives -= 1
#         print(f"\nThat is a wrong character.You have {lives}/{len(l3)} lives left")
#         if lives==0:
#             print(f"\nYou lost. The word was {word}")
#             break

import random
print("Welcome to hangman!!")
print("You need to guess the word")

def chooseWord():
    # Choosing a random word
    l = ["Tiger", "Panda", "Lion", "Dog", "Cat", "Cow", "Goat"]
    word = random.choice(l)
    word = word.lower()
    print(f"You have a {len(word)} letter word and you have {len(word)} lives")
    return word

word = chooseWord()

# Create a list of characters of word
l2 = list(word)
lives = len(l2)

# Taking input letters

available = ["_"] * len(l2)

while "_" in available:
    ch = input("\nEnter a character: ").lower()
    if len(ch) != 1 or (not ch.isalpha()):
        print("Enter only valid characters")
        continue

    if ch in l2:
        if available.count(ch) != l2.count(ch):
            print(f"{ch} is present in the word! Keep Going!")
            for idx, letter in enumerate(l2):
                if letter == ch and available[idx] == "_":
                    available[idx] = ch
            
            print(" ".join(available))
            if "_" not in available:
                print(f"\nYou won! Your word was {word}")
                print(" ".join(available))
                break
            
        else:
            print("\nYou have already guessed all occurrences of this character")
    else:
        lives -= 1
        print(f"\nThat is a wrong character. You have {lives}/{len(word)} lives left")
        if lives == 0:
            print(f"\nYou lost. The word was {word}")
            break
