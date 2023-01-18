from flask import Flask
from flask import render_template, request
from .database import cursor
from .database import Table
from datetime import datetime


app = Flask(__name__)

cursor, connection = cursor()


@app.route('/', methods=["GET", "POST"])
async def homepage():
    if request.method == "POST":
        today_date = datetime.now()
        try:
            cursor.execute(
                "INSERT INTO userinfo(id, firstname, lastname, username,password, lastlogin) VALUES ({},'{}','{}','{}','{}', '{}')".format(
                    request.form["userid"],
                    request.form["firstname"],
                    request.form["lastname"],
                    request.form["username"],
                    request.form["password"],
                    f"{today_date.year}-{today_date.month}-{today_date.day}",
                ))
            connection.commit()
        except Exception as e:
            print(e)
    return render_template('index.html')


@app.route('/database', methods=['GET', 'POST'])
async def database():
    return render_template('database.html', tables=Table())
app.run(host='192.168.111.146', port=8080)
