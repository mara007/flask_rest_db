import logging

logger = logging.getLogger(__name__)

class BaseStorage:
    def __init__(self) -> None:
        pass

    def insert(self, key: str, value: str, ns: str = 'default', overwrite: bool = False) -> bool:
        raise AttributeError('class not for dirrect use')

    def get(self, key: str, ns: str = 'default') -> str or None:
        raise AttributeError('class not for dirrect use')

    def delete(self, key: str, ns: str = 'default') -> bool:
        raise AttributeError('class not for dirrect use')

    def delete_ns(self, ns: str = 'default') -> bool:
        raise AttributeError('class not for dirrect use')

    def check(self, key: str, ns: str):
        raise AttributeError('class not for dirrect use')

    def keys(self, ns: str = 'default') -> str:
        raise AttributeError('class not for dirrect use')

    def dump(self, do_log = False) -> str:
        raise AttributeError('class not for dirrect use')


class StorageFactory:
    storage_classes = {}

    @staticmethod
    def get_storage(type: str) -> BaseStorage:
        '''
        returns instance of storage class @type
        '''
        if not type in StorageFactory.storage_classes:
            raise AttributeError(f'uknown storage: {type=}')

        return StorageFactory.storage_classes[type]()

    @staticmethod
    def register_storage_class(type: str, cls):
        logger.debug(f'registering storage class {type=} -> {repr(cls)}')
        StorageFactory.storage_classes[type] = cls
