'''
Name:Emnet Mekonnen
CSC 201
Programming Project 4--skip3.py

Skip 3 Solitaire uses one long row of cards dealt on card at a time. The
objective is to consolidate the cards into one pile using the following
rules. Two adjacent cards or two cards that are 3 apart (ie two cards
inbetween) can be consolidated into one pile is they have the same
suit or the same rank.

Document Assistance: (who and what  OR  declare that you gave or received no assistance):
Professor Mueller gave me suggestions for making my code less repetitive in the showEvaluations function

'''
from graphics2 import *
from board import CardRowBoard
from deck import Deck
from button import Button
import time

def showDirections():
    """
    Gives the directions for Skip 3 Solitaire. The "Click to begin" button
    must be clicked to continue to the game.

    """
    win = GraphWin("Directions", 700, 600)
    win.setBackground("white")
    string = ("Welcome to Skip-3 Solitaire\n\n"
                "The objective is to get all cards\n"
                "into the same pile following these rules.\n\n"
                "If two cards with the same suit or the same rank\n"
                "are either next to each other or have two cards\n"
                "between them, then click the two cards and the \n"
                "card clicked first will be placed on top of the\n"
                "card clicked second consolidating the piles.\n\n"
                "Good luck!")
    directions = Text(Point(win.getWidth()/ 2, win.getHeight()/2), string)
    directions.setSize(16)
    directions.draw(win)
    startButton = Button(Point(350, 525), 120, 40, "Click to begin")
    startButton.draw(win)
    startButton.activate()
    click = win.getMouse()
    while not startButton.isClicked(click):
        click = win.getMouse()
    win.close()

def setUpGame():
    """
    Draws the board and the button to deal the cards. It also initializes
    the board and deck of cards.
    
    Returns:
    the window for the game, the button to deal a card, the board for the game, and the deck of cards
    
    """
    window = GraphWin('Skip3 Solitare', CardRowBoard.WINDOW_WIDTH, CardRowBoard.WINDOW_HEIGHT)
    window.setBackground('green')
    
    dealCardButton = Button(Point(CardRowBoard.WINDOW_WIDTH - 100, CardRowBoard.WINDOW_HEIGHT - 30), 100, 40, "Deal Card")
    dealCardButton.draw(window)
    dealCardButton.activate()
    
    gameBoard = CardRowBoard()
    deck = Deck(False)
        
    return window, dealCardButton, gameBoard, deck

def giveMessage(window, words, numSecs):
    """
    Displays a message in the window for the number of seconds received
    
    Parameters:
    window (GraphWin): the window for the card game
    words (str): the message to be displayed in the window
    numSecs (int): the number of seconds to display the message
    """
    message = Text(Point(750, 400), words)
    message.setSize(18)
    message.setFill('red')
    message.draw(window)
    time.sleep(numSecs)
    message.undraw()
    
def initialClicks(window, gameBoard, dealCardButton, deck):
    """
    Two cards must be initially dealt to begin the game. The cards are dealt
    by clicking on a Deal Card button
    
    Parameters:
    window (GraphWin): the window for the card game
    gameBoard (CardRowBoard): the board managing the movement of the cards
    dealCardButton (Button): the button to click to deal a card
    deck (Deck): the deck of cards for the game
    
    """
    click = window.getMouse()
    while not dealCardButton.isClicked(click):
        giveMessage(window, 'You must click Deal Card twice to start the game!', 1)     
        click = window.getMouse()
    card = deck.dealCard()
    gameBoard.addCard(card, window)
    
    click = window.getMouse()
    while not dealCardButton.isClicked(click):
        giveMessage(window,'You must click Deal Card again to start the game!',1)    
        click = window.getMouse()
    card = deck.dealCard()
    gameBoard.addCard(card, window)
    
