import math

def calculate_lcm(numbers):
    def lcm(x, y):
        return x * y // math.gcd(x, y)

    result_lcm = numbers[0]

    for i in range(1, len(numbers)):
        result_lcm = lcm(result_lcm, numbers[i])

    return result_lcm

numbers_to_calculate_lcm = [11309, 30508, 42869, 58912, 72851, 91524]
result = calculate_lcm(numbers_to_calculate_lcm)
print(result)