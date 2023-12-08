file_path = 'problem2.txt'

import re

def parse_int_space_string(input_string):
    # Define the regex pattern
    pattern = re.compile(r'(\d+)\s(.+)')
    
    # Match the pattern in the input string
    match = pattern.match(input_string)
    
    # Check if a match is found
    if match:
        # Extract the integer, space, and string
        parsed_int = int(match.group(1))
        parsed_string = match.group(2)
        
        # Return the results
        return parsed_int, parsed_string
    else:
        # Return None if no match is found
        return None

# Open the file in read mode



with open(file_path, 'r') as file:
    total = 0
    # Read each line and process it
    for line_number, line in enumerate(file, start=1):
        # Do something with each line
        # For example, print the line number and content
        split_line = line.strip().split(':')
        line_list = split_line[1].split(';')
        game_id = int(split_line[0].split(' ')[1])
        can_win = True
        min_colors = {
            "blue": 0,
            "red": 0,
            "green": 0
        }
        for s in range(len(line_list)):
            line_list[s] = line_list[s].strip()
            
            split_colors = line_list[s].split(', ')
            
            for s in split_colors:
                count, color = parse_int_space_string(s)
                min_colors[color] = max(min_colors[color], count)
                
        total += min_colors["blue"] * min_colors["red"] * min_colors["green"]

    print(total)