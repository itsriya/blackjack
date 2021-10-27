#BlackJack Game
""" Functions: main():initiating the game processes and initialising the empty lists(dealer list and player list
               deal(): for playing the blackjack game.
               hit(): chosing a card randomly from the given list of cards.
               stand(): submit the sum of cards.
               compare(): compares the sum of cards of the player and the dealer
The list of cards include ace-11 or 1; king=10; queen=10; jack=10 ; 1,2,3,4,5,6,7,8,9
"""
import random
list_of_cards=[11,1,2,3,4,5,6,7,8,9,10,10,10]


def deal(player_list,dealer_list):
    
    for i in range(2):
        x=random.choice(list_of_cards)
        y=random.choice(list_of_cards)
        dealer_list.append(x)
        player_list.append(x)
    print(f"Dealer got the first card{dealer_list[0]}")
    y=sum(player_list)
    print(f"You have got cards{player_list} and the sum is{y}")
    if y<21:
        x=input("1 for hit and 0 for stand")
        user_input=int(x)
        if user_input==1:
            while(user_input==1 and y<21):
                hit(player_list, sum(player_list))
                y=sum(player_list)
                print(f"You have got cards{player_list} and the sum is{y}")
                if y<21:
                    user_input=int(input("Press 1 for hit and 0 for stand"))
                else:
                    break
                 
            stand(player_list,dealer_list)
                 
             
        
             
        elif user_input==0:
            stand(player_list,dealer_list)
        
    elif y==21 or y>21:
        stand(player_list,dealer_list)
        
        
    
    
    
        

    
    
    


def hit(player_list,sum_of_player):
     x=random.choice(list_of_cards)
     player_list.append(x)
     sum_of_player+=x
    
    
       




def stand(player_list,dealer_list):
    y=sum(dealer_list)
    while y<18:
        hit(dealer_list,y)
        y=sum(dealer_list)
    x=sum(player_list)
    y=sum(dealer_list)
    if x>21 and y>21:
        print("Draw")
    elif x>21:
        print("DEALER WON!!!!!!")
    elif x<21 and x<y:
        print("YOU WON !!!!!!!!!!")
    elif x<21 and y<21 and x<y:
        print("YOU WON!!!!!")
    elif x==21:
        print("You Won!!!!!!")
    



def main():
    dealer_list=[]
    player_list=[]
    
    user_input=input("Do You want to play the game(Y/N)?").lower()
    while user_input=='y':
        player_list.clear()
        dealer_list.clear()
        deal(player_list,dealer_list)
        user_input=input("Do you want to play the game(Y/N)?").lower()


main()
        
            
    
    
        
    
        
        
        
