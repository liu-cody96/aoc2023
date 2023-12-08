steps = "LRRRLRRRLRRLRRLRLRRLRRLRRRLRRLRRRLRRRLLRRRLRRRLRRRLRLRRLRRRLRLRRRLRRRLLRLRLRRLRRLLLRRLRRLRRRLLRRRLLRRRLRLRRRLRRRLLRRLRLLRLRRRLRRLRRLRLRLRLRLRLRRRLRLRRRLLRLRRLRRRLRRRLRLRRLRLLLRLRLRLRLRLRRRLLRRLRLRLLRRRLRRLRRRLRRLRRLRRRLLRRLRLRRLRRRLRRLRLRRLRLLRRLLRLRRRLRRLRLLRRRR"
length = len(steps)
# Specify the path to your text file
file_path = 'problem8.txt'

m = {}
# Open the file in read mode


import math

def calculate_lcm(numbers):
    # Function to calculate the LCM of two numbers
    def lcm(x, y):
        return x * y // math.gcd(x, y)

    # Initialize the LCM with the first number
    result_lcm = numbers[0]

    # Iterate through the remaining numbers and calculate LCM
    for i in range(1, len(numbers)):
        result_lcm = lcm(result_lcm, numbers[i])

    return result_lcm
    

with open(file_path, 'r') as file:
    nums = []
    for start in ['DVA', 'JQA', 'PTA', 'CRA', 'AAA', 'BGA']:
        curr = start
        total = 0
        for line_number, line in enumerate(file, start=1):
            # Do something with each line
            # For example, print the line number and content
            line = line.strip().split(' = ')
            key = line[0]
            nodes = line[1][1:-1].split(', ')
            m[key] = nodes
        
        step = 0
        while curr[-1] != 'Z':
            if steps[step] == 'L':
                curr = m[curr][0]
            else:
                curr = m[curr][1]
            total += 1
            step = (step + 1) % length
            if curr[-1] == 'Z':
                print(curr, total)

        nums.append(total)
    print(nums)
    print(calculate_lcm(nums))
    






