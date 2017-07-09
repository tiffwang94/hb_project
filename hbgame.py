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
print "coordinates will be chosen beginning with a number on the left and then a number on the bottom."
print
print "{}, you will be using the letter 'X' and {}, you will be using the letter 'O'".format(playerone, playertwo)
print

row_5 = ["E", "E", "E", "E", "E"]
row_4 = ["D", "D", "D", "D", "D"]
row_3 = ["C", "C", "C", "C", "C"]
row_2 = ["B", "B", "B", "B", "B"]
row_1 = ["A", "A", "A", "A", "A"]


print "5 | {} | {} | {} | {} | {} |".format(row_5[0], row_5[1], row_5[2], row_5[3], row_5[4])
print "-----------------------"
print "4 | {} | {} | {} | {} | {} |".format(row_4[0], row_4[1], row_4[2], row_4[3], row_4[4])
print "-----------------------"
print "3 | {} | {} | {} | {} | {} |".format(row_3[0], row_3[1], row_3[2], row_3[3], row_3[4])
print "-----------------------"
print "2 | {} | {} | {} | {} | {} |".format(row_2[0], row_2[1], row_2[2], row_2[3], row_2[4])
print "-----------------------"
print "1 | {} | {} | {} | {} | {} |".format(row_1[0], row_1[1], row_1[2], row_1[3], row_1[4])
print "-----------------------"
print "--- 1 - 2 - 3 - 4 - 5--"
print 
print "{}, you will be starting first, please choose your first coordinates.".format(playerone)
print "........"

#so far, players have been chosen and given their letters, grid has been  made













