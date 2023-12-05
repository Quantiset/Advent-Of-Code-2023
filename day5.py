import constants

data = constants.day5

data_lines = data.split("\n")
to_maps = ["soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
maps = {a: [] for a in to_maps}
cached_maps = {}

def map_value(map_list: list, from_value: int) -> int:
    for map_arr in map_list:
        if from_value >= map_arr[1] and from_value < map_arr[1] + map_arr[2]:
            return from_value - map_arr[1] + map_arr[0]
    return from_value

def full_map(inp: int):
    return map_value( maps["location"], map_value( maps["humidity"], map_value( maps["temperature"], map_value( maps["light"], map_value( maps["water"], map_value( maps["fertilizer"], map_value( maps["soil"] , inp )))))))

def find_min_map(seeds):
    min_val = 9999999999999
    for seed in seeds:
        seed = int(seed)
        min_val = min(min_val, full_map(seed))
    return min_val

def main():

    curr_map_idx = 0
    temp_maps_for_this_map = []
    critical_points = []
    for line in data_lines[2:]:
        if line.endswith("map:"):
            continue

        if line == "":
            if temp_maps_for_this_map == []: continue
            maps[to_maps[curr_map_idx]] = temp_maps_for_this_map
            curr_map_idx += 1
            temp_maps_for_this_map = []
        
        else:
            this_map = list(map(int, line.split(" ")))
            critical_points.append( int(this_map[1]) )
            critical_points.append( int(this_map[1] + this_map[2]) )
            temp_maps_for_this_map.append( this_map )
    
    critical_points = list(set(critical_points))
    
    # part 1: print(find_min_map(data_lines[0][7:].split(" ")))

    min_seed = 99999999999
    seeds = data_lines[0][7:].split(" ")
    for i in range( int(len(seeds) / 2) ):
        init_seed = int(seeds[2*i])
        seed_length = int(seeds[2*i+1])
        
        min_val = find_min_map(range(init_seed, init_seed+seed_length+1))
        min_seed = min(min_seed, min_val)
        print(min_val)

    print(min_seed)
        

#932524280, 505472937

main()