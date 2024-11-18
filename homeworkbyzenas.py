##odd or even
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

## Pass or Fail
score = int(input("Enter your score:  "))
if score >= 50:
    print("Pass")
else:
    print("Fail")

## Age Verification
age = int(input("Enter your age:  "))
if age <= 18:
    print("Youre a minor")
else:
    print("Youre an adult")

##Temperature Check
temperature = float(input("Enter the current outdoor temperature: "))

if temperature>= 30:
    print("It's hot!")
elif 15 <= temperature < 30:
    print("It's warm.")
else:
    print("It's cold.")

##Grade Calculator
Grade = int(input("Enter your score (out of 100): "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F" )

## Number Comparison
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print("The first number is greater") 
elif num2 > num1:
    print("The second number is greater")
else:
    print("Both numbers are equal")

##Eligibility for a discount
howoldareyou = int(input("Enter your age: "))
if howoldareyou < 12 or age > 65:
    print("You're eligible for a discount")
else:
    print("No discount available")

## Even Number Checker
checker = int(input("Enter a number: "))

if checker  % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")

## Simple Calculator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

if operator == '+':
    result = num1 + num2

elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2 

##Voting Eligibility
age = int(input("Enter your age: "))
country = input("Enter your country: ")

if age >= 18 and country == "Ghana":
    print("You can vote")
else:
    print("You cannot vote")