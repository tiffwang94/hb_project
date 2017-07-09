print
print "Welcome to this game of Connect the Letters!"
print
print "........"
print
print "Player one, what is your name?"
print

playerone = raw_input("Player one > ")
playerone = playerone.capitalize()

print "Hello, {}!".format(playerone)
print
print "Player two, what is your name?"
print 

playertwo = raw_input("Player two >")
playertwo = playertwo.capitalize()

print "Hello, {}!".format(playertwo)
print
print "The object of this game is to connect four letters in a row, either diagonally, horizontally, or vertically."
print "Each player must choose their coordinates, first beginning from the bottom and make their way up the board."
print
print "{}, you will be using the letter 'X' and {}, you will be using the letter 'O'".format(playerone, playertwo)
print 
print "{}, you will be starting first, please choose your first coordinates.".format(playerone)