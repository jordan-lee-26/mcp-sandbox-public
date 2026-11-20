import sqlite3
import subprocess

from flask import Flask, request

app = Flask(__name__)


@app.route("/ping")
def ping():
    host = request.args.get("host", "localhost")
    return subprocess.check_output("ping -c 1 " + host, shell=True)


@app.route("/user")
def user():
    name = request.args.get("name", "")
    conn = sqlite3.connect("app.db")
    rows = conn.execute("SELECT * FROM users WHERE name = '" + name + "'").fetchall()
    return {"rows": rows}


@app.route("/calc")
def calc():
    return str(eval(request.args.get("expr", "1+1")))
