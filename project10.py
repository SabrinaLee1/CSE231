##################################################
# Programming Project 10
#
# import cards
# function to initialize the game
# function to deal cards into tableau
# function to validate the moves to the foundation
# function to move the cards to the foundation
# function to validate the moves to the tableau
# function to move the cards to the tableau
# function to check for a win
# function to display the current state of the game
# function to get the option from the user
# main function to go through user inputs
# call functions to initialize game and get options
# display the start of the game
# while loop for option selection
#     if/elif/else statements for options
#         display selected option results
# closing message
# main function required code
#
#################################################
import cards  # required !!!

RULES = '''
Aces High Card Game:
     Tableau columns are numbered 1,2,3,4.
     Only the card at the bottom of a Tableau column can be moved.
     A card can be moved to the Foundation only if a higher ranked card 
     of the same suit is at the bottom of another Tableau column.
     To win, all cards except aces must be in the Foundation.'''

MENU = '''     
Input options:
    D: Deal to the Tableau (one card on each column).
    F x: Move card from Tableau column x to the Foundation.
    T x y: Move card from Tableau column x to empty Tableau column y.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game        
'''
# function to initialize the game
def init_game():
    """
    This function is used to initialize the game.
    Returns: stock (Class Deck), tableau (list of lists), foundation (list)
    """
    #make deck of cards
    deck = cards.Deck()
    deck.shuffle()
    #make a empty list to be the tableau
    tableau = []
    #deal four cards in to the tableau as their own list
    for x in range(4):
        card = deck.deal()
        tableau.append([card])
    #make an empty list for the foundation
    foundation =[]
    return (deck, tableau, foundation)  
    
# function to deal cards into tableau
def deal_to_tableau( tableau, stock):
    """
    This function is used to deal cards to the tableau.
    tableau: list of lists of the cards in the tableau (list of lists)
    stock: cards still in stock (Class Deck)
    Returns:
    """
    #if there are for or more cards still in the stock
    if len(stock) >= 4:
        #get the index of each list in the tableau
        for x, tab in enumerate(tableau):
            card = stock.deal()
            #append the card from the stock into the tableau
            tableau[x].append(card)
    #if there is less then 4 cards in the stock
    else:
        #append the remaining cards to each consecutive column
        for x, tab in enumerate(tableau):
            card = stock.deal()
            tableau.append(card)

# function to validate the moves to the foundation
def validate_move_to_foundation( tableau, from_col ):
    """
    This function is used to determine if a requested move to the foundation is valid.
    tableau: the data structure representing the tableau (list of lists)
    from_col: an int indicating the index of the column whose bottom card should be moved. (int) 
    Returns:The function will return True, if the move is valid; and False, otherwise. (bool)
    """
    #if the list is empty
    if len(tableau[from_col]) == 0:
        print("Error, empty column: {}".format(from_col +1))
        return False
    #get the last card from the list
    card = tableau[from_col][-1]
    #boolean flag to determin if move is valid or not
    moveCard=False
    #for each list in the tableau
    for x in tableau:
        #if its empty, continue
        if len(x) == 0:
            continue
        otherCard=x[-1]# check x (column) last card
        #if the last card from the list is the same the new card
        if(otherCard ==tableau[from_col][-1]):
            continue
        #making the ace card trump card
        rank = otherCard.rank()
        if rank==1:
            rank = 14
        
        card_rank = card.rank()
        if card_rank==1:
            card_rank = 14
        #check to see if the suits are the same and the rank is higher to validate
        if rank > card_rank and (otherCard.suit() == card.suit()):
            moveCard=True
    #error check for if the move is not valid
    if moveCard == False:
        print("\nError, cannot move {}.".format(card))
    return moveCard

# function to move the cards to the foundation
def move_to_foundation( tableau, foundation, from_col ):
    """
    This function is used to move a card from the tableau to the foundation.
    tableau:the data structure representing the tableau (list of lists)
    foundation:the data structure representing the foundation (list)
    from_col:an int indicating the index of the column whose bottom card should be moved. (int)
    Returns: nothing
    """
    if validate_move_to_foundation(tableau, from_col):
        lastcard = tableau[from_col].pop()
        foundation.append(lastcard)

# function to validate the moves to the tableau
def validate_move_within_tableau( tableau, from_col, to_col ):
    """
    This function to determine if a requested move to within the tableau is valid.
    tableau:the data structure representing the tableau (list of lists)
    from_col:an int indicating the index of the column whose bottom card should be moved (int)
    to_col:and an int indicating the column the card should be moved to (int)
    Returns:The function will return True, if the move is valid; and False, otherwise (bool)
    """
    #getting length of list the card will be moved to
    length_to = len(tableau[to_col])
    #if the list is not empty
    if length_to !=0:
        print("\nError, target column is not empty: {}".format(to_col+1))
        return False
    #if the list is empty and its a valid move
    #getting the length of the list
    length_from = len(tableau[from_col])
    #error check for empty list
    if length_from == 0:
        print("\nError, no card in column: {}".format(from_col+1))
        return False

    return True
