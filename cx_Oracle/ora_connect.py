import cx_Oracle


# netcup
db = cx_Oracle.connect('immo', 'Baumeul#3270', 'netcup:1521/xe')
print(db.version)

# ovh
db = cx_Oracle.connect('immo', 'Baumeul#3270', 'ovh:1521/xe')
print(db.version)


