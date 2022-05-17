# Exercise 2:
# Write a program that uses input to prompt a user for their name and then welcomes them.
name = input('Enter your name: ')
print("Hello " + name)


# Exercise 3:
# Write a program to prompt the user for hours and rate per hour to compute gross pay.
hours = int(input("Enter hours: "))
rate = int(input("Enter rate: "))
gross_pay = hours * rate
print('The gross pay is ' + str(gross_pay))

# Exercise 4:
# Assume that we execute the following assignment statements:
width = 17
height = 12.0
# For each of the following expressions, write the value of the expression and the type (of the value of the expression).
exp_i = width//2
print(exp_i)
print(type(exp_i))
exp_ii = width/2.0
print(exp_ii)
print(type(exp_ii))
exp_iii = height/3
print(exp_iii)
print(type(exp_iii))
exp_iv = 1 + 2 * 5
print(exp_iv)
print(type(exp_iv))


# Exercise 5:
# Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.
temp_in_celsius = int(input("Enter temperature in degree celsius: "))
temp_in_fahrenheit = (temp_in_celsius*1.8) + 32
print('The temperature in Fahrenheit is ' + str(temp_in_fahrenheit) + "degree Fahrenheit")