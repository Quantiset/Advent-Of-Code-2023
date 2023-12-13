import constants

data = constants.day13

data_lines = data.split("\n")

smudges = []

def check_horizontality(lines: list, line_idx: int):
    for line_idx_above_comparison in range(line_idx):
        if len(lines) > 2*line_idx-line_idx_above_comparison-1:
            if lines[line_idx_above_comparison] != lines[2*line_idx-line_idx_above_comparison-1]:
                return False
    return True

def find_horizontal(map: str, ignore=0):
    data_lines = map.split("\n")
    for line_idx in range(len(data_lines)):
        if check_horizontality(data_lines, line_idx) and line_idx != 0 and line_idx != ignore:
            return line_idx
    return 0

def check_verticality(lines: list, char_idx: int):
    def get_char_idx_column(char_idx):
        ret = []
        for line in lines:
            ret.append(line[char_idx])
        return ret

    for char_idx_before_comparison in range(char_idx):
        if len(lines[0]) > 2*char_idx-char_idx_before_comparison-1:
            if get_char_idx_column(char_idx_before_comparison) != get_char_idx_column(2*char_idx-char_idx_before_comparison-1):
                return False
    return True

def find_vertical(map: str, ignore = 0):
    data_lines = map.split("\n")
    for char_idx in range(len(data_lines[0])):
        if check_verticality(data_lines, char_idx) and char_idx != 0 and char_idx != ignore:
            return char_idx
    return 0

def find_value_of_map(map: str, ignore_h=0, ignore_v=0):
    return 100*find_horizontal(map,ignore_h)+find_vertical(map,ignore_v)

def main():
    summed = 0
    summed2 = 0
    for map in data.split("\n\n"):
        summed += find_value_of_map(map)
    for map in data.split("\n\n"):
        for line_idx, line in enumerate(map.split("\n")):
            is_changed = False
            for char_idx, char in enumerate(line):
                updated_map = map.split("\n")
                updated_map[line_idx] = updated_map[line_idx][:char_idx] + {".":"#","#":"."}[char] + updated_map[line_idx][char_idx + 1:]
                updated_map = "\n".join(updated_map)

                old_horiz = find_horizontal(map)
                old_vert = find_vertical(map)

                new_val = find_value_of_map(updated_map, old_horiz, old_vert)

                #print(updated_map, "\n", old_vert, check_verticality(updated_map.splitlines(), old_vert), new_val, "\n")

                #if ((old_horiz != 0 and not check_horizontality(updated_map.splitlines(), old_horiz)) or \
                #    (old_vert != 0 and not check_verticality(updated_map.splitlines(), old_vert))) and new_val>0:
                if new_val > 0:
                    summed2 += new_val
                    is_changed = True
                    break
            if is_changed:
                break

    print(summed, summed2)

main()