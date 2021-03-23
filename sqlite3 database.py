from Praw_Counter import new_final_nouns
import sqlite3
from collections import Counter
from datetime import datetime

Counter_Nouns = Counter()

conn = sqlite3.connect(r"nouns.db")
c = conn.cursor()

def Action():
    date = datetime.today().strftime("%b %Y")
    for item, number in new_final_nouns:
        c.execute("INSERT INTO Noun_Counter VALUES (?, ? , ?)", (date,item, number))
    c.execute("SELECT * FROM Noun_Counter")
    data = [i for i in c.fetchall()]
    map([Counter_Nouns.update({card: val}) for date, card, val in data], data)
    c.execute("DROP TABLE Noun_Counter")
    c.execute('''CREATE TABLE Noun_Counter (Date, Nouns, Occurences)''')
    [c.execute("INSERT INTO Noun_Counter Values(?, ?, ?)", (date, item, number)) for item, number in Counter_Nouns.items()]
    c.execute("SELECT * FROM Noun_Counter")
    conn.commit()
    conn.close()
    
try:
    c.execute('''CREATE TABLE Noun_Counter (Date, Nouns, Occurences)''')
    Action()
except sqlite3.OperationalError:
    Action()
print("done")

