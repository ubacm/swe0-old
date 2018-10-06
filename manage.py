from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from werkzeug.contrib.fixers import ProxyFix

from swe0 import app, db


app.wsgi_app = ProxyFix(app.wsgi_app)


manager = Manager(app)
manager.add_command('db', MigrateCommand)

migrate = Migrate(app, db)


if __name__ == '__main__':
    manager.run()
