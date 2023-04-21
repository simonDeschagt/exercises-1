def count_older_than(people, min_age):
    def age(person):
        return person.age
    return len([age(person) for person in people if age(person) >= min_age])

def indices_of_cards_with_suit(cards, suit):
    def is_suit(card):
        return card.suit == suit
    return [cards.index(card) for card in cards if is_suit(card)]
            