def dealCards(window, gameBoard, dealCardButton, deck):
    """
    The cards are dealt by clicking on the Deal Card button. If the player clicks on
    two cards, the cards are stacked on top of each other. The text on the deal card button
    changes to End game when the deck runs out of cards. Once the game ends evaluations are shown.
 
    Parameters:
    window (GraphWin): the window for the card game
    gameBoard (CardRowBoard): the board managing the movement of the cards
    dealCardButton (Button): the button to click to deal a card
    deck (Deck): the deck of cards for the game
    
    """
    first_click = window.getMouse()
    game_ended = False 
    
    while not game_ended:
        if dealCardButton.isClicked(first_click):
            # if the deck is Empty and End game button is clicked
            if deck.isEmpty(): 
                game_ended = True
            else:
                card = deck.dealCard()
                gameBoard.addCard(card, window)
                if deck.isEmpty(): #changes dealCard button to end game
                    dealCardButton.setLabel("End Game") 
                    giveMessage(window,'No more cards in the deck.', 1)
                    
        #if the player clicks on anything other than the deal card button or a card            
        elif gameBoard.getCardAtPoint(first_click) == None:
            giveMessage(window,'You must click on either Deal Card or a Card.', 1)
            
        #if the player clicks on a card    
        elif gameBoard.getCardAtPoint(first_click) != None:
            first_card = gameBoard.getCardAtPoint(first_click) 
            second_click = window.getMouse()
            
            # if the second click is on another card
            if gameBoard.getCardAtPoint(second_click) != None:
                second_card = gameBoard.getCardAtPoint(second_click)
                stackCards(window, gameBoard, first_card, second_card)
            else:
                giveMessage(window,'You should click on another card', 1)
           
        if not game_ended:
            first_click = window.getMouse()
        
    showEvaluations(gameBoard)
        
    
def showEvaluations(gameBoard):
    """
    Opens a new window after the game has ended. It displays the number of piles remaining
    and a message.

    Parameters:
    gameBoard (CardRowBoard): the board managing the movement of the cards
    """
    window = GraphWin("Final Results", 700, 600)
    window.setBackground("white")
    
    piles = gameBoard.getNumCardsOnBoard() # gets the number of piles left on the board
    if piles == 1:
        message = f"Wow I can't believe you won.\n\n There are still {piles} piles left on the board."
 
    elif 2 <= piles <= 4:
        message = f"So close, but you still lost\n\n There are still {piles} piles left on the board."
        
    elif 5 <= piles <= 14:
        message = f"Can't you do better?\n\n There are still {piles} piles left on the board."
        
    else:
        message = f"Gave up that easily?\n\n There are still {piles} piles left on the board. "
    
    message = Text(Point(window.getWidth()/ 2, window.getHeight()/3), message)
    message.setSize(20)
    message.draw(window)
    
        
def stackCards(window, gameBoard, first_card, second_card):
    """
    Calls getCardInfo() to get index, rank and suit of card and
    stacks the cards if the conditions are satisfied.

    Parameters:
    window (GraphWin): the window for the card game
    gameBoard (CardRowBoard): the board managing the movement of the cards
    first_card (Card): the card the first click landed on 
    second_card (Card): the card the second click landed on
    """
    index1, rank1, suit1 = getCardInfo(gameBoard, first_card)
    index2, rank2, suit2 = getCardInfo(gameBoard, second_card)
    
    #if the cards are next to each other or three apart and they have the same rank or suit the cards will be stacked
    if abs(index1 - index2 == 3) or abs(index1 - index2 == 1) and (rank1 == rank2 or suit1 == suit2):
        gameBoard.moveCard(first_card, second_card)
    else:
        giveMessage(window,'Nope, Try again.', 1)

def getCardInfo(gameBoard, card):
    """
    Gets the index, suit and rank of the card that was clicked.

    Parameters:
    gameBoard (CardRowBoard): the board managing the movement of the cards
    card (Card): the card that was clicked on last
    
    Returns:
    index (Card): the index of the card
    rank (Card): the rank of the card
    suit (Card): the suit of the card
    """
    index = gameBoard.getCardIndex(card)
    rank = card.getRank()
    suit = card.getSuit()
    
    return (index, rank, suit)        

def main():
    showDirections()
    
    window, dealCardButton, gameBoard, deck = setUpGame()

    initialClicks(window, gameBoard, dealCardButton, deck)
    
    dealCards(window, gameBoard, dealCardButton, deck)
    
  
if __name__ == '__main__':
    main()   