# function to move the cards to the tableau
def move_within_tableau( tableau, from_col, to_col ):
    """
    This function to move a card from the tableau to the foundation.
    tableau:the data structure representing the tableau (list of lists)
    from_col:an int indicating the index of the column whose bottom card should be moved (int)
    to_col:and an int indicating the column the card should be moved to (int)
    Returns: nothing
    """
    #if the move is valid
    if validate_move_within_tableau(tableau, from_col, to_col):
        #get the card from the colum at the index
        card = tableau[from_col].pop()
        #append the card to the column it should be moved to
        tableau[to_col].append(card)

# function to check for a win        
def check_for_win( tableau, stock ):
    """
    This function to check if the game has been won.
    tableau:the data structure representing the tableau. (list of lists)
    stock: the data structure representing the stock (Class deck)
    Returns:It returns True, if the stock is empty and the tableau contains 
    only the four aces; and False, otherwise (bool)
    """
    #ace counter
    aces =0
    #go thru each list in tableau
    for lists in tableau:
        #go thru each card in list
        for card in lists:
            #if its an ace
            if card.rank() == 1:
                aces += 1
            else:
                return False
    #if there are 4 aces in the tableau, and there are no more cards to be dealt
    if aces == 4 and stock.is_empty():
        return True
    else:
        return False

# function to display the current state of the game
def display(stock, tableau, foundation ):
    '''Provided: Display the stock, tableau, and foundation.'''
    print("\n{:<8s}{:^13s}{:s}".format( "stock", "tableau", "  foundation"))
    maxm = 0
    for col in tableau:
        if len(col) > maxm:
            maxm = len(col)
    assert maxm > 0   # maxm == 0 should not happen in this game?    
    for i in range(maxm):
        if i == 0:
            if stock.is_empty():
                print("{:<8s}".format(""),end='')
            else:
                print("{:<8s}".format(" XX"),end='')
        else:
            print("{:<8s}".format(""),end='')        
        #prior_ten = False  # indicate if prior card was a ten
        for col in tableau:
            if len(col) <= i:
                print("{:4s}".format(''), end='')
            else:
                print( "{:4s}".format( str(col[i]) ), end='' )
        if i == 0:
            if len(foundation) != 0:
                print("    {}".format(foundation[-1]), end='')        
        print()

# function to get the option from the user
def get_option():
    """
    This function to prompt the user to enter an option and return a representation of the option.
    Returns: a list representation of the option to help with processing (list)
    """
    #make a list of entered option
    option = input("\nInput an option (DFTRHQ): ").strip().split()
    try:
        if option[0].upper() == "D" and len(option)==1:
            return [option[0].upper()]
        elif len(option)==1 and option[0].upper() == "R":
            return [option[0].upper()]
        elif len(option)==1 and option[0].upper() == "H":
            return [option[0].upper()]
        elif len(option)==1 and option[0].upper() == "Q":
            return [option[0].upper()]
            #check that the option list has 2 elements
        elif len(option) == 2 and option[0].upper() == "F" :
            #check the numbers are numeric and between 1 and 4
            if option[1].isnumeric() and int(option[1]) >= 1\
            and int(option[1]) <=4:
                #get the actual representation of the number by subracting one
                option[1]= int(option[1])-1
                #return the list verison of option
                return [option[0].upper(), int(option[1])]
            else:
                print(f"\nError in option: " + " ".join(option))
                return []   
        #check that the option list has 3 elements
        elif len(option)==3 and option[0].upper() == "T" :
            #check the numbers are numeric and between 1 and 4
            if option[1].isnumeric() and option[2].isnumeric() and\
            int(option[1]) >= 1 and int(option[1]) <=4 and\
            int(option[2]) >= 1 and int(option[2]) <=4:
                #get the actual representation of the number by subracting one
                option[1]= int(option[1])-1
                option[2]= int(option[2])-1
                return [option[0].upper(), int(option[1]), int(option[2])]
            else:
                print(f"\nError in option: " + " ".join(option))
                return []
        else:
            print(f"\nError in option: " + " ".join(option))
            return []   
    except:
        return []
        
# main function to go through user inputs        
def main():
    #initialize game
    (deck, tableau, foundation) = init_game()
    #print rules
    print(RULES)
    #print menu
    print(MENU)
    #display how the game starts
    display(deck, tableau, foundation)
    #get the option from the user
    option = get_option()
    while True:
        #checking if it returns an empty list or not
        if len(option)>0:
            if option[0]=="Q":
                print("\nYou have chosen to quit.")
                break
            if option[0] == 'H':
                print(MENU)
            elif option[0] == 'R':
                #re init game
                (deck, tableau, foundation) = init_game()
                print("\n=========== Restarting: new game ============")
                print(RULES)
                print(MENU)     
            elif option[0] == 'D':
                deal_to_tableau(tableau, deck)    
            elif option[0] == 'F':
                move_to_foundation(tableau, foundation, option[1])
            elif option[0] == 'T':
                move_within_tableau(tableau, option[1], option[2])
            if check_for_win(tableau,deck)==True:
                print("\nYou won!")
                break
            else:
                display(deck, tableau, foundation)
        #always asks for an option
        option = get_option()
  

if __name__ == '__main__':
     main()

