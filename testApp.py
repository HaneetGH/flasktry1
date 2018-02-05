from flask import Flask
import MySQLdb
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/json")
def get():
    return "jsonValue"


@app.route("/j")
def haneet():
    myDB = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root@123", db="test")
    cHandler = myDB.cursor()
    cHandler.execute("SHOW DATABASES")
    results = cHandler.fetchall()
    for items in results:
        print(items[items])
    return "yoo"


if __name__ == '__main__':
    app.run(debug=True)
