import random

random_number = random.randint(1, 20)
print(random_number)

random_float = random.random()
print(random_float)

love_score = random.randint(1,100)
print(f"Your love score is %{love_score}")

##############################################################################################
#Heads or Tails
# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲
import random
coin = random.randint(0,1)
if coin == 0:
  print("Tails")
else:
  print("Heads")

##############################################################################################

#Lists
States_of_America = ["Florida", "Georgia", "Delaware", "Alabama", "California"]

print(States_of_America[0])

States_of_America[1] = "New Item"
print(States_of_America)

States_of_America.append("New State")
print(States_of_America)
##############################################################################################
#Banker Roulette
# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
#Get the total number of items in list.
num_items = len(names)
#Generate random numbers between 0 and the last index.
random_choice = random.randint(0, num_items - 1)
#Pick out random person from list of names using the random number.
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today!")
##############################################################################################
# Nested lists
even_numbers = [2,4,6,8,10,12]
odd_numbers = [1,3,5,7,9,11]
numbers = [even_numbers, odd_numbers]
print(numbers)
##############################################################################################
# Treasure finder
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
position = list(position.strip()) 
if position[0] == "A":
  Column = 0
elif position[0] == "B":
  Column = 1
else: 
  Column = 2
Row = int(position[1]) - 1
map[int(Row)][int(Column)] = "X"
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")