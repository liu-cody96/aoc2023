# Specify the path to your text file
file_path = 'problem1input.txt'

# Open the file in read mode
digits = set([str(i) for i in range(10)])

print(digits)
total = 0
with open(file_path, 'r') as file:
    # Read each line and process it
    for line_number, line in enumerate(file, start=1):
        # Do something with each line
        # For example, print the line number and content
        line = line.strip()
        start = 0
        end = len(line) - 1 
        while start < len(line):
            if line[start] in digits:
                break 
            start += 1

        while end > -1:
            if line[end] in digits:
                break
            end -= 1
        
        total += int(line[start] + line[end])

print(total)
# Note: 'line.strip()' removes leading and trailing whitespaces from the line
