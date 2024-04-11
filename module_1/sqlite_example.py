# step 0 import sqlite3
import sqlite3
import queries as q


# step 1
# connect to the database
# tripple check the spelling of your database filename
connection =sqlite3.connect('rpg_db.sqlite3')

# step 2- Make the cursor
cursor = connection.cursor()


# step3- Write a query
# (seee the queries.py file)

#step4 - Exucute the query on the cursor and fetchthe results
# pulling the results from the cursor"
results = cursor.execute(q.SELECT_ALL).fetchall()


# The results come back as tuples
if __name__=="__main__":
    print(results[::5])

