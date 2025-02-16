def square_generator(N):
    for i in range(1, N + 1):
        yield i ** 2


N = 10
for square in square_generator(N):
    print(square)



def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Enter a number for even numbers: "))
print(",".join(str(num) for num in even_numbers(n)))


def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("\nEnter a number for numbers divisible by 3 and 4: "))
print(list(divisible_by_3_and_4(n)))


def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("\nEnter the start of the range for squares: "))
b = int(input("Enter the end of the range for squares: "))

for square in squares(a, b):
    print(square, end=" ")


def countdown(n):
    for i in range(n, -1, -1):
        yield i

n = int(input("\n\nEnter a number for countdown: "))
for num in countdown(n):
    print(num, end=" ")
