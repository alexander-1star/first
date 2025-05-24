import sqlite3
connection = sqlite3.connect('it_step.sl3')
cur = connection.cursor()
#cur.execute('Create Table first_table (name Text;)')
cur.execute("Insert into first_table(name) Values('Nick');")
connection.commit()
connection.close()