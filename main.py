#!/usr/bin/env python3

from flask import Flask, request, Response
import logging

import http_manager
import db_manager

app = Flask(__name__)
http_man = http_manager.HttpManager()

logger = logging.getLogger(__name__)

@app.route('/')
def main_page():
    logger.info('http: / invoked')
    html = '''<h1>flask_rest_db</h1>use REST api'''
    return html


@app.route('/db/<namespace>/<key>', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def rest_api(namespace, key):
    logger.info(f'REST API invoked - method: {request.method}, path: /db/{namespace=}/{key=}')

    if request.method == 'GET':
        return http_man.do_get(k=key, ns=namespace)

    elif request.method in ['POST', 'PUT']:
        return http_man.do_put_post(k=key, d=request.get_data(), ns=namespace)

    elif request.method == 'PATCH':
        return http_man.do_patch(k=key, d=request.get_data(), ns=namespace)

    elif request.method == 'DELETE':
        return http_man.do_delete(k=key, ns=namespace)

    return http_man.do_bad_request()


if __name__ == "__main__":
    db_man = db_manager.DbManager()
    db_man.init('storage_memory', 'default')

    http_man.init(db_man)
    app.run()