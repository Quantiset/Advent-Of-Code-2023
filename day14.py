import constants

data = constants.day14

data_lines = data.split("\n")

def find_load(platform):
    for i in range(3):
        platform = rotate_clock(platform)
    lines = platform.split("\n")
    load = 0
    for line in lines:
        for char_idx, char in enumerate(line):
            if char == "O":
                load += (len(line) - char_idx) 
    return load

cache = {}

def tilt_left(platform):
    lines = platform.split("\n")
    new_plat = []
    for line in lines:
        t_line = tuple(line)
        if t_line in cache:
            new_plat.append(cache[t_line])
            continue
        new_string = list(line)
        last_lean_idx = 0
        for char_idx in range(len(line)):
            char = new_string[char_idx]
            if char == "O":
                if char_idx != last_lean_idx:
                    new_string[last_lean_idx] = "O"
                    new_string[char_idx] = "."
                    last_lean_idx += 1
                else:
                    last_lean_idx = char_idx + 1
            if char == "#":
                last_lean_idx = char_idx + 1
        
        new_string = "".join(new_string)
        cache[t_line] = new_string
        new_plat.append(new_string)

    return "\n".join(new_plat)

def rotate_clock(platform):
    platform = platform.split("\n")
    lines = ["".join(a) for a in list(zip(*platform[::-1]))]
    return ("\n".join(lines))

def main():

    platform = data
    load = 0
    prevalances = []

    cycles = -1
    while True:
        cycles += 1
        for i in range(3):
            platform = rotate_clock(platform)
        
        for j in range(4):
            platform = tilt_left(platform)
            if j != 3:
                platform = rotate_clock(platform)
        
        for i in range(2):
            platform = rotate_clock(platform)

        if platform in prevalances:
            start_cycle = prevalances.index(platform)
            print(start_cycle)
            print(find_load(prevalances[start_cycle + (1000000000-start_cycle) % (len(prevalances) - start_cycle) - 1 ]))
            break
        prevalances.append(platform)
        
    print(list(map(find_load, prevalances)))
    


main()