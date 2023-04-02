from flask import Flask
from flask import request
from flask import Flask,render_template,request,redirect
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.sql import text
# import pymysql
import json

url = URL.create(
    drivername='mysql+mysqldb',
    username='test',
    password='password',
    host='db',
    database='test',
    query={"charset": "utf8"},
)
app = Flask(__name__)
engine = create_engine(url, pool_recycle=10)
session = sessionmaker(bind=engine)()

@app.route('/')
def index():
    return("hoge")

@app.route('/hoge')
def hoge():
    t = text("select * from hoges")
    hoges = session.execute(t)
    send_data = []
    for hoge in hoges:
        send_data.append({
            "id": hoge.id,
            "name": hoge.name
        })
    return json.dumps(send_data, indent=4)

@app.route('/test/<name>')
def test(name):
    t = text("insert hoges (name) values ('{}')".format(name))
    hoges = session.execute(t)
    session.commit()
    return("hoge")


if __name__ == '__main__':
    app.run(debug=True)
