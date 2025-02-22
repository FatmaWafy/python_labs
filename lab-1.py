#Q1#
a = [10, 20, 30, 20, 40, 50]
a.remove(20)  
print(a)  
#_________________________________________#
#Q2#
a = [10, 20, 30, 20, 40, 50]
Val = a.pop(1)
print("Updated list:", a)  
print("Removed value:", Val)  
#_________________________________________#
#Q3#
a = [10, 20, 30, 40, 50, 60, 70]
del a[1:4]
print("Updated list:", a)
#_________________________________________#
#Q4#
a = [10, 20, 30, 40, 50, 60, 70]
a.clear()
print("Updated list:", a)
#_________________________________________#
#Q5#
text = input("Enter a string: ")
count = text.count("ITI")
print("The substring 'ITI' appears", count, "times.")
#_________________________________________#
#Q6#
binary_number = input("Enter a binary number: ")
decimal_number = int(binary_number, 2)
print("The decimal equivalent is:", decimal_number)
#_________________________________________#
#Q7#
def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "Fizz Buzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
number = int(input("Enter a number: "))
print(fizz_buzz(number))
#_________________________________________#
#Q8#
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius
print(f"Area of the circle: {area:.2f}")
print(f"Circumference of the circle: {circumference:.2f}")
#_________________________________________#
#Q9#
while True:
    name = input("Enter your name: ").strip()
    if name and not name.isdigit():
        break
    print("Invalid name! Please enter a valid name.")
    
email = input("Enter your email: ")
print("\nUser Information:")
print(f"Name: {name}")
print(f"Email: {email}")
#_________________________________________#