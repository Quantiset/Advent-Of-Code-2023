import constants
import math

data = constants.day11
data_lines = data.split("\n")

def v_sub(a, b):
    return [a[0]-b[0],a[1]-b[1]]

def main():
    
    galaxies = []

    y_add = 0
    for line_idx, line in enumerate(data_lines):
        is_galaxy_on_line = False
        x_add = 0
        for char_idx, char in enumerate(line):

            is_x_empty = True
            for y_char_idx in range(len(data_lines)):
                if data_lines[y_char_idx][char_idx] == "#":
                    is_x_empty = False
                    break
            if is_x_empty:
                x_add += 1000000-1

            if char == "#":
                xy = [char_idx+x_add, line_idx+y_add]
                galaxies.append(xy)
                is_galaxy_on_line = True
        
        if not is_galaxy_on_line:
            y_add += 1000000-1
    
    sum_paths = 0
    for galaxy_pos in galaxies:
        for other_galaxy_pos in galaxies:
            if galaxy_pos == other_galaxy_pos: continue
            vel = v_sub(other_galaxy_pos, galaxy_pos)

            sum_paths += abs(vel[0])+abs(vel[1])
    
    print(sum_paths//2)



    

main()