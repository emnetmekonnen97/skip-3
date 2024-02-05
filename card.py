'''
Name: Emnet Mekonnen
CSC 201
Programming Project 4--Card Class

The Card class represents one standard poker card for a card game. Cards have a rank
and a suit. The card stores its position in a graphics window. It can be drawn and
undrawn in the graphics window.

Document Assistance: (who and what  OR  declare that you gave or received no assistance):
I received no assistance



'''
from graphics2 import *
import time

class Card:
    '''
    Card represents one standard poker card with an image to display
    
    instance variables:
    image (Image): the Image that will be displayed for the card
    rank (int): the rank of the card (ace is 1 or 14, jack is 11, queen is 12, king is 13, joker is 0)
    suit (str): the suit of the card ('h' is hearts, 'd' is diamonds, 's' is spades, 'c' is clubs, 'j' is joker) 
    '''
    def __init__(self, fileName):
        '''
        Initializes the suit, rank and image
        
        Params:
        fileName (string): name of the file which contains suit and rank of the card
        '''
        self.image = Image(Point(0, 0), fileName)
        ending = fileName.split("/")[-1]
        suit_and_rank = ending.split(".")[0]
        suit = suit_and_rank[-1]
        rank = suit_and_rank[:-1]
        self.suit = suit
        self.rank = int(rank)
        
    def getRank(self):
        '''
        Returns the rank of the cards
        
        Returns:
            the rank of the cards
        '''
        return self.rank
    
    def getSuit(self):
        '''
        Returns the suit of the cards
        
        Returns:
            the suits of the cards
        '''
        return self.suit
    
    def getImage(self):
        '''
        Returns the image of the cards
        
        Returns:
            the images of the cards
        '''
        return self.image
    
    def draw(self, window):
        '''
        Draws the cards in the window.
        
        Params:
        window(GraphWin): the window where the card will be displayed

        '''
        self.image.draw(window)
        
    def undraw(self):
        '''
        Undraws the cards in the window.

        '''
        self.image.undraw()
        
    def move(self, dx, dy):
        '''
        Moves the card dx units in the x axis and dy units in the y axis.
        
        Params:
        dx (Point): units in the x-axis
        dy (Point): units in the y-axis

        '''
        self.image.move(dx, dy)
        
    def containsPoint(self, point):
        '''
        Checks if the point is within the image boundaries
        
        Params:
        point (Point): point where the image is clicked 
        
        Returns:
        True if the point is in the image
        False if the point is outside the image

        '''
        point_left = self.image.getCenter().getX() - 1/2 * (self.image.getWidth()) 
        point_right = self.image.getCenter().getX() + 1/2 * (self.image.getWidth()) 
        point_top = self.image.getCenter().getY() - 1/2 * (self.image.getHeight())
        point_bottom = self.image.getCenter().getY() + 1/2 * (self.image.getHeight())
        
        #checks if the clicked point is within the card's boundaries
        return (point.getX() > point_left) and (point.getX() < point_right) and (point.getY() > point_top) and (point.getY() < point_bottom)

            
    def __str__(self):
        '''
        Returns a string with the suit, rank and center of the Image

        '''
        return f"suit = {self.suit}, rank = {self.rank}, center = Point({self.image.getCenter()})"
        

# test code for the Card class
def main():  
    window = GraphWin("Testing Card", 500, 500)
    
    # create King of Hearts card
    fileName = 'cards/13h.gif'
    card = Card(fileName)

    # print card using __str__ and test getRank, getSuit, getImage
    print(card)
    print(card.getRank())
    print(card.getSuit())
    print(card.getImage())
    rank = card.getRank()
    if type(rank) is int:
        print('Rank is an int as it should be.')
    elif type(rank) is str:
        print('ERROR. Rank should be an int. Yours is a string!')
    else:
        print('ERROR. Rank should be an int.')
        
    # move card to center of window and display it
    card.move(250, 250)
    card.draw(window)
    
    # click on card should move it 100 pixels left
    point = window.getMouse()
    while not card.containsPoint(point):
        point = window.getMouse()
    card.move(-100, 0)
    
    # click on card should move it 200 pixels right
    point = window.getMouse()
    while not card.containsPoint(point):
        point = window.getMouse()
    card.move(200, 0)
    
    # print the card using __str__
    print(card)
    
    # stall 2 seconds
    time.sleep(2)
    
    # create 2 of Diamonds card
    fileName = 'cards/2d.gif'
    card2 = Card(fileName)

    # print card2 using __str__ and test getRank, getSuit
    print(card2)
    print(card2.getRank())
    print(card2.getSuit())
    
    # move card to center of window and display it
    card2.move(250, 250)
    card2.draw(window)
    
    # stall 2 seconds then remove both cards from the window
    time.sleep(2)
    card.undraw()
    card2.undraw()
    
    # stall 2 seconds then close the window
    time.sleep(2)
    window.close()
    
if __name__ == '__main__':
    main()
        
        