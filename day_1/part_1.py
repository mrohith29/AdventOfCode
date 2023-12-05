def calculate_calibration_values(data):
    total = 0
    for line in data:
        value = "".join([char for char in line if char.isdigit()])
        fin = value[0] + value[-1]
        total += int(fin)
    return total

data = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet"
]


temp_contents = []

with open("input_part_1.txt", "r") as f:
    temp_contents = f.readlines()
    
    contents = [line.strip('\n') for line in temp_contents]


result = calculate_calibration_values(contents)
print("Total Calibration:", result)
