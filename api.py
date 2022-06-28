from unicodedata import name
import requests
from requests.exceptions import HTTPError

import logging

logger = logging.getLogger(__name__)

class Api:
    '''
    synchronous API for `flask_rest_db`
    '''
    def __init__(self, db_uri: str, namespace: str) -> None:
        logger.info(f'Api init: {db_uri=} {namespace=}')
        self.db_uri = db_uri
        self.namespace = namespace


    def insert(self, key: str, value: str, namespace = None, overwrite: bool = False) -> bool:
        ns = namespace if namespace else self.namespace
        try:
            response = requests.put(f'http://{self.db_uri}/db/{ns}/{key}', data=value)
        except HTTPError as ex:
            logger.error(f'error inserting {key=}: {ex}')
            return False
        except:
            logger.error(f'error inserting {key=}: {ex}')
            return False

        return response.status_code == 202


    def get(self, key: str, namespace = None) -> str or None:
        ns = namespace if namespace else self.namespace
        try:
            response = requests.get(f'http://{self.db_uri}/db/{ns}/{key}')
        except HTTPError as ex:
            logger.error(f'error getting {key=}: {ex}')
            return None
        except:
            logger.error(f'error getting {key=}: {ex}')
            return None

        if response.status_code != 200:
            return None

        return response.content.decode('utf-8')


    def delete(self, key: str, namespace = None) -> bool:
        ns = namespace if namespace else self.namespace
        try:
            response = requests.delete(f'http://{self.db_uri}/db/{ns}/{key}')
        except HTTPError as ex:
            logger.error(f'error deleting: {ex}')
            return False
        except:
            logger.error(f'error deleting: {ex}')
            return False

        return response.status_code == 200


    def delete_ns(self, namespace = None) -> bool:
        ns = namespace if namespace else self.namespace
        raise AttributeError('not implemented yet')


    def check(self, key: str, namespace = None) -> bool:
        ns = namespace if namespace else self.namespace
        raise AttributeError('not implemented yet')
