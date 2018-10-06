import importlib


def enable_extension(app, name):
    module = importlib.import_module('swe0.ext.{}'.format(name))
    blueprint = getattr(module, '{}_blueprint'.format(name))
    app.register_blueprint(blueprint, url_prefix='/{}'.format(name.replace('_', '-')))
