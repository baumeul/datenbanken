from flask import Flask, render_template, request
import cx_Oracle, psycopg2

app = Flask(__name__)


@app.route('/oracle')
def do_oracle() -> 'html':
    return render_template('entry.html', the_title='Willkommen! Zur Web-Version von webapp!')


@app.route('/oraconnect', methods=['Post'])
def do_oraconnect() -> str:
    username = request.form['username']
    password = request.form['password']
    server = request.form['server']
    db = cx_Oracle.connect(username, password, server)
    version = db.version
    return version


@app.route('/postgres')
def do_postgres() -> 'html':
    con = psycopg2.connect(database='immo', user='postgres', password='4score7', host='localhost')
    cursor = con.cursor()
    cursor.execute("select count(*) from im_umsaetze")
    for rec in cursor:
        result = rec
    return str(result[0])

app.run()
