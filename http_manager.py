import logging
from flask import Response
import db_manager

logger = logging.getLogger(__name__)

class HttpManager:
    '''
    handles http calls from flask app, returning appropriate responses
    '''
    def __init__(self, ) -> None:
        logger.debug('creating HttpManager')
        self.db_manager = None

    def init(self, db_man: db_manager.DbManager):
        logger.debug('init')
        self.db_manager = db_man

    def do_get(self, k: str, ns: str):
        logger.debug(f'do_get: {k=} {ns=}')

        found_data = self.db_manager.get(key=k, namespace=ns)
        if found_data:
            return Response(status=200, response=found_data)

        return Response(status=404)

    def do_put_post(self, k: str, d: str, ns: str):
        logger.debug(f'do_put_post: {k=} "{d=}" {ns=}')

        if self.db_manager.insert(key=k, value=d, namespace=ns, overwrite=True):
            return Response(status=202)

        return Response(status=403)

    def do_patch(self, k: str, d: str, ns: str):
        logger.debug(f'do_patch: {k=} "{d=}" {ns=}')

        if not self.db_manager.check(key=k, namespace=ns):
            return Response(404)

        if self.db_manager.insert(key=k, value=d, namespace=ns, overwrite=True):
            return Response(status=200)

        return Response(404)

    def do_delete(self, k: str, ns: str):
        logger.debug(f'do_delete: {k=} {ns=}')

        if self.db_manager.delete(key=k, namespace=ns):
            return Response(status=200)

        return Response(status=404)

    def do_bad_request(self):
        logger.debug('do_bad_request')
        return Response(status=400, response='<h1>TODO MAREK bro, TODO MAREK..</h1>')
