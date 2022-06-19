import pytest
import logging

import db.storage

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG)

@pytest.mark.parametrize('storage_type', [('storage_memory')])
def test_storage(storage_type):
    logger.info(f'{storage_type=}')

    my_db = db.storage.StorageFactory.get_storage(storage_type)

    assert my_db.insert(key='key1', value='value1') == True
    assert my_db.insert(key='key1', value='value1') == False
    assert my_db.insert(key='key1', value='value2', overwrite=True) == True
    assert my_db.insert(key='key2', value='value2') == True

    assert my_db.get(key='key1') == 'value2'
    assert my_db.get(key='key3') == None

    assert my_db.delete_ns() == True
    assert my_db.get(key='key1') == None
    assert my_db.get(key='key2') == None