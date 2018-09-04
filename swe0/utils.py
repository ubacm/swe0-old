import importlib


def enable_extension(app, name):
    module = importlib.import_module('.{}'.format(name), 'swe0.ext')
    blueprint = getattr(module, '{}_blueprint'.format(name))
    app.register_blueprint(blueprint, url_prefix='/{}'.format(name.replace('_', '-')))
