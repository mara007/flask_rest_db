import pytest
from flask import request as flask_request
import threading
from multiprocessing import Process

import logging
import time
import api
import my_app

logger = logging.getLogger(__name__)


@pytest.fixture(scope='class')
def flask_app():
    logger.info('--> starting rest_db app')

    def runner():
        logger.info('..inside sub process')
        server = my_app.create_app({'namespace': 'default', 'storage': 'storage_memory'})
        server.run(debug=True, use_reloader=False)

    flask_server = Process(target=runner)
    flask_server.start()
    time.sleep(0.5)
    yield
    logger.info('<-- stopping rest_db app')
    flask_server.terminate()
    logger.info('<-- stopped rest_db app')

@pytest.fixture(scope='class')
def client_api():
    logger.info('--> setup client API')
    yield api.Api(db_uri='localhost:5000', namespace='default')
    logger.info('<-- un setup client API')

################################################################################

@pytest.mark.usefixtures('flask_app', 'client_api')
class TestClientApi:
    def test_insert_get_keys(self, client_api: api.Api):
        assert client_api.insert(key='username', value='john') == True
        assert client_api.get(key='username') == 'john'
        assert client_api.get_keys() == ['username']
