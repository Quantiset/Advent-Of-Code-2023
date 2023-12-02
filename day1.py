import constants

inputs = constants.day1

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def main():
    sum = 0
    for line in inputs.split("\n"):
        lnum = 0
        rnum = 0
        for i in range(len(line)):
            if lnum == 0 and is_num(line, i):
                lnum = get_num(line, i)
            
            if is_num(line, i):
                rnum = get_num(line, i)
        sum += 10*lnum+rnum
    
    print(sum)

def is_num(line: str, i: int):
    return line[i].isdigit() or bool(sum([line[i:].startswith(num) for num in numbers]))

def get_num(line: str, i: int):
    if line[i].isdigit():
        return int(line[i])
    k = 0
    for num in numbers:
        k += 1
        if line[i:].startswith(num):
            return k
    print("err")
        
main()