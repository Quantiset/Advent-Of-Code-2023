import constants

data = constants.day6
data_lines = data.split("\n") 

def main():
    times = list(map(int, list(filter(None, data_lines[0][7:].split(" ")))))
    distances = list(map(int, list(filter(None, data_lines[1][10:].split(" ")))))
    
    margin = 1
    for idx, time in enumerate(times):
        ways = 0
        distance = distances[idx]
        for query_initial_buildup_time in range(1, time):
            speed = query_initial_buildup_time
            if (time - query_initial_buildup_time) > distance / speed:
                ways += 1
        margin *= ways
    
    time = int(str(times).removeprefix("[").removesuffix("]").replace(", ", ""))
    distance = int(str(distances).removeprefix("[").removesuffix("]").replace(", ", ""))

    lower_bound = 0
    upper_bound = 999999
    for query_initial_buildup_time in range(1, time):
        speed = query_initial_buildup_time
        if (time - query_initial_buildup_time) > distance / speed:
            lower_bound = query_initial_buildup_time
            break
    
    for query_initial_buildup_time in range(time+1, 1, -1):
        speed = query_initial_buildup_time
        if (time - query_initial_buildup_time) > distance / speed:
            upper_bound = query_initial_buildup_time
            break

    print(margin, upper_bound-lower_bound+1)


main()