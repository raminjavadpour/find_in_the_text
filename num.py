import re

def extract_mobile_numbers(input_file_path, output_file_path):
    # Read txt file
    with open(input_file_path, 'r') as file:
        content = file.read()

    # find mobile num started by +98
    mobile_numbers = re.findall(r'\+98\d{10}', content)

    # save to txt file
    with open(output_file_path, 'w') as output_file:
        for mobile_number in mobile_numbers:
            output_file.write(mobile_number + '\n')

#input file path and output file path
extract_mobile_numbers('C:/input.txt', 'C:/output.txt')
