import importlib


def enable_extension(app, name):
    module = importlib.import_module('swe0.ext.{}'.format(name))
    blueprint = getattr(module, '{}_blueprint'.format(name))
    url_prefix = '/{}'.format(getattr(
      module,
      'override_url_prefix',
      name.replace('_', '-')
    ))

    app.register_blueprint(blueprint, url_prefix=url_prefix)
    
    return {
      'title': name,
      'path': url_prefix,
    }
