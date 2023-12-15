def solution(contents):
    total = 0
    for word in contents:
        currentValue = 0
        for letter in word:
            currentValue += ord(letter)
            currentValue *= 17
            currentValue %= 256
        total += currentValue

    return total

# temp_content = []
def main():
    with open("testcase.txt", "r") as f:
        temp_content = f.readline()

        contents = temp_content.split(',')    
    # contents = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7".split(',')
    # print(contents)
    print(solution(contents))

if __name__ == "__main__":
    main()