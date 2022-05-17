# Exercise 1:
# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
pay = hours * rate
pay2 = hours * (1.5*rate)
if hours > 40:
    print(pay2)
else:
    print(pay)

# Exercise 2:
# Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message
# and exiting the program. The following shows two executions of the program:
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
try:
    pay = float(hours) * float(rate)
    print(pay)
except:
    print("Error, please enter a numeric input")


# Exercise 3:
# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message.
# If the score is between 0.0 and 1.0, print a grade using the following table:
input = input('Enter Score: ')

try:
    score = float(input)
    if score < 0.0 or score > 1.0:
        print("Bad Score")
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    elif score < 0.6:
        print ("F")
    else:
        print("Bad score")
except:
    print("Bad Score")