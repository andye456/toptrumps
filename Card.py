import json
import random
from os import listdir

'''
This is the deck of cards, it opens the deck (by reading the json file) and deals one random card from the deck.
'''


cards={}

def select_deck():
    decks=listdir("data")
    for i in decks:
        print str(decks.index(i))+" "+i
    choice = raw_input("Please select a deck using it's number: ")
    return decks[int(choice)]

def open_deck(deck):
    with open("data/"+deck) as f:
        # Load the cards into a static variable
        global cards
        cards = json.load(f)
        # return the number of cards in the deck
        return len(cards)


def select_random_card():
    # Select a random index from the deck
    card = random.choice(cards)
    # Remove the randomly selected card from the deck.
    global cards
    cards.pop(cards.index(card))
    return card