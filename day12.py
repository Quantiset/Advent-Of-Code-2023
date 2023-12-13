import constants
from itertools import combinations

data = constants.day12
data = """??.???.### 1,1,3"""
data_lines = data.split("\n")

configurations_cache = {}

def count_permutations(geysers, configurations, depth, path: list):
    print(geysers, configurations, depth, path)
    
    if len(configurations) == 0:
        print("HIT")
        if "#" in geysers:
            return depth
        return 1

    summed = 0
    for char_idx, char in enumerate(geysers):
        if char == ".": continue

        

        geysers = geysers[char_idx:]

        number_in_a_row = configurations[0]

        if (char_idx+number_in_a_row > len(geysers)):
            break

        allow = True
        for i in range(1,number_in_a_row):
            if geysers[i] == "." or geysers[i] == "?":
                allow = False
                break

        if allow:
            path.append( geysers[:number_in_a_row] )
            summed += count_permutations(geysers[number_in_a_row:], configurations[1:], depth+1, path)

    return summed
        

def decimal_to_binary(num: int, q_indices):
    return num
    to_bin = bin(num).replace("0b", "").zfill(len(q_indices))
    return to_bin

def is_valid_geyser(geyser, configuration):
    test = list(filter(None, geyser.split(".")))
    if len(test) != len(configuration): return False
    for i,j in zip(test, configuration):
        if len(i) != j:
            return False
    return True

def generate_configurations(q_indices):
    ret = []
    for i in range(2**len(q_indices)):
        ret.append(decimal_to_binary(i, q_indices))
    return ret

def main():

    for line in data_lines:
        q_indices = []
        geysers = line.split(" ")[0]
        #geysers = ((geysers + "?") * 5).removesuffix("?")
        total_configurations = list(map(int, line.split(" ")[1].split(",")))
        #total_configurations = list(map(int,((line.split(" ")[1]+",") * 5).removesuffix(",").split(",")))

        print(geysers, total_configurations)
        print(count_permutations(geysers, total_configurations, 0, []))
        
        """
        for idx, char in enumerate(geysers):
            if char == "?":
                q_indices.append(idx)
        
        configurations = generate_configurations(q_indices)
        for configuration in configurations:
            temp_str = geysers
            for configuration_idx, configuration_bit in enumerate(configuration):
                configuration_bit = int(configuration_bit)
                temp_str = temp_str[:q_indices[configuration_idx]] + [".","#"][configuration_bit] + temp_str[q_indices[configuration_idx] + 1:]
            
            if is_valid_geyser(temp_str, total_configurations):
                summed += 1
        """
    


main()