import constants

data = constants.day2
costs = {
    " red": 12,
    " green": 13,
    " blue": 14
}

def main():

    sum = len(data.split("\n"))*(len(data.split("\n"))+1)/2
    for idx, line in enumerate(data.split("\n")):
        idx += 1
        allow = True
        sets = line.split(":")[1].split(";")
        for set in sets:
            for color_amount in set.split(","):
                for color in costs:
                    cost = costs[color]
                    if color_amount.endswith(color) and int(color_amount.removesuffix(color)) > cost:
                        sum -= idx
                        allow = False
                        break
                if not allow: break
            if not allow: break
    print(sum)
            
def main2():

    sum = 0
    for idx, line in enumerate(data.split("\n")):
        idx += 1
        sets = line.split(":")[1].split(";")
        colors = {list(costs.keys())[0]:0,list(costs.keys())[1]:0,list(costs.keys())[2]:0}
        for set in sets:
            for color_amount in set.split(","):
                for color in costs:
                    if color_amount.endswith(color): 
                        cost = int(color_amount.removesuffix(color))
                        colors[color] = max(colors[color], cost)
        print(line, colors)
        sum += colors[list(costs.keys())[0]] * colors[list(costs.keys())[1]] * colors[list(costs.keys())[2]]
    print(sum)

main2()