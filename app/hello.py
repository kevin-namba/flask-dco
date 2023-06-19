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

@app.route('/template')
def template():
    hoges = ["fuga","piyo"]
    return render_template("template.html",tests=hoges)

@app.route('/contents')
def get_contents():
    t = text("select * from contents")
    contents = session.execute(t)
    send_data = []
    for content in contents:
        send_data.append({
            "id": content.id,
            "text": content.text
        })
    return json.dumps(send_data, indent=4)

if __name__ == '__main__':
    app.run(debug=True)
