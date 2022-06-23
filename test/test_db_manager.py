import pytest
import logging
import json

import db_manager

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG)

@pytest.mark.parametrize('storage_type', [('storage_memory')])
def test_storage(storage_type):
    '''
    tests that `db_manager` facade works
    - namespace passed in `init()` is used correctly
    '''
    logger.info(f'{storage_type=}')

    my_db_man = db_manager.DbManager()
    my_db_man.init(storage_type, 'my_namespace')

    assert my_db_man.insert(key='key1', value='value1', overwrite=False) == True
    assert my_db_man.insert(key='key1', value='value1', namespace='another_namespace', overwrite=False) == True
    expected_content = {
        'my_namespace': {
            'key1': 'value1'
        },
        'another_namespace': {
            'key1': 'value1'
        }
    }
    assert json.loads(my_db_man.dump()) == expected_content
    assert my_db_man.delete_ns() == True
    assert my_db_man.delete_ns() == False

    expected_content = {
        'another_namespace': {
            'key1': 'value1'
        }
    }
    assert json.loads(my_db_man.dump()) == expected_content

    assert my_db_man.delete_ns('another_namespace') == True
    assert my_db_man.delete_ns('another_namespace') == False

    assert json.loads(my_db_man.dump()) == {}