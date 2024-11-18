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

