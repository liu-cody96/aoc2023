# Specify the path to your text file
file_path = 'problem9.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
    total = 0
    # Read each line and process it
    for line_number, line in enumerate(file, start=1):
        # Do something with each line
        # For example, print the line number and content
        lst = line.strip().split(' ')
        
        num_zeroes = 0
        lsts = [lst]
        while num_zeroes != len(lst):
            new_lst = []
            num_zeroes = 0
            for i in range(1, len(lst)):
                diff = int(lst[i]) - int(lst[i-1])
                if diff == 0:
                    num_zeroes += 1
                new_lst.append(diff)
            lst = new_lst
            lsts.append(lst)
        
        curr_lst = len(lsts)-1
        while curr_lst > -1:
            last_num = lsts[curr_lst][-1]
            if curr_lst > 0:
                curr_diff = int(last_num) + int(lsts[curr_lst-1][-1])
                lsts[curr_lst-1].append(curr_diff)
                if curr_lst-1 == 0:
                    total += curr_diff
            curr_lst -= 1

    print(total)

# Note: 'line.strip()' removes leading and trailing whitespaces from the line
