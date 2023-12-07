import constants

data = constants.day7
data_lines = data.split("\n")

FIVE_KIND = 6
FOUR_KIND = 5
FULL = 4
THREE_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH = 0

is_day_2 = 1


temp_jok_reserve = [False, False, False, False, False]

def count(hand, alpha, amount, is_double = False):
    count_amount = 0

    for idx, char in enumerate(hand):
        if char == alpha or ((not temp_jok_reserve[idx] or not is_double) and char == "J"):
            count_amount += 1

    return count_amount == amount

def get_type(hand: str) -> int:
    type = HIGH
    temp_doub = "X"
    temp_jok_reserve[0] = False
    temp_jok_reserve[1] = False
    temp_jok_reserve[2] = False
    temp_jok_reserve[3] = False
    temp_jok_reserve[4] = False
    if hand == "JJJJJ":
        return FIVE_KIND
    for alpha in hand:
        if alpha == "J": continue
        if count(hand, alpha, 2, True) and type == ONE_PAIR and temp_doub != alpha:
            type = TWO_PAIR
        if count(hand, alpha, 2) and type < ONE_PAIR:
            type = ONE_PAIR
            temp_doub = alpha
            if hand.find("J") != -1:
                temp_jok_reserve[hand.find("J")] = True
                #print(temp_jok_reserve)
        if count(hand, alpha, 3) and type < THREE_KIND:
            type = THREE_KIND
            if (len(hand.replace(alpha, "")) == 2 and (hand.replace(alpha, "")[0] == hand.replace(alpha, "")[1])) or \
                    ( hand.count(alpha) == 2 and hand.count("J") == 1 and hand.replace(alpha, "").replace("J","")[0]==hand.replace(alpha, "").replace("J","")[1] ):
                type = FULL
        if count(hand, alpha, 4) and type < FOUR_KIND:
            type = FOUR_KIND
        if count(hand, alpha, 5) and type < FIVE_KIND:
            type = FIVE_KIND
    return type

def sort_this(arr):
    n = len(arr)
    arr_val = list(map(get_line, arr))
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if compare_hands(arr_val[j], arr_val[j + 1]):
                swapped = True
                arr_val[j], arr_val[j + 1] = arr_val[j + 1], arr_val[j]
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return

def abs_val(val: str):
    if val.isdigit():
        return int(val)
    else:
        if val == "T":
            return 10
        elif val == "J":
            return 11 - is_day_2*10
        elif val == "Q":
            return 12
        elif val == "K":
            return 13
        elif val == "A":
            return 14

def compare_hands(hand1: str, hand2: str):
    hand1type = get_type(hand1)
    hand2type = get_type(hand2)
    if hand1type == hand2type:
        for i in range(5):
            if hand1[i] == hand2[i]:
                pass
            else:
                return abs_val(hand1[i]) > abs_val(hand2[i])
        return False
    else:
        return hand1type > hand2type

def value_of_line(idx: int):
    return get_type(get_line(idx))

def get_line(idx: int):
    return data_lines[idx].split(" ")[0]

def get_bid(idx: int):
    return int(data_lines[idx].split(" ")[1])

def main():
    
    size = len(data_lines)

    indices = list(range(size))
    sort_this(indices)
    
    summed = 0
    for i, indice, indice_value in zip(list(range(size)), indices, list(map(value_of_line, indices))):
        print(i, indice, indice_value, get_line(indice))
        summed += (i + 1) * get_bid(indice)
    print(summed)



main()