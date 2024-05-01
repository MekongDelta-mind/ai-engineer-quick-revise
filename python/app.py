# from math import *
import math as m 

# drawing a shape
# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|")


# variables and data types

# ## without var
# print("There once was a man named George, ")
# print("he was 70 yaers old. ")
# print("He really liked the name John, ")
# print("but didn't like being 70.")

# with var
# character_name = "George"
# character_age = "35"

# print(f"There once was a man named {character_name}, ")
# print(f"he was {character_age} yaers old. ")
# print(f"He really liked the name {character_name}, ")
# print(f"but didn't like being {character_age}.")

## updating the var mid way
# character_name = "George"
# character_age = "35"

# print(f"There once was a man named {character_name}, ")
# print(f"he was {character_age} yaers old. ")
# character_name = "Minion"
# print(f"He really liked the name {character_name}, ")
# print(f"but didn't like being {character_age}.")


# datatypes:
## string
## numbers: int, float
## boolean: 

# working wiht strings

# print("Giraffe \n Academy")
# #Giraffe 
# # Academy


# phrase = "Giraffe Academy"
# print(phrase + "is cool")
# #Giraffe Academyis cool

# # common string functions
# phrase = "Giraffe Academy"
# print(phrase.lower())
# print(phrase.upper())
# print(phrase.isupper())
# print(phrase.islower())
# print(phrase.upper().isupper())
# print(phrase.lower().islower())
# print(len(phrase))
# print(phrase[4:10])
# print(phrase.index("ff"))
# print(phrase.replace("Giraffe","Deer"))


# working with numbers:

# print(3+ 4.5)
# print(3 * 4.5)
# print(3 * 4 + 5)
# print( 3 * (4+5) )

# print( 10 % 3)
# print( 10 // 3)
# print( 10 / 3)

# my_num = 7
# print(my_num)
# print(str(my_num) + " my fav number")

my_num = -7
print(abs(my_num))
print(pow(abs(my_num),2))
print(max(4,6))
list_num = [4,6]
print(max(list_num))
print(min(list_num))
print(round(3.45))

# from math import * 
decimal_num = 3.45
print(m.floor(decimal_num))
print(m.ceil(decimal_num))
print(m.sqrt(49))
