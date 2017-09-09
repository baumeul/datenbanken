import cx_Oracle

db = cx_Oracle.connect('system', 'Baumeul#3270', 'vb08:1521/xe')
print(db.version)
