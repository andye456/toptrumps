import json
import random

'''
This is the deck of cards, it opens the deck (by reading the json file) and deals one random card from the deck.
'''
class CardDeck():

    cards={}

    @staticmethod
    def open_deck():
        with open('dogs.json') as f:
            # Select random cards
            CardDeck.cards = json.load(f)
            return len(CardDeck.cards['cards'])


    @staticmethod
    def select_random_card():
        # Select a random index from the deck
        card = random.choice(CardDeck.cards['cards'])
        # Remove the randomly selected card from the deck.
        CardDeck.cards['cards'].pop(CardDeck.cards['cards'].index(card))
        return card