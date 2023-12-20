import constants
import math
from collections import defaultdict

data = constants.day18

data_lines = data.split("\n")

use_brute_force = False # I don't want to talk about the time I spent doing this -_-

def v_add(v1, v2):
    return (v1[0]+v2[0],v1[1]+v2[1])

def v_sub(v1, v2):
    return (v1[0]-v2[0],v1[1]-v2[1])

def v_hash(a, b):
    return 100000*a+b

def rotate(vec, angle):
    return (int(vec[0]*math.cos(angle)-vec[1]*math.sin(angle)), int(vec[0]*math.sin(angle)+vec[1]*math.cos(angle)))

pos_to_dist = {}
path = []
paths = {}

def cast_ray(paths, pos: list, dir: list, mins: tuple):
    
    min_x, max_x, min_y, max_y = mins
    print(mins)

    if paths[v_add(pos, dir)]: return 0

    dir = list(dir)
    nums = -1
    if dir == [1, 0]:
        for x in range(pos[0]+1, max_x+1):
            nums += 1
            if paths[(x,pos[1])]:
                return nums
            paths[(x,pos[1])] = True
    if dir == [-1, 0]:
        for x in range(pos[0]-1, min_x-1, -1):
            
            if pos == (4, 6):
                print((x,pos[1]))
            nums += 1
            if paths[(x,pos[1])]:
                return nums
            paths[(x,pos[1])] = True
    if dir == [0, 1]:
        for y in range(pos[1]+1, max_y+1):
            nums += 1
            if paths[(pos[0],y)]:
                return nums
            paths[(pos[0],y)] = True
    if dir == [0, -1]:
        for y in range(pos[1]-1, min_y-1, -1):
            nums += 1
            if paths[(pos[0],y)]:
                return nums
            paths[(pos[0],y)] = True
    return 0

def make_vector(char, length):
    if char == "R":
        return [(i, 0) for i in range(1, length+1)]
    if char == "L":
        return [(-i, 0) for i in range(1, length+1)]
    if char == "D":
        return [(0, i) for i in range(1, length+1)]
    if char == "U":
        return [(0, -i) for i in range(1, length+1)]

def main():
    min_x, max_x, min_y, max_y = (0,0,0,0)
    vertices = []
    path = [(0,0)]
    mins = ()
    for line in data_lines:
        line = line.split(" ")
        inst = ( line[0], int(line[1]) )
        inst2 = ( line[0], int(line[1]), line[2] )
        last = path[-1] 
        vertices.append(inst2)
        for vec in make_vector(*inst):
            tmp = v_add(last, vec) 
            min_x = min(min_x, tmp[0])
            max_x = max(max_x, tmp[0])
            min_y = min(min_y, tmp[1])
            max_y = max(max_y, tmp[1])
            mins = (min_x, max_x, min_y, max_y)
            if tmp != (0,0) and not tmp in path:
                path.append( tmp )

    
    paths = defaultdict(lambda: False)
    for a in path:
        paths[a] = True
    
    area = 0
    ray_dir = (-1,0)
    
    if use_brute_force:
        for pos_idx in range(-2,len(path)-1):
            pos = path[pos_idx]
            prev_pos = path[pos_idx-1]
            next_pos = path[pos_idx+1]
            prev_vel = v_sub(pos, prev_pos)
            next_vel = v_sub(next_pos, pos)

            if next_vel != prev_vel:
                area += cast_ray( paths, pos, ray_dir, mins )
                
                if rotate(prev_vel, math.radians(90)) == next_vel:
                    ray_dir = rotate(ray_dir, math.radians(90))
                else:
                    ray_dir = rotate(ray_dir, math.radians(-90))

            area += cast_ray( paths, pos, ray_dir, mins )
            
            if pos_idx == 1:
                print(area)


        print(area + len(path))
    else:
        # shoelace + peck's after trying to brute force
        dirs = {
            "R": (1,0),
            "D": (0,1),
            "L": (-1,0),
            "U": (0,-1),
            "0": (1, 0),
            "1": (0, 1),
            "2": (-1,0),
            "3": (0,-1)
        }

        pos = 0
        ans = 1
        pos2 = 0
        ans2 = 1
        for char, steps, col in vertices:
            dir = dirs[char]
            pos += steps * dir[0]
            ans += steps * (dir[1]*pos+0.5)
        
        for char, steps, col in vertices:
            dir = dirs[col[7]]
            steps = int(col[2:7], 16)
            
            pos2 += steps * dir[0]
            ans2 += steps * (dir[1]*pos2+0.5)
        
        ans, ans2 = int(ans), int(ans2)

        print(ans, ans2) 

main()