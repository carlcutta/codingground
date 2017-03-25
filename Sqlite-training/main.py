import sqlite3
import csv

conn = sqlite3.connect('example.db')
c = conn.cursor()

for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)
        
with open ('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
