import constants
import sys

sys.setrecursionlimit(100000)

data = constants.day23
data = """\
#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""

data_lines = data.split("\n")

arrow_to_dir = {
    "<": (-1,0),
    ">": (1,0),
    "^": (0,-1),
    "v": (0,1),
    ".": (0,0)
}

# (pos): [ (o_pos, dist_to) ]
graph: dict[tuple[int,int], list[tuple[tuple[int,int],int]]] = {}
end = (len(data_lines[0])-2, len(data_lines)-1)

criticals = []
def precompute_criticals():
    for x in range(len(data_lines[0])):
        for y in range(len(data_lines)):
            adjacencies = 0
            if x > 0 and x < len(data_lines[0])-1 and y > 0 and y < len(data_lines)-1:
                for adj in ((1,0), (-1,0), (0,1), (0,-1)):
                    if get_value_at(vadd(adj, (x,y))) != "#":
                        adjacencies += 1

            if adjacencies > 2:
                criticals.append((x,y))
    
    criticals.append( end )

def get_value_at(pos):
    return data_lines[pos[1]][pos[0]]

def neg(dir):
    return (-dir[0], -dir[1])

def vadd(v1, v2):
    return (v1[0]+v2[0],v1[1]+v2[1])

states = set()
def tokenize_graph_ray(pos, dir, og_pos, prev_dist=0, p2=False):

    def is_transverseable(lpos, ldir, p2 = False):
        if p2:
            return get_value_at(lpos) != "#"
        else:
            return get_value_at(lpos) == "." or (get_value_at(lpos) != "#" and arrow_to_dir[get_value_at(lpos)] == ldir) 
    if not is_transverseable(vadd(pos, dir), dir, p2): return 
    if (pos, dir) in states: return 

    new_pos = pos
    states.add((pos, dir))

    while is_transverseable(vadd(new_pos, dir), dir, p2):
        prev_dist += 1
        new_pos = vadd(new_pos, dir)
        if new_pos in criticals:
            if not og_pos in graph:
                graph[og_pos] = []
            graph[og_pos].append((new_pos, prev_dist))
            prev_dist = 0
            og_pos = new_pos
            break
    
    if new_pos == end:
        return

    for potential_dir in dirs:
        if potential_dir == neg(dir): continue
        tokenize_graph_ray(new_pos,potential_dir,og_pos,prev_dist,p2)



prev_visited = []
dirs = [(1,0),(0,1),(-1,0),(0,-1)]
def calculate_longest_length(pos):
    if pos == end:
        return 0

    p_len = 0

    if pos in prev_visited: return -999
    prev_visited.append(pos)
    for potential_to, t_l in graph[pos]:
        c_prev_visited = prev_visited.copy()
        p_len = max(p_len, t_l+calculate_longest_length(potential_to))

        prev_visited.clear()
        for item in c_prev_visited:
            prev_visited.append(item)
    
    return p_len

def main():
    precompute_criticals()
    tokenize_graph_ray((1,0),(0,1),(1,0),0,True)
    print(graph)
    print(calculate_longest_length((1,0)))
    return
    prev_visited.remove((1,1))
    print(calculate_longest_length((1,0),(0,1),True))
    

main()