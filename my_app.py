from flask import Flask, request
import logging

import http_manager
import db_manager

logger = logging.getLogger(__name__)

def create_app(config_params) -> Flask:
    logger.info(f'Creating Flask APP - {config_params=}')

    app = Flask(__name__)
    db_man = db_manager.DbManager()
    db_man.init(config_params['storage'], config_params['namespace'])

    http_man = http_manager.HttpManager()
    http_man.init(db_man)

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


    @app.route('/db/<namespace>', methods=['GET'])
    def rest_api_keys(namespace):
        logger.info(f'REST API invoked (keys) - method: {request.method}, path: /db/{namespace=}')
        return http_man.do_get(k=None, ns=namespace)


    return app