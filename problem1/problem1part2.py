# Specify the path to your text file
file_path = 'problem2.txt'

# Open the file in read mode
digits = set([str(i) for i in range(10)])

names_to_digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0
}

total = 0
with open(file_path, 'r') as file:
    # Read each line and process it
    
    for line_number, line in enumerate(file, start=1):
        # find the earliest start
        line = line.strip()

        # earliest start for numeric digit
        numeric_start = 0
        end = len(line) - 1 
        numeric_found = False 
        while numeric_start < len(line):
            if line[numeric_start] in digits:
                numeric_found = True 
                break 
            numeric_start += 1

        # earliest start for 3 chars long
        three_chars_start = 0 
        three_found = False 
        while three_chars_start < len(line) - 3:
            if line[three_chars_start:three_chars_start+3] in names_to_digits:
                three_found = True 
                break
            three_chars_start += 1
        

        # earliest start for 4 chars long
        four_chars_start = 0 
        four_found = False 
        while four_chars_start < len(line) - 4:
            if line[four_chars_start:four_chars_start+4] in names_to_digits:
                four_found = True 
                break
            four_chars_start += 1

        # earliest start for 5 chars long
        five_chars_start = 0 
        five_found = False 
        while five_chars_start < len(line) - 5:
            if line[five_chars_start:five_chars_start+5] in names_to_digits:
                five_found = True 
                break
            five_chars_start += 1

        founds = {
            0: numeric_start,
            1: three_chars_start,
            2: four_chars_start,
            3: five_chars_start
        }
        
        min_start = len(line) + 1
        min_start_plus_length = 0
        founds_idx = -1
        for idx, val in enumerate([numeric_found, three_found, four_found, five_found]):
            if val:
                if founds[idx] < min_start:
                    min_start = founds[idx]
                    if idx == 0:
                        min_start_plus_length = 1
                    if idx == 1:
                        min_start_plus_length = 3
                    if idx == 2:
                        min_start_plus_length = 4
                    if idx == 3:
                        min_start_plus_length = 5
                # find the minimum start idx 

        # find the earliest end
        # earliest start for numeric digit
        numeric_end = len(line)-1
        numeric_found = False 
        while numeric_end > -1:
            if line[numeric_end] in digits:
                numeric_found = True 
                break 
            numeric_end -= 1

        # earliest start for 3 chars long
        three_chars_end = len(line)-3
        three_found = False
        while three_chars_end > -1:
            if line[three_chars_end:three_chars_end+3] in names_to_digits:
                three_found = True 
                break
            three_chars_end -= 1
        

        # earliest start for 4 chars long
        four_chars_end = len(line)-4
        four_found = False 
        while four_chars_end >  -1:
            if line[four_chars_end:four_chars_end+4] in names_to_digits:
                four_found = True 
                break
            four_chars_end -= 1

        # earliest start for 5 chars long
        five_chars_end = len(line)-5
        five_found = False 
        while five_chars_end > -1:
            if line[five_chars_end:five_chars_end+5] in names_to_digits:
                five_found = True 
                break
            five_chars_end -= 1

        founds = {
            0: numeric_end,
            1: three_chars_end,
            2: four_chars_end,
            3: five_chars_end
        }
        
        min_end = -1
        min_end_plus_length = 0
        founds_idx = -1
        for idx, val in enumerate([numeric_found, three_found, four_found, five_found]):
            if val:
                if founds[idx] > min_end:
                    min_end = founds[idx]
                    if idx == 0:
                        min_end_plus_length = 1
                    if idx == 1:
                        min_end_plus_length = 3
                    if idx == 2:
                        min_end_plus_length = 4
                    if idx == 3:
                        min_end_plus_length = 5
        # print(line, line[min_start:min_start+min_start_plus_length], line[min_end:min_end+min_end_plus_length])
        
        first_digit = line[min_start:min_start+min_start_plus_length]

        second_digit = line[min_end:min_end+min_end_plus_length]

        if first_digit in names_to_digits:
            first_digit = names_to_digits[first_digit]

        if second_digit in names_to_digits:
            second_digit = names_to_digits[second_digit]

        total += int(str(first_digit) + str(second_digit))
        
        print('--------')
        

print(total)
# Note: 'line.strip()' removes leading and trailing whitespaces from the line
