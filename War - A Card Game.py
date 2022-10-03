#CONCEPT OF THE CLASSES I THE GAME -->
#1. Card Class(SUIT, RANK, VALUE) - can make a card and print the object of card class 
#2. Deck Class - create instance for every card present and shuffle and deal a card
#3. Player - to know how many cards a player holds and to add or remove cards to deal and add after game
#4. Game logic - 
    
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
           'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


#CARD Class
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank] 
        
    def __str__(self):
        return self.rank + ' of ' + self.suit


#DECK Class
import random
class Deck():

    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                
                #create the card object
                created_card = Card(suit,rank)
                
                
                self.all_cards.append(created_card)
                
    def shuffle(self):
        
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        
        return self.all_cards.pop()
                
                
            
        
#Player Class
class Player():
    
    def __init__(self,name):
        
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            
            #If there are multiple cards to add to player
            self.all_cards.extend(new_cards)
        else:
            
            #if there is a single card to add to the player
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'



#Game Logic - Game setup, While game_on(while at war)

#Game Setup
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()


for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


game_on = True
#While game on

round_num = 0

while game_on:
    
    round_num += 1
    print(f"Round {round_num}")
    
    if len(player_one.all_cards) == 0:
        
        print("Player One, out of cards! Player Two wins!")
        
        game_on = False
        break
        
    if len(player_two.all_cards) == 0:
        
        
        print("Player Two, out of cards! Player One wins!")
        
        game_on = False
        break
        
    #Start a new round 
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
    
    #While in case of war means facing each other
    
    at_war = True
    
    while at_war:
        
        #Selected last card so that the same card dosen't appear again and again in case of war
        if player_one_cards[-1].value > player_two_cards[-1].value:
            
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            
            at_war = False
            
        
        elif player_one_cards[-1].value < player_two_cards[-1].value:
                        
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)
            
            at_war = False
            
        else:
            
            print("War...!!")
            
            if len(player_one.all_cards) < 5:#value can be changed for the variaration of the game - more card : shorter game
                print("Player One unable to declare war.. ")
                print("Player Two WINS!!")
                game_on = False
                break
                
            elif len(player_two.all_cards) < 5:
                print("Player Two unable to declare war.. ")
                print("Player One WINS!!")
                game_on = False
                break
                
            else:
                #Else the game goes on:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
                
            
            
        