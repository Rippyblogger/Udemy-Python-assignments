#Create Deck class
import random
import CardShuffle

class Deck:
    import random
    #import the random library
    #Set minimum and maximum bet amounts
    minimum_bet = 5
    maximum_bet = 500

    def __init__(self,amount):
        self.amount = amount


    #Create class method to accept user's bet amount input
    @classmethod
    def from_input(cls):
        return cls(
            amount = int(input("Enter the amount you wish to place your bet with: "))
            )
#Create method to print out Class instance
    def __str__(self):
        return f"{self.amount} Dollar bet placed"

#Create method for shuffling cards
    def card_shuffle(self):
        self.cards = [str(x) for x in range(2,11)]
        self.faceCards = ["A","J","Q","K"]
        self.cards.extend(self.faceCards)
        random.shuffle(self.cards)
        print(self.cards)

#create method for player to cut card
    def cutCard(self):
        print("There are 52 cards in the deck.")
        while True:
            try:
                Cards = input("Please select a number between 0 and 51 to cut: ")
                print(CardShuffle.card_shuffle(self.cards))
            except:
                print("Please enter a number between 0 and 51")







    #while amount not in range(5, 501):
     #   try:
      #      amount = int(input("Enter the amount you wish to place your bet with: "))
       # except:
        #    print("Kindly enter an amount between 5 and 500")
        #else:
         #   print("Amount Accepted")




#Method calls
Firstplay = Deck.from_input()
print(Firstplay)
Firstplay.card_shuffle()