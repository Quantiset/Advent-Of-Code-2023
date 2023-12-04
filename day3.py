
import constants

data = constants.day3
data_lines = data.split("\n")

def sum_vectors(a, b):
    return [a[0]+b[0], a[1]+b[1]]

def sort_vector_val(a):
    return a[0] + 300*a[1]

def vector_hash(a):
    return 300*a[0] + a[1]

def get_char(pos):
    return str( data_lines[pos[1]][pos[0]] )

def main():

    actual_numbers = []
    numbers = []
    symbols = []
    for line_idx, line in enumerate(data_lines):
        for word_idx, char in enumerate(line):
            if char.isdigit():
                numbers.append([word_idx, line_idx])
            elif char != ".":
                symbols.append([word_idx, line_idx])
    
    for symbol_pos in symbols:
        for x in range(3):
            x -= 1
            for y in range(3):
                y -= 1
                if [x,y]==[0,0]: continue
                summed_vector = sum_vectors(symbol_pos, [x,y])
                
                if summed_vector in numbers:
                    summed_vector_l = summed_vector
                    while summed_vector_l in numbers:
                        actual_numbers.append(summed_vector_l)
                        summed_vector_l = sum_vectors(summed_vector_l, [-1,0])
                    
                    summed_vector = sum_vectors(summed_vector, [1,0])
                    while summed_vector in numbers:
                        actual_numbers.append(summed_vector)
                        summed_vector = sum_vectors(summed_vector, [1,0])

    actual_numbers.sort(key=sort_vector_val)
    number_positions = []
    tmp = []

    for actual_number_idx in range(len(actual_numbers)):
        actual_number_idx += 1
        number_position = actual_numbers[actual_number_idx] if actual_number_idx != len(actual_numbers) else -1

        if actual_numbers[actual_number_idx-1] == number_position:
            continue
        
        tmp.append(actual_numbers[actual_number_idx-1])
        if sum_vectors( actual_numbers[actual_number_idx-1], [1,0] ) != number_position:
            number_positions.append(tmp)
            tmp = []

    sum = 0
    pos_to_num = {}
    hash_to_start = {}
    for number_pos_chain in number_positions:
        string_representation = ""
        for num_pos in number_pos_chain:
            string_representation += get_char(num_pos)
        this_number = int(string_representation)
        sum += this_number
        for num_pos in number_pos_chain:
            pos_to_num[vector_hash(num_pos)] = this_number
            hash_to_start[vector_hash(num_pos)] = vector_hash(number_pos_chain[0])
    
    gear_sums = 0
    for symbol_pos in symbols:
        if get_char(symbol_pos) == "*":
            num_numbers = 0
            gear_ratio = 0
            prev_hash = -1

            for y in range(3):
                y -= 1
                prev_hash = -1
                for x in range(3):
                    x -= 1
                    if [x,y]==[0,0]:
                        prev_hash = -1
                        continue

                    pointer_position = sum_vectors(symbol_pos, [x,y])
                    if pointer_position in actual_numbers and \
                            (prev_hash == -1 or hash_to_start[prev_hash] != hash_to_start[vector_hash(pointer_position)]):
                        prev_hash = vector_hash(pointer_position)
                        if gear_ratio == 0:
                            gear_ratio = pos_to_num[prev_hash]
                        else:
                            gear_ratio *= pos_to_num[vector_hash(pointer_position)]
                        num_numbers += 1
            
            if num_numbers == 2:
                gear_sums += gear_ratio           
    
    print(sum, gear_sums)


main()