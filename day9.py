import constants

data = constants.day9

data_lines = data.split("\n")

def arenotzeroes(val: list):
    for i in val:
        if i != 0:
            return True
    return False

def main():

    summed = 0
    summed2 = 0
    
    for line_idx, line in enumerate(data_lines):
        
        values = [[int(a) for a in line.split(" ")]]
        curr_level_idx = 0
        while arenotzeroes(values[curr_level_idx]):
            tmp = []
            these_values = values[curr_level_idx]
            for val_idx in range(1,len(these_values)):
                tmp.append( these_values[val_idx] - these_values[val_idx-1] )
            values.append(tmp)
            curr_level_idx += 1
        

        def get_val(idx: int):
            if arenotzeroes(values[idx]):
                return values[idx][-1] + get_val(idx+1)
            return 0
        
        def get_val2(idx: int):
            if arenotzeroes(values[idx]):
                return values[idx][0] - get_val2(idx+1)
            return 0

        summed2 += get_val2(0)
        summed += get_val(0)
        
    
    print(summed, summed2)



main()