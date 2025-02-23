import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print (x)



import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)



import re
txt = "Ronaldo is the best striker"
x = re.findall("Messi" , txt)
print (x)


import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())



import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)



import re 

txt = "Ronaldo is the best striker"
x = re.split("\s" , txt)
print (x)



import re

def match_a_followed_by_zero_or_more_bs(text):
    pattern = r'ab*'
    if re.fullmatch(pattern, text):
        return True
    return False

# Example 
print(match_a_followed_by_zero_or_more_bs("ab"))  # True
print(match_a_followed_by_zero_or_more_bs("a"))   # True
print(match_a_followed_by_zero_or_more_bs("ac"))  # False




import re

# 1
def match_a_followed_by_zero_or_more_bs(text):
    pattern = r'ab*'
    return bool(re.fullmatch(pattern, text))

# 2
def match_a_followed_by_two_to_three_bs(text):
    pattern = r'ab{2,3}'
    return bool(re.fullmatch(pattern, text))

# 3
def find_lowercase_sequences_with_underscore(text):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, text)

# 4
def find_uppercase_followed_by_lowercase(text):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, text)

# 5
def match_a_followed_by_anything_ending_in_b(text):
    pattern = r'a.*b$'
    return bool(re.fullmatch(pattern, text))

# 6
def replace_spaces_commas_dots_with_colon(text):
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', text)

# 7
def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

# 8
def split_at_uppercase(text):
    return re.findall(r'[A-Z][^A-Z]*', text)

# 9
def insert_spaces_between_capitals(text):
    return re.sub(r'(?<!^)([A-Z])', r' \1', text)

# 10
def camel_to_snake(camel_str):
    return re.sub(r'(?<!^)([A-Z])', r'_\1', camel_str).lower()

#Examples
if __name__ == "__main__":
    # 1
    print("1. Match 'a' followed by zero or more 'b's:")
    print(match_a_followed_by_zero_or_more_bs("ab"))  
    print(match_a_followed_by_zero_or_more_bs("a"))   
    print(match_a_followed_by_zero_or_more_bs("ac"))  
    print()

    # 2
    print("2. Match 'a' followed by two to three 'b's:")
    print(match_a_followed_by_two_to_three_bs("abb"))    
    print(match_a_followed_by_two_to_three_bs("abbb"))   
    print(match_a_followed_by_two_to_three_bs("ab"))     
    print()

    # 3
    print("3. Find sequences of lowercase letters joined with an underscore:")
    print(find_lowercase_sequences_with_underscore("hello_world and foo_bar"))  # ['hello_world', 'foo_bar']
    print()

    # 4
    print("4. Find sequences of one uppercase letter followed by lowercase letters:")
    print(find_uppercase_followed_by_lowercase("Hello World and Python"))  # ['Hello', 'World', 'Python']
    print()

    # 5
    print("5. Match 'a' followed by anything, ending in 'b':")
    print(match_a_followed_by_anything_ending_in_b("aanythingb"))  # True
    print(match_a_followed_by_anything_ending_in_b("ab"))          # True
    print(match_a_followed_by_anything_ending_in_b("ac"))          # False
    print()

    # 6
    print("6. Replace spaces, commas, or dots with a colon:")
    print(replace_spaces_commas_dots_with_colon("Hello, world. This is a test."))  # "Hello::world::This:is:a:test:"
    print()

    # 7
    print("7. Convert snake case to camel case:")
    print(snake_to_camel("hello_world"))  # "helloWorld"
    print()

    # 8
    print("8. Split a string at uppercase letters:")
    print(split_at_uppercase("HelloWorldThisIsPython"))  # ['Hello', 'World', 'This', 'Is', 'Python']
    print()

    # 9
    print("9. Insert spaces between words starting with capital letters:")
    print(insert_spaces_between_capitals("HelloWorldThisIsPython"))  # "Hello World This Is Python"
    print()

    # 10
    print("10. Convert camel case to snake case:")
    print(camel_to_snake("helloWorldThisIsPython"))  # "hello_world_this_is_python"

