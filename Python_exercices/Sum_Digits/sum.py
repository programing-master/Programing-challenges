# Generate an algorithm that calculates the sum of the digits of a given number.

def sum_digit(number):
    if number == 0:
        return 0
    return number % 10 + sum_digit(number // 10)

print(sum_digit(123))
print()
print(sum_digit(223))