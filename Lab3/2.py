import random
import math

# Task 1: Convert grams to ounces
def grams_to_ounces(grams):
    return 28.3495231 * grams

# Task 2: Convert Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)

# Task 3: Solve the chicken and rabbit puzzle
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (2 * chickens + 4 * rabbits) == numlegs:
            return chickens, rabbits
    return None

# Task 4: Filter prime numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

# Task 5: Generate all permutations of a string
from itertools import permutations
def string_permutations(s):
    return ["".join(p) for p in permutations(s)]

# Task 6: Reverse words in a sentence
def reverse_sentence(sentence):
    return " ".join(sentence.split()[::-1])

# Task 7: Check for consecutive 3s
def has_33(nums):
    return any(nums[i] == nums[i+1] == 3 for i in range(len(nums)-1))

# Task 8: Check for sequence 007 in a list
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

# Task 9: Compute volume of a sphere
def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

# Task 10: Get unique elements from a list
def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Task 11: Check if a word is a palindrome
def is_palindrome(s):
    return s == s[::-1]

# Task 12: Print a histogram
def histogram(lst):
    for num in lst:
        print("*" * num)

# Task 13: Guess the number game
def guess_the_number():
    name = input("Hello! What is your name?\n")
    number = random.randint(1, 20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    guesses = 0
    while True:
        guess = int(input("Take a guess.\n"))
        guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break
