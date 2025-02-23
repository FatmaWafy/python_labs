#Q1#
def calculator(operation, a, b):
    match operation:
        case "add":
            return a + b
        case "subtract":
            return a - b
        case "multiply":
            return a * b
        case "divide":
            return a / b if b != 0 else "Cannot divide by zero"
        case _:
            return "Invalid operation"
        
operation = "add"
a, b = 10, 5
result = calculator(operation, a, b)
print(result)
#_________________________________________#
#Q2#
def filter_odds(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return odd_numbers, len(odd_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers, count = filter_odds(numbers)

print(filtered_numbers, "Count =", count)  
#_________________________________________#
#Q3#
def is_valid_password(password):
    if len(password) < 8:
        return "Invalid Password: Too short"
    
    if not any(char.isupper() for char in password):
        return "Invalid Password: No uppercase letter"
    
    if not any(char.isdigit() for char in password):
        return "Invalid Password: No digit"
    
    return "Valid Password"

password = "Pass1234"
print(is_valid_password(password))
#_________________________________________#
#Q4#
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

merged_dict = {}
merged_dict.update(dic1)
merged_dict.update(dic2)
merged_dict.update(dic3)

print(merged_dict)
#_________________________________________#
#Q5#
def longest_alphabetical_substring(s):
    longest = current = s[0]
    
    for i in range(1, len(s)):
        if s[i] >= s[i - 1]:
            current += s[i]
        else:
            if len(current) > len(longest):
                longest = current
            current = s[i]
        
    if len(current) > len(longest):
        longest = current
        
    return longest

s = "Abdulrahman"
print(f"The longest substring in alphabetical order is: {longest_alphabetical_substring(s)}")
#_________________________________________#
#Q6#
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return "Valid Email"
    else:
        return "Invalid Email"

email = input("Enter your email: ")
print(is_valid_email(email))
#_________________________________________#
 