import psycopg2

con = psycopg2.connect(database='immo', user='postgres', password='4score7', host='localhost')
cursor = con.cursor()
cursor.execute("select * from im_banken")
for row in cursor:
    print(row)
