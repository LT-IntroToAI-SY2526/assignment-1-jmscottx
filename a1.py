# Assignment 1: AI-Generated Python Problems
# Name: [James Scott]

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT: 
["I'm learning Python basics in a high school programming class. I have some experience with JavaScript. Can you create 5-7 practice problems that cover Variables and basic data types, Conditionals (if/elif/else) Loops (for and while), Functions, Basic list operations, Make them progressively more challenging. Make sure each problem has clear instructions and example inputs/outputs."]

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

PROBLEM 1: Celsius to Fahrenheit Converter
[Writes a program that converts a temperature from Celsius to Fahrenheit]
"""

def celsius_to_farenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

"""
PROBLEM 2: Even or Odd Checker
[Ask the user for a number and tell them whether it's even or odd.]
"""
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is even.")
else:
    print(num, "is odd.")

""""
PROBLEM 3: COUNTDOWN TIMER
[Write a program that counts down from a number to 0.]
"""
num = int(input("Enter a number: "))
while num >= 0:
    print(num)
    num -= 1

""""
PROBLEM 4: SUM OF NUMBERS
[Write a function that takes a number n and returns the sum of numbers from 1 to n.]
"""
def sum_up_to(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sum_up_to(5))

""""
PROBLEM 5: FIZZBUZZ
[Prints numbers from 1 to 20.]
"""
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result

"""
PROBLEM 6: FIND MAXIMUM IN A LIST
[Writes a function that returns the largest number in a list without using max().]
"""
def find_max(lst):
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

print(find_max([3, 8, 2, 9, 5]))

"""
PROBLEM 7: COUNT VOWELS IN A STRING
[Counts vowels in a strng of text]

"""
def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text:
        if char.lower() in vowels:
            count += 1
    return count

print(count_vowels("Hello World"))

def is_even(n):
    return n % 2 == 0

# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Testing Problem 1:")

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

assert celsius_to_fahrenheit(0) == 32, "0°C should be 32°F"
assert celsius_to_fahrenheit(100) == 212, "100°C should be 212°F"
assert celsius_to_fahrenheit(-40) == -40, "-40°C should be -40°F"
assert celsius_to_fahrenheit(37) == 98.6, "37°C should be 98.6°F"
assert round(celsius_to_fahrenheit(20), 1) == 68.0, "20°C should be 68°F"

print("All tests passed!")

print("\nTesting Problem 2:")
assert is_even(4) == True
assert is_even(7) == False
assert is_even(0) == True
assert is_even(-2) == True
print("Passed all tests for Problem 2.")

print("\nTesting Problem 3:")
def countdown(n):
    while n >= 0:
        print(n)
        n -= 1
countdown(3)
# Expected output:
# 3
# 2
# 1
# 0
print("Visually check output for countdown.\n")

print("\nTesting Problem 4:")
def sum_up_to(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

assert sum_up_to(5) == 15
assert sum_up_to(1) == 1
assert sum_up_to(10) == 55
assert sum_up_to(0) == 0
print("Passed all tests for Problem 4.\n")

print("\nTesting Problem 5:")

expected = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz",
            11, "Fizz", 13, 14, "FizzBuzz"]
assert fizzbuzz(15) == expected
print("Passed all tests for Problem 5.\n")

def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result