import pytest
import logging

import my_app

logger = logging.getLogger(__name__)

@pytest.fixture(params=[
    ('storage_memory'),
    # ('TODO_MAREK_storage_sqlite3')
])
def app(request):
    logger.info(f'--> app: {request.param}')
    yield my_app.create_app({'namespace': 'default', 'storage': request.param})
    logger.info(f'<-- app: {request.param}')


@pytest.fixture
def client(app):
    return app.test_client()

################################################################################

def test_rest_root(client):
    logger.info('test root: /')
    resp = client.get('/')
    assert b'flask_rest_db' in resp.data

    logger.debug(f'app is: {app}')


def test_rest_of_rest(client):
    logger.info('GET from empty')
    resp = client.get('/db/my_namespace/my_key')
    assert resp.status_code == 404

    logger.info('DELETE from empty')
    resp = client.delete('/db/my_namespace/my_key')
    assert resp.status_code == 404

    logger.info('PUT data')
    resp = client.put('/db/my_namespace/my_key', data='my_data')
    assert resp.status_code == 202

    logger.info('check PUT data')
    resp = client.get('/db/my_namespace/my_key')
    assert resp.status_code == 200
    assert resp.data == b'my_data'

    logger.info('DELETE data')
    resp = client.delete('/db/my_namespace/my_key')
    assert resp.status_code == 200

    logger.info('check DELETEd data by GET from empty')
    resp = client.get('/db/my_namespace/my_key')
    assert resp.status_code == 404

