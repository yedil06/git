from functools import reduce
import time
import math

# 1.
def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

# 2
def count_upper_lower(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count

# 3
def is_palindrome(s):
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned_string == cleaned_string[::-1]

# 4. 
def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)  # Convert milliseconds to seconds
    result = math.sqrt(number)
    return result

# 5.
def all_true(t):
    return all(t)

# Main program
if __name__ == "__main__":
    # 1
    numbers = [1, 2, 3, 4, 5]
    product = multiply_list(numbers)
    print(f"Product of numbers in the list: {product}")

    # 2
    input_string = "Hello World!"
    upper, lower = count_upper_lower(input_string)
    print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")

    # 3
    palindrome_string = "A man, a plan, a canal, Panama"
    if is_palindrome(palindrome_string):
        print(f"'{palindrome_string}' is a palindrome.")
    else:
        print(f"'{palindrome_string}' is not a palindrome.")

    # 4
    number = 25100
    delay_ms = 2123
    sqrt_result = delayed_sqrt(number, delay_ms)
    print(f"Square root of {number} after {delay_ms} milliseconds is {sqrt_result}")

    # 5 
    tuple1 = (True, True, True)
    tuple2 = (True, False, True)
    print(f"All elements in {tuple1} are true: {all_true(tuple1)}")
    print(f"All elements in {tuple2} are true: {all_true(tuple2)}")