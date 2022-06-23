import logging
from db.storage import StorageFactory

logger = logging.getLogger(__name__)

class DbManager:
    '''
    initializes storage engine and forwards calls to it
    '''
    def __init__(self) -> None:
        logger.info('DbManager created')
        self.db_engine = None
        self.namespace = ''

    def init(self, db_engine: str, namespace: str):
        self.db_engine = StorageFactory.get_storage(db_engine)
        self.namespace = namespace

    def insert(self, key: str, value: str, namespace = None, overwrite: bool = False) -> bool:
        ns = namespace if namespace else self.namespace
        return self.db_engine.insert(key=key, value=value, ns=ns, overwrite=overwrite)

    def get(self, key: str, namespace = None) -> bool:
        ns = namespace if namespace else self.namespace
        return self.db_engine.get(key=key, ns=ns)

    def delete(self, key: str, namespace = None) -> bool:
        ns = namespace if namespace else self.namespace
        return self.db_engine.delete(key=key, ns=ns)

    def delete_ns(self, namespace = None) -> bool:
        ns = namespace if namespace else self.namespace
        return self.db_engine.delete_ns(ns=ns)

    def check(self, key: str, namespace = None) -> bool:
        ns = namespace if namespace else self.namespace
        return self.db_engine.check(key=key, ns=ns)

    def dump(self, do_log: bool = False):
        return self.db_engine.dump(do_log=do_log)

