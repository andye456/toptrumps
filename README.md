# Top Trumps

This is the classic card game. You start with half the deck, the computer has the other half. You present you top card's best attribute and the computer had to declare the same attribute on their top card. If yours is higher then you win their card and keep your turn, if the computers is higher you lose your card and your turn. 

## The cards
The deck of cards is in JSON format and any deck can be used.

## Usage
Put the files in the same directory and run python TopTrumpsGame.
To add new decks of cards either create your own from scratch, or check out the link below.

## TO DO:
- There is practically no error handling, you can only use attributes that have a decimal value. 
- Order the attributes so the descriptions are at the top - TBH I'm not sure why they're not.
- Make the reference to the elements a number so you don't have to type the attribute name in each time. 
- Make the static class more Pythonic (I'm from Java)

## Refernce
Many thanks to @APStats for this data
https://github.com/APStats/Top-Trumps-data

To turn it into JSON use:
https://www.csvjson.com/csv2json


