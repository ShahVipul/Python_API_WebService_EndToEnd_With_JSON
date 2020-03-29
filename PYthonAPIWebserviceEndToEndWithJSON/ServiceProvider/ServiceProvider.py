import flask
from flask import request, jsonify
import sqlite3
import pandas as pd
import json
import requests
import os
app = flask.Flask(__name__)
app.config["DEBUG"] = True
#This App is created by Vipul Shah
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
@app.route('/', methods=['GET'])
def home():
    return '''<center><h1>This App is created by Vipul Shah</h1>
    <p>You can read the readme document for description</p></center>'''
@app.route('/api/vipul/exchangerates/curr/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('exchange_rates.db')  #database connection
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_curr = cur.execute('SELECT currency,ask_rate ex_ask_rate,bid_rate ex_bid_rate FROM ex_rates;').fetchall()
    return jsonify(all_curr)
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404
@app.route('/api/vipul/exchangerates/curr', methods=['GET'])

#This App is created by Vipul Shah

def api_filter():
    query_parameters = request.args
    currency = query_parameters.get('currency')
    ask_rate = query_parameters.get('ask_rate')
    bid_rate = query_parameters.get('bid_rate')
    query = "SELECT currency,ask_rate ex_ask_rate,bid_rate ex_bid_rate FROM ex_rates WHERE"
    to_filter = []
    if currency:
        query += ' currency=? AND'
        to_filter.append(currency)
    if ask_rate:
        query += ' ask_rate=? AND'
        to_filter.append(ask_rate)
    if bid_rate:
        query += ' bid_rate=? AND'
        to_filter.append(bid_rate)
    if not (currency or ask_rate or bid_rate):
        return page_not_found(404)
    query = query[:-4] + ';'
    conn = sqlite3.connect('exchange_rates.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    results = cur.execute(query, to_filter).fetchall()
    return jsonify(results)

app.run()
