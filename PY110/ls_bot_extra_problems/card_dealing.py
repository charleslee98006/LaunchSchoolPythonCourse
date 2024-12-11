def deal_cards(cards, num_players):
    even_number_of_cards = len(cards)
    while True:
        if even_number_of_cards % num_players == 0:
            break
        even_number_of_cards -= 1
    print('total:', even_number_of_cards)
    result_dict = {}
    counter = 1
    while even_number_of_cards != 0:
        card = cards.pop(0)
        if(result_dict.get(counter, None)):
            result_dict[counter].append(card)
        else:
            result_dict.setdefault(counter, [card])
        counter += 1
        if counter > num_players:
            counter = 1
        even_number_of_cards -= 1
        print(even_number_of_cards)
    print(result_dict)
    return result_dict

# Test cases
deck = ['2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH']
print(deal_cards(deck, 3) == {1: ['2H', '5H', '8H', 'JH'], 2: ['3H', '6H', '9H', 'QH'], 3: ['4H', '7H', '10H', 'KH']})
print(deal_cards(['AS', 'KS', 'QS', 'JS'], 2) == {1: ['AS', 'QS'], 2: ['KS', 'JS']})
print(deal_cards(['2D', '3D', '4D', '5D', '6D'], 5) == {1: ['2D'], 2: ['3D'], 3: ['4D'], 4: ['5D'], 5: ['6D']})