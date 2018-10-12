import importlib


def enable_extension(app, name):
    module = importlib.import_module('swe0.ext.{}'.format(name))
    blueprint = getattr(module, '{}_blueprint'.format(name))
    url_prefix = getattr(module, 'override_url_prefix', name.replace('_', '-'))
    app.register_blueprint(blueprint, url_prefix='/{}'.format(url_prefix))
