from flask import Flask
from flask import request
# from sqlalchemy import create_engine
# from sqlalchemy.sql import text
# from sqlalchemy.orm import sessionmaker 
import MySQLdb
# import pymysql
import json

app = Flask(__name__)
# engine = create_engine('mysql://test:password@db:3306/test')
# session = sessionmaker(bind=engine)()
conn = MySQLdb.connect(user='test',
                       password='password',
                       host='db',
                       db='test')

@app.route('/hoge')
def secret():
    return 'hoge'

@app.route('/v1/hoge', methods= ['get'])
def getAllAmount():
    query = "SELECT DISTINCT name from hoges"
    with conn.cursor(MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute(query)
        data = cursor.fetchall()
    send_data = {}
    for i in data:
        name = i["name"]
        query = "SELECT COUNT( * ) from hoges WHERE name = '" +  name + "';"
        with conn.cursor(MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute(query)
            data = cursor.fetchone()
    return json.dumps(send_data, indent=4)


if __name__ == '__main__':
    app.run(debug=True)
