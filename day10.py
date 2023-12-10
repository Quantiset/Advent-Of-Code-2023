import constants
import sys
import math

data = constants.day10
data_lines = data.split("\n")

pipe_to_connections = {
    "-": [[1,0],[-1,0]],
    "|": [[0,-1],[0,1]],
    "L": [[0,-1],[1,0]],
    "J": [[0,-1],[-1,0]],
    "7": [[-1,0],[0,1]],
    "F": [[1,0],[0,1]],
}

class Pipe:
    char: str = ""
    dist: int = 0

    def __init__(self, _pos, _char, _dist, _to) -> None:
        self.pos = _pos
        self.char = _char
        self.dist = _dist
        self.to = _to

def get_char(x, y):
    return data_lines[y][x]

def v_add(v1, v2):
    return [v1[0]+v2[0],v1[1]+v2[1]]

def v_sub(v1, v2):
    return [v1[0]-v2[0],v1[1]-v2[1]]

def v_hash(a, b):
    return 100000*a+b

def rotate(vec, angle):
    return [int(vec[0]*math.cos(angle)-vec[1]*math.sin(angle)), int(vec[0]*math.sin(angle)+vec[1]*math.cos(angle))]

pos_to_dist = {}
pipe_poses = []
paths = {}

max_x = len(data_lines[2])
max_y = len(data_lines)

def cast_ray(pos: list, dir: list):
    if paths[v_hash(*v_add(pos, dir))]: return 0

    nums = -1
    if dir == [1, 0]:
        for x in range(pos[0]+1, max_x):
            nums += 1
            if paths[v_hash(x,pos[1])]:
                return nums
            paths[v_hash(x,pos[1])] = True
    if dir == [-1, 0]:
        for x in range(pos[0]-1, 0, -1):
            nums += 1
            if paths[v_hash(x,pos[1])]:
                return nums
            paths[v_hash(x,pos[1])] = True
    if dir == [0, 1]:
        for y in range(pos[1]+1, max_y):
            nums += 1
            if paths[v_hash(pos[0],y)]:
                return nums
            paths[v_hash(pos[0],y)] = True
    if dir == [0, -1]:
        for y in range(pos[1]-1, 0, -1):
            nums += 1
            if paths[v_hash(pos[0],y)]:
                return nums
            paths[v_hash(pos[0],y)] = True
    return 0

def make_pipe(pos, dist, og_pipe):
    if pos == og_pipe.pos:
        return og_pipe

    direction = []
    directions = pipe_to_connections[get_char(*pos)]

    if v_add(directions[0], pos) in pipe_poses:
        direction = directions[1]
    else:
        direction = directions[0]
    
    pipe_poses.append(pos)

    pos_hash = v_hash(*pos)
    if not pos_hash in pos_to_dist:
        pos_to_dist[pos_hash] = dist
    else:
        pos_to_dist[pos_hash] = min(pos_to_dist[pos_hash], dist)

    pipe = Pipe(pos, get_char(*pos), dist, make_pipe(v_add(pos, direction), dist+1, og_pipe))
    return pipe

def main():

    xy = []
    for y, line in enumerate(data_lines):
        for x, char in enumerate(line):
            paths[v_hash(x,y)] = False
            if char == "S":
                xy = [x,y]
                offset = v_add([0,-1], xy)
                make_pipe(offset, 1, Pipe(xy, "S", 0, None))
    
    
    pipe_poses.insert(0, xy)
    for a in pipe_poses:
        paths[v_hash(*a)] = True
    
    area = 0
    ray_dir = [-1,0]
    
    for pos_idx in range(1,len(pipe_poses)-1):
        pos = pipe_poses[pos_idx]
        prev_pos = pipe_poses[pos_idx-1]
        next_pos = pipe_poses[pos_idx+1]
        prev_vel = v_sub(pos, prev_pos)
        next_vel = v_sub(next_pos, pos)

        if next_vel != prev_vel:
            area += cast_ray( pos, ray_dir )
            
            if rotate(prev_vel, math.radians(90)) == next_vel:
                ray_dir = rotate(ray_dir, math.radians(90))
            else:
                ray_dir = rotate(ray_dir, math.radians(-90))

        area += cast_ray( pos, ray_dir )

    print( (max(list(pos_to_dist.values()))+1)//2, area )


sys.setrecursionlimit(100000)
main()