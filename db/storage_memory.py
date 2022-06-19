import logging

from db.storage import BaseStorage, StorageFactory

logger = logging.getLogger(__name__)

class MemoryStorage(BaseStorage):
    def __init__(self) -> None:
        super().__init__()

        logger.info('creating memory storage')
        self.data = {}

    def insert(self, key: str, value: str, ns: str = 'default', overwrite: bool = False) -> bool:
        logger.debug('insert')
        if ns not in self.data:
            logger.debug(f'creating {ns=}')
            self.data[ns] = {}

        if key in self.data[ns] and not overwrite:
            logger.debug(f'{key=} already in {ns=} and {overwrite=} -> not updating')
            return False

        self.data[ns][key] = value
        return True


    def get(self, key: str, ns: str = 'default') -> str or None:
        logger.debug('get')
        if not ns in self.data:
            logger.debug(f'no {ns=}')
            return None

        if not key in self.data[ns]:
            logger.debug(f'no {key=} in {ns=}')
            return None

        result = self.data[ns][key]
        logger.info(f'returning: {ns=} - {key=}: {result=}')
        return result


    def delete(self, key: str, ns: str = 'default') -> bool:
        logger.debug('delete')
        if not ns in self.data:
            logger.debug(f'no {ns=}')
            return False

        if not key in self.data[ns]:
            logger.debug(f'no {key=} in {ns=}')
            return False

        del self.data[ns][key]
        logger.info(f'deleted: {ns=} - {key=}')
        return True

    def delete_ns(self, ns: str = 'default') -> bool:
        logger.debug('delete_ns')
        if not ns in self.data:
            logger.debug(f'no {ns=}')
            return False

        logger.info(f'deleting {ns=}')
        del self.data[ns]
        return True


StorageFactory.register_storage_class('storage_memory', MemoryStorage)