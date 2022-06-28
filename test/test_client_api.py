import pytest
from flask import request as flask_request
import threading
import logging

import api
import my_app

logger = logging.getLogger(__name__)


@pytest.fixture
def app():
    logger.info('--> starting rest_db app')

    app = my_app.create_app({'namespace': 'default', 'storage': 'storage_memory'})
    t = threading.Thread(target=app.run(debug=True, use_reloader=False))
    t.run()
    yield
    logger.info('<-- stopping rest_db app')
    flask_shutdown_hook = flask_request.environ.get('werkzeug.server.shutdown')
    if flask_shutdown_hook is None:
        raise AttributeError('cant get shutdown hook')

    flask_shutdown_hook()
    t.join()

    logger.info('<-- stopped rest_db app')


def test_client_api(app):
    logger.info('testing')