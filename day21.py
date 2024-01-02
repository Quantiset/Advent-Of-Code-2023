import constants

data = constants.day21
data_lines = data.split("\n")

adjacencies = [(0,1),(1,0),(0,-1),(-1,0)]
blockers = []
start_pos: tuple

def add(v1, v2):
    return (v1[0]+v2[0],v1[1]+v2[1])

def main():
    for y, line in enumerate(data_lines):
        for x, char in enumerate(line):
            if data_lines[y][x] == "#":
                blockers.append((x,y))
            elif data_lines[y][x] == "S":
                start_pos = (x,y)
    
    iters = 64
    flood = [start_pos]
    edge = flood
    for i in range(iters):
        v = edge.copy()
        edge = []
        for pos in v:
            for adj in adjacencies:
                if not add(pos,adj) in blockers and not add(pos, adj) in flood:
                    flood.append(add(pos, adj))
                    edge.append(add(pos, adj))
    
    summed = 0
    for new_pos in flood:
        if (new_pos[0]+new_pos[1]) % 2 == 0:
            summed += 1
    
    print(summed)
    


main()