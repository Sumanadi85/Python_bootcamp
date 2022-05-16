# DAY 3

# Condition 

# IF .. Else

print("Welcome to the roller coaster ride.")
height = int(input("Enter your height in cm: "))

if height >= 120:
    print("You are in!")
else:
    print("Sorry Bro you have to wait to grow up.")
	
#Odd & Even
number = int(input("Which number do you want to check? "))
if (number % 2) == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
	
# IF..elif 
print("Welcome to the roller coaster ride.")
height = int(input("Enter your height in cm: "))

if height >= 120:
  age = int(input("Enter your Age: "))

  if age < 12:
    print("Pay $5")
    print("And you are in!")
  elif age <=18:
    print ("Pay $7")
    print("And you are in!")
  else:
    print("Pay $12")
    print("And you are in!")
else:
    print("Sorry Bro you have to wait to grow up.")


# BMI 2.0

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi=int(round((weight/(height**2)),0))

if bmi < 18.5:
    text = "you are underweight."
elif bmi < 25:
    text = "you have a normal weight."
elif bmi < 30:
    text = "you are slightly overweight."
elif bmi <= 35:
    text = "you are obese."
elif bmi > 35:
    text = "you are clinically obese."

print(f"Your BMI is {bmi}, {text}")


# Finding a year is Leap year or not

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
         print ("Leap year.")
      else:
        print ("Not leap year.") 
    else: 
      print ("Leap year.")
else:
    print ("Not leap year.") 
	
# Roller Coaster 2.0

print("Welcome to the roller coaster ride.")
height = int(input("Enter your height in cm: "))

if height >= 120:
    print("And you are in!")
    age = int(input("Enter your Age: "))
    bill = 0
	
    if age < 12:
        bill = 5
        print(f"Your Ticket Price is ${bill}")
    elif age <= 18:
        bill = 7
        print(f"Your Ticket Price is ${bill}")
    else:
        bill = 12
        print(f"Your Ticket Price is ${bill}")

    want_photo = (input("Do you want to take photo? Y or N "))

    if want_photo == 'Y':
        bill += 3
        print(f"Your Final Ticket Price is ${bill}")

else:
    print("Sorry Bro you have to wait to grow up.")
	
	
# Pizza order bill


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size == 'S':
    price = 15
elif size == 'M':
    price = 20
elif size == 'L':
    price = 25
else:
    price == 0

if add_pepperoni == 'Y':
    if size == 'S':
        pep_price = 2
    elif size == 'M':
        pep_price = 3
    elif size == 'L':
        pep_price = 3
else:
    pep_price = 0

if extra_cheese == 'Y':
    cheese_price = 1
else:
    cheese_price = 0

final_bill = price + pep_price + cheese_price

print(f"Your final bill is: ${final_bill}.")


# Love Calculator

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combine_name = name1 + name2
lower_case=combine_name.lower()

#print(lower_case)

t=lower_case.count("t")
r=lower_case.count("r")
u=lower_case.count("u")
e=lower_case.count("e")

true_sum = t+r+u+e
#print(true_sum)


l=lower_case.count("l")
o=lower_case.count("o")
v=lower_case.count("v")
e=lower_case.count("e")

love_sum = l+o+v+e
#print(love_sum)


final_value = int(str(true_sum) + str(love_sum))

if final_value < 10 or final_value > 90:
    print(f"Your score is {final_value}, you go together like coke and mentos.")
elif final_value >= 40 and int(final_value) <= 50:
    print(f"Your score is {final_value}, you are al-right together.")
else:
    print(f"Your score is {final_value}.")


# Project Treasure Island

print("Welcome to the Treasure Island.")
left_right = input("Which way you want to go? Left or Right\n").lower()

if left_right == 'left':
  swim_wait = input("Do want to swim or wait? Swim or Wait\n").lower()
  if swim_wait == 'swim':
    door_color = input("Which colour door you want to open? Red, Blue or Yellow\n").lower()
    if door_color == 'red':
      print("Brunt by fire. Game Over!")
    elif door_color == 'blue':
      print("Eaten by Beast. Game over!")
    elif door_color == 'yellow':
      print("You Win.")
    else:
      print("Game over!")
  else: 
    print("Attach by Trout. Game over!")
else:
  print("You fall into a whole. Game over!")