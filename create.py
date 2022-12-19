import json
import sqlite3

connection = sqlite3.connect('databaserecipes.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE Table1(area TEXT, categories TEXT,category TEXT, dish TEXT, id INT)''')

[
    {
    "area" : "Asia"
    "categories": [
    [
        {
            "category" : "Indian",
            "dish" : "Tikka Masala",
            "id" : 1
        }
        ]
    ]
    }
]





cursor.execute('''INSERT INTO Table1 VALUES(?,?,?,?)''', (area, categories, category, dish, id))
# traffic = json.load(open('output.json'))
# columns = ['name','course','roll']
#
# #
connection.commit()
connection.close()