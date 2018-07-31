import sqlite3

# 1. connect 2. cursor 3. execute cursor 4. fetchall cursor
# 5. print results through iteration
# 5. close connection
connection = sqlite3.connect("jeopardy.db")
cursor = connection.cursor()

cursor.execute("SELECT game FROM category ORDER BY RANDOM() LIMIT 1")
results = cursor.fetchall()

# Get a random game
game_id = results[0][0]
print ("Categories for game #%d:" % (game_id,))

# Get the categories for the game
query = """SELECT name, round FROM category 
WHERE game=%d ORDER BY round""" % (game_id,)
cursor.execute(query)
results = cursor.fetchall()

# unpacking for tuples and lists
# example with list l= ['a', 'b', 'c']
# item1, item2, item3 = l --> yay! unpacked

# process results
for tup in results:
    # round 0 initial Jeopardy roun
    # round 1 Double Jeopardy
    # round 2 Final Jeopardy
    # name = tup[0]
    # round = tup[1]
    # now do tuple unpacking
    name, round = tup
    # Round 0: Category
    print ("Round %d: %s" % (round, name))

connection.close()


### simple commands
connection = sqlite3.connect("jeopardy.db")
cursor = connection.cursor()

cursor.execute("SELECT name FROM category LIMIT 10")
results = cursor.fetchall()
print ("results through iteration")
for category in results:
    print (category[0])
connection.close()

# now get the question, answer and dollar value form clue table
connection = sqlite3.connect("jeopardy.db")
cursor = connection.cursor()

cursor.execute("SELECT text, answer, value FROM clue LIMIT 15")
results = cursor.fetchall()
for clues in results:
    print ("Question: %s " %clues[0])
    print ("Answer: What is '%s'" %clues[1])
    print ("Dollar; %3d" %clues[2])
cursor.close()

print ('hello')
