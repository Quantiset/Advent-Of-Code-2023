import constants

data = constants.day4
data_lines = data.split("\n")

def recur_card_count(card_idx, amount) -> int:

    line = data_lines[card_idx]
    card_nums = list(filter(None, line.split("|")[0].split(" ")[2:]))
    winning_nums = list(filter(None, line.split("|")[1].split(" ")))

    matches = 0
    for card in card_nums:
        if card in winning_nums:
            matches += 1
    if matches == 0: 
        return 1

    if amount == -1:
        amount = matches

    sum = 1
    for i in range(1, amount+1):
        add_val = recur_card_count(card_idx+i, -1)
        #print("adding", add_val, "on card", card_idx+i+1)
        sum += add_val
    return sum


def main():

    total_cards = 0
    sum = 0
    for card_idx, line in enumerate(data_lines):
        card_nums = list(filter(None, line.split("|")[0].split(" ")[2:]))
        winning_nums = list(filter(None, line.split("|")[1].split(" ")))
        
        matching_cards = 0
        factor = 0
        for card_num in card_nums:
            if card_num in winning_nums:
                matching_cards += 1
                if factor == 0:
                    factor = 1
                else:
                    factor *= 2
        sum += factor

        if matching_cards > 0:
            total_cards += recur_card_count(card_idx, matching_cards)
        else:
            total_cards += 1
            

    print(sum, total_cards)




main()