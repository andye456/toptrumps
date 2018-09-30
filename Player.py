from Card import CardDeck

'''
This is the player object, it selects the given number of cards randomly from the deck

'''
class Player():

    def __init__(self, name, number_of_cards):
        self.number_of_cards = number_of_cards
        self.name=name
        print "Creating player "+name+" with "+str(number_of_cards)+" cards"
        self.your_cards = []
        self.createCards()

    # loop through the number of cards required and select random ones from the deck
    def createCards(self):
        for i in range(0,self.number_of_cards):
            self.your_cards.append(CardDeck.select_random_card())


    def getHand(self):
        return self.your_cards
