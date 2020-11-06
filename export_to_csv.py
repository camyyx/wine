import psycopg2
import csv

# Connect to an existing database
conn = psycopg2.connect("dbname=wine_db user=camelia password=Camtaro2302 host=localhost")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates csv file from the table
cur.execute("SELECT * FROM winePred ;")
table = cur.fetchall()

with open('export.csv', 'wb') as f:
    writer = csv.writer(f)
    #writer.writerows(table)



# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()