import constants
import math

data = constants.day20
data_lines = data.split("\n")

table = {}
flip_flops = []
conjunctions = []
broadcasts = []
memory = {}

queue = []

def cycle(p2 = False):
    prev_layer = set(module for module in table if "zh" in table[module])
    lengths = []

    counts = {0:0,1:0}
    presses = 0
    while True:
        presses += 1
        if presses == 1001 and not p2:
            break
        counts[0] += 1

        for broadcast_to in broadcasts:
            queue.append( ("broadcaster", 0, broadcast_to) )
        
        while len(queue) > 0:
            origin, strength, this = queue.pop(0)
            counts[strength] += 1

            if this in flip_flops and strength == 0:
                o_strength = 1
                if memory[this] == 0:
                    memory[this] = 1
                    o_strength = 1
                elif memory[this] == 1:
                    memory[this] = 0
                    o_strength = 0
                for to in table[this]:
                    queue.append( (this, o_strength, to) )
            
            elif this in conjunctions:
                memory[this][origin] = strength
                o_strength = 0
                if 0 in memory[this].values():
                    o_strength = 1
                for to in table[this]:
                    queue.append( (this, o_strength, to) )

                if this in prev_layer and o_strength == 1:
                    lengths.append(presses)
                    prev_layer.remove(this)
            
            else:
                continue
        
        if len(prev_layer) == 0 and p2:
            break
        
    
    if not p2:
        return counts[0]*counts[1]
    if p2:
        return math.lcm(*lengths)


def main():

    for line in data_lines:
        table[line.split(" -> ")[0].removeprefix("%").removeprefix("&")] = line.split(" -> ")[1].split(", ")
        if line.startswith("%"):
            flip_flops.append(line.split(" -> ")[0].removeprefix("%"))
        if line.startswith("&"):
            conjunctions.append(line.split(" -> ")[0].removeprefix("&"))
        if line.startswith("broadcaster -> "):
            for cast in line.removeprefix("broadcaster -> ").split(", "):
                broadcasts.append(cast)
    
    for conjunction in conjunctions:
        memory[conjunction] = {}
    
    for flip_flop in flip_flops:
        memory[flip_flop] = 0

    for conjunction in conjunctions:
        for origin in table:
            if conjunction in table[origin]:
                memory[conjunction][origin] = 0

    
    print(cycle(True))


main()