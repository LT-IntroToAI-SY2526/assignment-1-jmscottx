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
# Add your tests here

print("\nTesting Problem 2:")
# Add your tests here

print("\nTesting Problem 3:")
# Add your tests here

print("\nTesting Problem 4:")
# Add your tests here

print("\nTesting Problem 5:")
# Add your tests here

"""
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is even.")
else:
    print(num, "is odd.")

    ✅ Problem 3: Countdown Timer

Topics: while loop, Variables

📝 Instructions:

Write a program that counts down from a number to 0.

num = int(input("Enter a number: "))
while num >= 0:
    print(num)
    num -= 1

   ✅ Problem 4: Sum of Numbers

Topics: for loop, Functions

📝 Instructions:

Write a function that takes a number n and returns the sum of numbers from 1 to n.

def sum_up_to(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sum_up_to(5))

✅ Problem 5: FizzBuzz

Topics: Loops, Conditionals

📝 Instructions:

Print numbers from 1 to 20.

If a number is divisible by 3, print "Fizz".

If divisible by 5, print "Buzz".

If divisible by both, print "FizzBuzz".

Otherwise, print the number.

for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

    Problem 6: Find Maximum in a List

Topics: Lists, Loops, Functions

📝 Instructions:

Write a function that returns the largest number in a list without using max().

def find_max(lst):
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

print(find_max([3, 8, 2, 9, 5]))

Problem 7: Count Vowels in a String

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

print("Testing Problem 2:")
assert is_even(4) == True
assert is_even(7) == False
assert is_even(0) == True
assert is_even(-2) == True
print("Passed all tests for Problem 2.\n")

def countdown(n):
    while n >= 0:
        print(n)
        n -= 1

print("Testing Problem 3:")
countdown(3)
# Expected output:
# 3
# 2
# 1
# 0
print("Visually check output for countdown.\n")

def sum_up_to(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print("Testing Problem 4:")
assert sum_up_to(5) == 15
assert sum_up_to(1) == 1
assert sum_up_to(10) == 55
assert sum_up_to(0) == 0
print("Passed all tests for Problem 4.\n")
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

print("Testing Problem 5:")
expected = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz",
            11, "Fizz", 13, 14, "FizzBuzz"]
assert fizzbuzz(15) == expected
print("Passed all tests for Problem 5.\n")

def find_max(lst):
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

print("Testing Problem 6:")
assert find_max([1, 2, 3, 4, 5]) == 5
assert find_max([5, 4, 3, 2, 1]) == 5
assert find_max([-5, -3, -10]) == -3
assert find_max([100]) == 100
print("Passed all tests for Problem 6.\n")

def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text:
        if char.lower() in vowels:
            count += 1
    return count

print("Testing Problem 7:")
assert count_vowels("Hello World") == 3
assert count_vowels("PYTHON") == 1
assert count_vowels("abcdefghijklmnopqrstuvwxyz") == 5
assert count_vowels("") == 0
assert count_vowels("AEIOUaeiou") == 10
print("Passed all tests for Problem 7.\n")

"""