steps = "LRRRLRRRLRRLRRLRLRRLRRLRRRLRRLRRRLRRRLLRRRLRRRLRRRLRLRRLRRRLRLRRRLRRRLLRLRLRRLRRLLLRRLRRLRRRLLRRRLLRRRLRLRRRLRRRLLRRLRLLRLRRRLRRLRRLRLRLRLRLRLRRRLRLRRRLLRLRRLRRRLRRRLRLRRLRLLLRLRLRLRLRLRRRLLRRLRLRLLRRRLRRLRRRLRRLRRLRRRLLRRLRLRRLRRRLRRLRLRRLRLLRRLLRLRRRLRRLRLLRRRR"
length = len(steps)
# Specify the path to your text file
file_path = 'problem8.txt'

from collections import deque

m = {}
# Open the file in read mode
total = 0

num_z_nodes = 0 

with open(file_path, 'r') as file:
    curr = deque()
    for line_number, line in enumerate(file, start=1):
        # Do something with each line
        # For example, print the line number and content
        line = line.strip().split(' = ')
        key = line[0]
        nodes = line[1][1:-1].split(', ')
        m[key] = nodes
        if key[-1] == 'A':
            curr.append(key)
    
    step = 0
    
    while num_z_nodes != 6:
        curr_length = 6
        if steps[step] == 'L':
            for _ in range(curr_length):
                top = curr.popleft()
                if top[-1] == 'Z':
                    num_z_nodes -= 1
                new = m[top][0]
                if new[-1] == 'Z':
                    num_z_nodes += 1
                curr.append(new)
        else:
            for _ in range(curr_length):
                top = curr.popleft()
                if top[-1] == 'Z':
                    num_z_nodes -= 1
                new = m[top][1]
                if new[-1] == 'Z':
                    num_z_nodes += 1
                curr.append(new)
        total += 1
        step = (step + 1) % length
        if num_z_nodes > 1:
            print(curr, num_z_nodes)
            print(total)

    print(total)

    
    


