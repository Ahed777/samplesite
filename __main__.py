from flask import Flask
from flask import render_template, request
from .database import cursor
from .database import Table
app = Flask(__name__)

cursor, connection = cursor()


@app.route('/', methods=["GET", "POST"])
async def homepage():
    if request.method == "POST":
        try:
            cursor.execute(
                "INSERT INTO userinfo(id, firstname, lastname, password,username, lastlogin) VALUES ({},'{}','{}','{}','{}', '{}')".format(
                    request.form["userid"],
                    request.form["firstname"],
                    request.form["lastname"],
                    request.form["password"],
                    request.form["username"],
                    "2022-08-23",
                ))
            connection.commit()
        except Exception as e:
            print(e)
    return render_template('index.html')


@app.route('/database', methods=['GET', 'POST'])
async def database():
    return render_template('database.html', tables=Table())
app.run(host='192.168.111.146', port=8080)
