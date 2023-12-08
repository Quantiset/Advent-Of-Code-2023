import constants
import math

data = constants.day8
data_lines = data.split("\n")[2:]

step_to_int = {"R": 1, "L": 0}

def lcm(inp: list):
    a = inp[0]
    for i in inp:
        a = math.lcm(a, i)
    return a

def main():
    maps = {}
    steps_instructions = data.split("\n")[0]

    for line in data_lines:
        origin = line.split(" = ")[0]
        to_map = line.split(" = ")[1].removeprefix("(").removesuffix(")").split(", ")
        maps[origin] = to_map
    
    def p1():
        steps = 0
        curr = "AAA"
        while curr != "ZZZ":
            step_dir = steps_instructions[steps % len(steps_instructions)]
            curr = maps[curr][step_to_int[step_dir]]
            steps += 1

        print(steps)
    
    curr_list = [a for a in [z.split(" = ")[0] for z in data_lines] if a[2]=="A"]
    finished_currs = {}
    for curr in curr_list:
        steps = 0
        while not curr in finished_currs:
            step_dir = steps_instructions[steps % len(steps_instructions)]
            curr = maps[curr][step_to_int[step_dir]]
            steps += 1
            if curr[2] == "Z":
                finished_currs[curr] = steps
    
    print(lcm(list(finished_currs.values())))

main()