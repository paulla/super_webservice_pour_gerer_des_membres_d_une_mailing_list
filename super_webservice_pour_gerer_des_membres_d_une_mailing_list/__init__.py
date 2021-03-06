from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_route('membres_liste', '/liste/{liste}/membres')
    config.scan()
    return config.make_wsgi_app()
