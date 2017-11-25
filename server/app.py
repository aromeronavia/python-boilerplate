import falcon

from server.middlewares.database import DatabaseMiddleware
from database import Database


class APIResource:
    def on_get(self, req, res):
        res.status = falcon.HTTP_OK
        res.body = 'Hello world!'


class OperationsApp(falcon.API):
    def __init__(self, config, *args, **kwargs):
        super(OperationsApp, self).__init__(*args, **kwargs)
        kwargs['middleware'] = self._get_middlewares(config)
        self._configure_routes()

    def _get_middlewares(self, config):
        return [DatabaseMiddleware(Database(config))]

    def _configure_routes(self):
        self.add_route(
                '/api',
                APIResource()
            )


def app_factory(config):
    return OperationsApp(config)
