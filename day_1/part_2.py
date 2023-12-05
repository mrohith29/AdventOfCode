with open("input_part_2.txt", "r") as f:
    contents = f.readlines()
    contents = [line.strip('\n') for line in contents]
    print(contents)