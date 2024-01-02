import constants

data = constants.day24
data_lines = data.split("\n")

hails = []

def parametric_to_cartesian(x, y):
    if y[1]/x[1] == 0: raise ZeroDivisionError
    return ( y[0]-y[1]*x[0]/x[1] , y[1]/x[1] )

def find_intersection(sys1, sys2):
    l1 = parametric_to_cartesian( (sys1[0][0],sys1[1][0]),(sys1[0][1],sys1[1][1]) )
    l2 = parametric_to_cartesian( (sys2[0][0],sys2[1][0]),(sys2[0][1],sys2[1][1]) )
    if (l2[1]-l1[1]) == 0: raise ZeroDivisionError
    x = (l1[0]-l2[0])/(l2[1]-l1[1])
    return (x, l1[0]+l1[1]*x)

def get_time_until_intersection(intersection, hail):
    return (intersection[0] - hail[0][0]) / hail[1][0]

def check_intersections_with_range(lower, higher):
    for line in data_lines:
        hails.append( (tuple(map(int, line.split(" @ ")[0].split(", "))),tuple(map(int, line.split(" @ ")[1].split(", ")))) )
    
    summed = 0
    for hail1 in hails:
        for hail2 in hails:
            
            if hail1 == hail2: continue
    
            try:
                pos = find_intersection(hail1, hail2)
                if pos[0] >= lower and pos[0] <= higher and pos[1] >= lower and pos[1] <= higher and get_time_until_intersection(pos, hail1) >= 0 and get_time_until_intersection(pos, hail2) >= 0:
                    summed += 1
            except ZeroDivisionError:
                pass
            
    return summed//2

def main():
    
    print(check_intersections_with_range(200000000000000,400000000000000))
    
main()