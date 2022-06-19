#!/usr/bin/env python3

from unicodedata import name
from flask import Flask, request, Response
from db_manager import DbManager
import logging

app = Flask(__name__)
db_mananager = DbManager()
logger = logging.getLogger(__name__)


@app.route('/')
def main_page():
    logger.info('http: / invoked')
    html = '''<h1>flask_rest_db</h1>use REST api'''
    return html


@app.route('/db/<namespace:string>/<key:string>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def rest_api(namespace, key):
    logger.info(f'REST API invoked - method: {request.method}, path: /db/{namespace=}/{key=}')

    if request.method == 'GET':
        found_data = db_mananager.get(namespace=namespace, key=key)
        if found_data:
            return Response(response=found_data, status=200)

        return Response(status=404)

    elif request.method == 'POST':
        if db_mananager.insert(namespace=namespace, key=key, value=request.get_data())
        pass
    elif request.method == 'DELETE':
        pass
    else:
        pass

    return '<i>Nothing to see here</i>'


if __name__ == "__main__":
    app.run()