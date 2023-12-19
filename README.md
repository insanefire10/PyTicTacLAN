Welcome to PyTicTacLAN!
This is a simple Tic-Tac-Toe game that you and a friend can play over a LAN (Local Area Network)
For you network savvy folks out there, you can even try to play it over the internet if you are able to Port-Forward
This is a simple game I made to learn Python's socket protocol for opening up communication over LAN/The internet

How to play:
1. Player 1 will run the PyTicTacToeHost.py file on their machine. After opening the script, the console will show you the IP address and port that the guest will have to enter in
2. Player 2 will then run the PyTicTacToeGuest.py file on their machine. The console will ask them to enter in the IP and port.
3. Once Player 2 connects to Player 1 (Host) the game will start immediately. to select which coordinate to place your marker on, enter the row number and column number seperated by a space

Ex:
# # #    # # #
# # # -> # # X
# # #    # # #
Player 1 would enter "2 3" to add an X

# # #    # # #
# # # -> # # #
# # #    # O #
Player 2 would enter "3 2" to add an O

The game ends when a player gets 3 marks in a row

Ending notes:
*I am looking to turn this project into something bigger via PyGame so there will be a GUI instead of CLI-Based
