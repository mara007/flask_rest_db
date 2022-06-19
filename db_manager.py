import logging
from flask import Response
from db.storage import StorageFactory

logger = logging.getLogger(__name__)

class DbManager:
    def __init__(self) -> None:
        logger.info('DbManager created')
        self.db_engine = None

    def init(self, db_engine: str, namespace: str):
        self.db_engine = StorageFactory.get_storage(db_engine)

    def insert(self, key: str, value: str, namespace: str, overwrite: bool) -> Response:
        return self.db_engine.insert(key=key, value=value, ns=namespace, overwrite=overwrite)

    def get(self, key: str, namespace: str) -> Response:
        return self.db_engine.get(key=key, ns=namespace)

    def delete(self, key: str, namespace: str) -> Response:
        return self.db_engine.delete(key=key, ns=namespace)

    def delete_ns(self, namespace: str) -> Response:
        return self.db_engine.delete_ns(ns=namespace)

