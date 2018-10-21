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
      'description': getattr(module, 'description', ''),
      'name': name,
      'path': url_prefix,
      'pretty_name': getattr(module, 'name', name.title()),
    }


def foreign_key(db, model_class, column='id'):
    """Creates the ForeignKey schema with the table name and column name.

    Usage: field = db.Column(db.Integer, db_foreign_key(MyModel, 'optional_id')
    """
    column = '{}.{}'.format(model_class.__tablename__, column)
    return db.ForeignKey(column)
