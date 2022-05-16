# DAY 2

#Data type

String
Integer -- positive and negetive number
Float -- decimal
boolean - True, False

-- This below feathurs is called subscripting 
print("hello"[0]) -- It will return the first character from "hello"
print("hello"[1]) -- It will return the second character from "hello"
print("hello"[2]) -- It will return the third character from "hello"
print("hello"[3]) -- It will return the fourth character from "hello"
print("hello"[4]) -- It will return the fifth character from "hello"
print("hello"[5])-- It will return IndexError: string index out of range error

print(type(tot_char)) -- type function will return the data type of any variable 

# Methematice operation sequence
#	PEMDASLR
#	()
#	**
#	* /
#	+ - 

# BMI calculator
hight=input("Enter your hight in meter: ")
weight=input("Enter your weight in Kg: ")
new_weight=float(weight)
new_hight=float(hight)
bmi=(new_weight/(new_hight**2))
print(int(bmi))

# find the number of char in a string
tot_char = len(input("What is your name?\n"))
new_tot_char = str(tot_char)
print("My name has " + new_tot_char + " Characters.")


# Calculate how many days, week, month remaining in your life

age = input("What is your current age? ")
age=int(age)
age_remaining = 90-age
days_ramaining = age_remaining*365
week_remaining = age_remaining*52
months_remaining = age_remaining *12
message= f"You have {days_ramaining} days, {week_remaining} weeks, and {months_remaining} months left."
print(message)


# Project Tip calculator

print("welcome to the tip Calculator.")
total_bill=float(input("What is the total bill amount? "))
no_of_people=int(input("How many no of people will split the bill? "))
tip_percent=int(input("What percent of tip you want to give? 10, 12, or 15? "))
total_amount = total_bill*(1+(tip_percent/100))
tips_per_person = round(total_amount/no_of_people,2)
tips_per_person = "{:.2f}".format(tips_per_person)
print(f"Each person should pay: {tips_per_person}")