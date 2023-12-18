import constants
import heapq

data = constants.day17

data_lines = data.split("\n")
end = len(data_lines) * len(data_lines[0]) - 1

def get_adjacencies(pos):
    adj = []
    x = pos % len(data_lines[0])
    y = pos // len(data_lines[0])
    pos = y*len(data_lines[0])+x

    if x != len(data_lines[0])-1:
        adj.append([+1, int(data_lines[y][x+1]) ])
    if x != 0:
        adj.append([-1, int(data_lines[y][x-1]) ])
    if y != len(data_lines)-1:
        adj.append([+len(data_lines[0]), int(data_lines[y+1][x]) ])
    if y != 0:
        adj.append([-len(data_lines[0]), int(data_lines[y-1][x]) ])
    return adj

def find_cost(pos):
    x = pos % len(data_lines[0])
    y = pos // len(data_lines[0])
    return int(data_lines[y][x])

def check_p1(curr_dp, dp, in_a_row):
    if dp == -curr_dp:
        return -1
    if dp != curr_dp:
        return 1
    if dp == curr_dp:
        return in_a_row+1
    return -1

def check_p2(curr_dp, dp, in_a_row):
    if dp == curr_dp:
        return in_a_row + 1
    if dp == -curr_dp:
        return -1
    if in_a_row >= 4 or curr_dp == 0:
        return 1
    return -1

def search(function, max_length):
    lines = []
    for line in data.split("\n"):
        lines.append(list(map(int, list(line))))
    
    distances = {a:{} for a in range(end+1)}
    paths = {a:[] for a in range(end+1)}

    queue = [(0, 0, 0, 1)]

    while len(queue) != 0:
        current_distance, current_position, prev_dp, in_a_row = heapq.heappop(queue)

        for dp, weight in get_adjacencies(current_position):

            new_in_a_row = function(prev_dp, dp, in_a_row)
            if new_in_a_row == -1 or new_in_a_row == max_length:
                continue
            
            neighbor = dp + current_position
            distance = current_distance + weight

            if not (dp, new_in_a_row) in distances[neighbor]:
                distances[neighbor][dp, new_in_a_row] = 9999999
            
            if distance < distances[neighbor][dp, new_in_a_row]:
                paths[neighbor] = paths[current_position] + [current_position]
                distances[neighbor][dp, new_in_a_row] = distance
                heapq.heappush(queue, (distance, neighbor, dp, new_in_a_row))
    
    return distances

def main():
    print( min(search(check_p1, 4)[end].values()) , min(search(check_p2, 11)[end].values()) )
    

main()