import constants

data = constants.day22
data_lines = data.split("\n")

rectangles = []
fallen_rectangles = []
height_map = {}
vec3_to_rec = {}

def basis_vectors(rec):
    ret = []
    for x in range(rec[0][0], rec[1][0]+1):
        for y in range(rec[0][1], rec[1][1]+1):
            ret.append((x,y))
    return ret

def get_leaning_amount(rec):
    if rec[0][2] == 1:
        return 1
    
    count = 0
    for basis_vector in basis_vectors(rec):
        if basis_vector in height_map and height_map[basis_vector] + 1 == rec[0][2]:
            count += 1
    
    return count

def add_to_heightmap(rec):
    for vec in basis_vectors(rec):
        height_map[vec] = rec[1][2]
        vec3_to_rec[(vec[0],vec[1],rec[1][2])] = rec

def fall_rec(rec):
    return ( (rec[0][0], rec[0][1], rec[0][2]-1), (rec[1][0], rec[1][1], rec[1][2]-1) )


def main():
    
    for line_idx, line in enumerate(data_lines):
        tmp = []
        for corner in line.split("~"):
            tmp.append(tuple(map(int, corner.split(","))))
        rectangles.append(tuple(tmp))

    rectangles.sort(key=lambda rec: rec[0][2])

    for rectangle in rectangles:
        while get_leaning_amount(rectangle) == 0:
            rectangle = fall_rec(rectangle)
        add_to_heightmap(rectangle)
        fallen_rectangles.append(rectangle)
    
    important_rects = []
    tmp = fallen_rectangles.copy()
    for rectangle in fallen_rectangles:
        tmp.remove(rectangle)
        is_rect_important = True
        for other_rec in tmp:
            is_falling = True
            for basis in basis_vectors(other_rec):
                if other_rec[0][2] == 1: 
                    is_falling = False
                    break
                if (basis[0], basis[1], other_rec[0][2]-1) in vec3_to_rec:
                    if not vec3_to_rec[(basis[0], basis[1], other_rec[0][2]-1)] == rectangle:
                        is_falling = False
            if is_falling:
                is_rect_important = False
        if not is_rect_important:
            important_rects.append(rectangle)
        tmp.append(rectangle)

    height_map.clear()
    total_fallen = 0
    for rect in important_rects:
        after_rects = fallen_rectangles.copy()
        after_rects.remove(rect)
        for rectangle in after_rects:
            has_fallen = False
            while get_leaning_amount(rectangle) == 0:
                rectangle = fall_rec(rectangle)
                has_fallen = True
            if has_fallen:
                total_fallen += 1
            add_to_heightmap(rectangle)

    print(len(rectangles) - len(important_rects), total_fallen )    

main()