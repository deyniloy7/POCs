from flask import Flask, render_template,jsonify
import pymysql
from Database import Database
from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()

app = Flask(__name__)

app.config["DEBUG"] = True

def insert_data(sqlData):
    res = es.index(index=sqlData['company'].lower(), id=sqlData['idquestions'], body=sqlData)
    return res

def employees():
    def db_query():
        db=Database()
        emps = db.list_employees()
        return  emps

    res = db_query()
    for x in res:
        print(x['company'])
        insert_data(x)

print(employees())




if __name__ == '__main__':
    app.run()
