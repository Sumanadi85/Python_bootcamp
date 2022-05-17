# DAY -5 

# loops

# Avg height calculator

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_Student = n + 1
totol_height = 0
for height in student_heights:
    totol_height += int(height)

avg_height = round((totol_height/total_Student))
#print(student_heights)
print(avg_height)


# calculates the highest score

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

heighst_score = 0

for score in student_scores:
    if int(score) > heighst_score:
        heighst_score = int(score)

print(f"The highest score in the class is: {heighst_score}")

# calculates the sum of all the even numbers
total = 0
for n in range(1, 101):

    if n % 2 == 0:
        #print(n)
        total += n
print(total)

# FizzBuzz game

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

		
#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#print(random.sample(letters, nr_letters))
letter = ''
for l in random.sample(letters, nr_letters):
    letter = letter + l
#print(letter)

#print(random.sample(numbers, nr_numbers))
number = ''
for l in random.sample(numbers, nr_numbers):
    number = str(number) + str(l)
#print(number)

#print(random.sample(numbers, nr_numbers))
symbol = ''
for l in random.sample(symbols, nr_symbols):
    symbol = str(symbol) + str(l)
#print(symbol)

password = (letter + number + symbol)
print(password)
print(''.join(random.sample(password, len(password))))
	