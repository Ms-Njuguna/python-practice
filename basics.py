# 1. Even or Odd Checker
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# 2. Sum of List
def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# 3. CLI Greeter
name = input("What's your name? ")
age = input("How old are you? ")
print(f"Hello {name}, you are {age} years old!")
