import psycopg2

'''''Database template'''

connection = psycopg2.connect(host= "localhost", database="postgres", user= "postgres", password="WallSpeaker5" ) #to login
connection.autocommit = True #thanks to this it will automaticly add the rows

cur = connection.cursor() #defines a cursor to work with



the_name = "Stefan"
the_name1 = "Branko"

class player:
    def __init__(self, name):
        self.Name = name
        self.score = 0

player1 = player(the_name)
player2 = player(the_name1)

for i in range(0,5):
    player1.score += 2
    player2.score += 1


cur.execute("Insert into battleport_highscores VALUES (%s, %s, %s, %s)", (3, player1.Name, player1.score, 5)) #inserts date into table

