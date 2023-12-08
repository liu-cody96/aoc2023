steps = "LRRRLRRRLRRLRRLRLRRLRRLRRRLRRLRRRLRRRLLRRRLRRRLRRRLRLRRLRRRLRLRRRLRRRLLRLRLRRLRRLLLRRLRRLRRRLLRRRLLRRRLRLRRRLRRRLLRRLRLLRLRRRLRRLRRLRLRLRLRLRLRRRLRLRRRLLRLRRLRRRLRRRLRLRRLRLLLRLRLRLRLRLRRRLLRRLRLRLLRRRLRRLRRRLRRLRRLRRRLLRRLRLRRLRRRLRRLRLRRLRLLRRLLRLRRRLRRLRLLRRRR"
length = len(steps)
# Specify the path to your text file
file_path = 'problem8.txt'

m = {}
# Open the file in read mode
total = 0
with open(file_path, 'r') as file:
    curr = 'AAA'
    ['DVA', 'JQA', 'PTA', 'CRA', 'AAA', 'BGA']
    for line_number, line in enumerate(file, start=1):
        # Do something with each line
        # For example, print the line number and content
        line = line.strip().split(' = ')
        key = line[0]
        nodes = line[1][1:-1].split(', ')
        m[key] = nodes
    
    step = 0
    while curr != 'ZZZ':
        if steps[step] == 'L':
            curr = m[curr][0]
        else:
            curr = m[curr][1]
        total += 1
        step = (step + 1) % length
        # print(curr)
        print(total)

    print(total)

    
    






