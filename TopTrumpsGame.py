from Player import Player
import Card
import pprint, time

class TopTrumpsGame(object):

    def __init__(self):
        # Initialise an array to hold all the players
        # Future expansion - many players, only one human
        self.player = []
        # This is to pretty print the json array
        self.pp = pprint.PrettyPrinter(indent=4)


    def addPlayer(self,name,cards):
        print "add player"
        self.player.append(Player(name,cards))


    def main(self):
        # Select the deck to use
        pack_name=Card.select_deck()
        # Get the deck of cards from the json file
        number_of_cards = Card.open_deck(pack_name)
        # half the deck each
        cards_to_deal = number_of_cards/2
        # Add two players
        self.addPlayer("Joseph", cards_to_deal)
        self.addPlayer("Computer", cards_to_deal)

        print "Welcome "+self.player[0].name+", good luck"
        
        # Get the cards that have been dealt.
        player_cards = self.player[0].getHand()
        computer_cards = self.player[1].getHand()

        # Player goes first
        players_turn=True

        if __name__ == '__main__':
            # main game loop
            while True:
                attr_to_use=""
                print "\n***** New Hand *****"
                # Get the cards from the top of each hand
                player_card=player_cards.pop(0)
                computer_card=computer_cards.pop(0)
                #  Get the attribute to use for either the player or computer
                if players_turn:
                    # shows the players card
                    print "~~~~~ Players Turn ~~~~~"
                    for key, value in player_card.iteritems():
                        print key + ": " + str(value)

                    # select an attribute from the current card that you think will beat your opponent
                    attr_to_use = raw_input("Select Attribute: ")
                    print "~~~~~~~~~~"
                    print "{INFO} player using: " + attr_to_use + " = " + str(player_card[attr_to_use])
                    print "{INFO} computer using: " + attr_to_use + " = " + str(computer_card[attr_to_use])
                else:
                    print "~~~~~ Computers Turn ~~~~~"
                    # prints the cards and finds the one with the highest value
                    comp_val=0
                    val_to_use=0
                    for key, value in computer_card.iteritems():
                        print key + ": " + str(value)
                        if type(value) is int:
                                if value > comp_val:
                                    attr_to_use=key
                                    val_to_use=value
                                comp_val=value
                    print "{INFO} computer using: " + attr_to_use + " = " + str(computer_card[attr_to_use])
                    print "{INFO} player using: " + attr_to_use + " = " + str(player_card[attr_to_use])
                    time.sleep(1)

                print

                # Compare the cards
                if( player_card[attr_to_use] > computer_card[attr_to_use]):
                    # You win
                    print "You Win :)"
                    # put the computers card at the back your hand
                    player_cards.append(computer_card)
                    # put your current card at the back of the hand
                    player_cards.insert(len(player_cards), player_card)
                    players_turn=True
                else:
                    # computer win
                    print "Computer won :("
                    # Put the player's card at the back of the hand
                    computer_cards.append(player_card)
                    # put current card at the back of the hand
                    computer_cards.insert(len(computer_cards), computer_card)
                    players_turn=False


                print "{INFO} You have "+str(len(player_cards))+" cards"
                print "{INFO} Computer has " + str(len(computer_cards)) + " cards"

                if len(computer_cards) < 1:
                    print "{END} Player "+self.player[0].name+" won!!!"
                    break
                if len(player_cards) < 1:
                    print "{END} Computer won!!"
                    break

TopTrumpsGame().main()

