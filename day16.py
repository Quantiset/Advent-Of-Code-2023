import constants

print_representation = False

data = constants.day16

data_lines = data.split("\n")
laser_directions = {a:[] for a in range(len(data_lines[0]) * len(data_lines))}

class LaserTip:
    position: int
    direction: int
    max_x = len(data_lines[0])
    max_y = len(data_lines)
    force: bool

    def __init__(self, _pos, _dir, _force=False) -> None:
        self.position = _pos
        self.direction = _dir
        self.laser_directions = laser_directions
        self.force = _force
    
    def is_ofb(self):
        return self.position < 0 or self.position >= self.max_x * self.max_y

    def step(self) -> bool:
        starting_ofb = self.is_ofb()
        cached_row = self.position // self.max_x
        self.position += self.direction
        if int(abs(self.direction)) == 1 and not self.force:
            if not starting_ofb and (self.position // self.max_x != cached_row):
                return False
            elif starting_ofb and self.is_ofb():
                return False
        else:
            if self.is_ofb():
                return False
        self.force = False
        if self.direction in self.laser_directions[self.position]:
            return False
        self.laser_directions[self.position].append(self.direction)
        return True 

    def __hash__(self) -> int:
        return hash(1000000*self.position + self.direction)

    def __repr__(self) -> str:
        return str(self.position) + " " + str(self.direction)

blockers = {}

def count_activated(laser_directions, lasers = None) -> int:
    for pos in laser_directions:
        laser_directions[pos].clear()

    activated = []
    if lasers == None:
        lasers = [LaserTip(-1,1)]
    
    def activate(pos):
        if not pos in activated:
            activated.append(pos)
    
    while len(lasers) != 0:
        #print(lasers)
        for laser in lasers.copy():
            
            out_of_bounds = False

            if not laser.step():
                lasers.remove(laser)
                continue
            activate(laser.position)
            while not laser.position in blockers:
                if not laser.step():
                    lasers.remove(laser)
                    out_of_bounds = True
                    break
                activate(laser.position)
            
            if out_of_bounds:
                continue

            blocker = blockers[laser.position]

            if blocker == "/" or blocker == "\\":
                if int(abs(laser.direction)) == 1:
                    laser.direction *= (-1 * (2*int(blocker == "/")-1) ) * len(data_lines[0])
                else:
                    laser.direction = (-1 * (2*int(blocker == "/")-1) ) * (2*int(laser.direction > 0) - 1)
            
            if blocker == "|":
                if int(abs(laser.direction)) == 1:
                    lasers.append(LaserTip(laser.position, -len(data_lines[0])))
                    lasers.append(LaserTip(laser.position, len(data_lines[0])))
                    lasers.remove(laser)
                    continue
            if blocker == "-":
                if int(abs(laser.direction)) != 1:
                    lasers.append(LaserTip(laser.position, -1))
                    lasers.append(LaserTip(laser.position, 1))
                    lasers.remove(laser)
                    continue
    
    
    out = ""
    for y in range(len(data_lines)):
        for x in range(len(data_lines[0])):
            if y*len(data_lines[0])+x in activated:
                out += "X"
            else:
                out += "."
        out += "\n"
    
    if print_representation:
        print(out)

    return len(activated)

def main():
    line_length = len(data_lines[0])
    for line_idx, line in enumerate(data_lines):
        for char_idx, char in enumerate(line):
            position = line_length * line_idx + char_idx
            if char != ".":
                blockers[position] = char

    max_tiles = 0
    max_x = len(data_lines[0])
    max_y = len(data_lines)
    for row in range(max_y):
        print( row, -1+max_x*row, max_x+max_x*row)
        max_tiles = max(max_tiles, count_activated(laser_directions,[LaserTip( -1+max_x*row, 1, True )]))
        max_tiles = max(max_tiles, count_activated(laser_directions,[LaserTip(  max_x+max_x*row, -1, True )]))
    for column in range(max_x):
        print( column, -max_x + column, max_y * max_x + column - 1 )
        max_tiles = max(max_tiles, count_activated(laser_directions,[LaserTip( -max_x + column , max_x, True )]))
        max_tiles = max(max_tiles, count_activated(laser_directions,[LaserTip( max_y * max_x + column - 1 , -max_x, True )]))   

    print(count_activated(laser_directions), max_tiles)


main()