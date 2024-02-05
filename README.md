# Skip-3 Solitaire

This is a Python program that implements a card game called Skip-3 Solitaire. The game is played with a standard 52-card deck and the objective is to get all cards into the same pile following some rules.

## How to play

To play this game, you need to have Python 3 and the graphics2, board, deck, and button modules installed on your computer. You can download the game files from this GitHub repository and save them in a folder on your computer. The main file is `skip3.py`, which you can run from the command line or an IDE.

The game will first show you a window with the directions for the game and a button to start the game. After you click the button, the game will open another window with a background image of a table and a button to deal a card. You can click the button to deal a card from the deck and place it on the board.

The rules for moving cards are as follows:

- If two cards with the same suit or the same rank are either next to each other or have two cards between them, then you can click the two cards and the card clicked first will be placed on top of the card clicked second, consolidating the piles.
- You can only move cards that are not covered by other cards.
- You can only move one card at a time.

The game ends when you have either moved all cards into the same pile or there are no more possible moves. After the game ends, a new window displays the final results, showing the number of piles remaining and a message.

