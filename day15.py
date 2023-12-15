import constants

data = constants.day15

boxes = [[] for i in range(256)]
tag_to_boxes = {}

def get_hash(string):
    val = 0
    for char in string:
        val += ord(char)
        val *= 17
        val %= 256
    return val

def main():
    summed = 0
    for hashable in data.split(","):
        summed += get_hash(hashable)

        if "=" in hashable:
            lens = hashable.split("=")
            lens[1] = int(lens[1])

            tag = lens[0]
            if tag in tag_to_boxes:
                boxes[tag_to_boxes[tag][0]][tag_to_boxes[tag][1]][1] = lens[1]
            else:
                box_idx = get_hash(tag)
                boxes[box_idx].append( lens )
                tag_to_boxes[tag] = [ box_idx, len(boxes[box_idx])-1 ]

        elif "-" in hashable:
            tag = hashable.removesuffix("-")
            if tag in tag_to_boxes:
                for tag2 in boxes[tag_to_boxes[tag][0]][ tag_to_boxes[tag][1]+1: ]:
                    tag_to_boxes[tag2[0]][1] -= 1
                boxes[tag_to_boxes[tag][0]].pop(tag_to_boxes[tag][1])
                tag_to_boxes.pop(tag)

    focal_length = 0
    for box_number, box in enumerate(boxes):
        box_number += 1
        for slot_idx, lens in enumerate(box):
            slot_idx += 1
            focal_length += box_number * slot_idx * lens[1]
    print(summed, focal_length)

main() 