import os
import uuid

from flask import url_for

from swe0 import app, db
from swe0.auth.models import User
from swe0.utils import foreign_key


class Resume(db.Model):
    __tablename__ = 'resumes_resume'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, foreign_key(db, User))
    filename = db.Column(db.String(50), nullable=False)

    user = db.relationship(User, backref=db.backref('resume', uselist=False))

    @classmethod
    def generate_filename(cls):
        def generate():
            return uuid.uuid4().hex + '.pdf'
        filename = generate()
        while db.session.query(cls.query.filter_by(filename=filename).exists()).scalar():
            # Regenerate in the unlikely event of a duplicate.
            filename = generate()
        return filename

    @property
    def file_path(self):
        return os.path.join(app.config['UPLOAD_FOLDER'], 'resumes', self.filename)

    @property
    def url_path(self):
        return url_for('resumes.view', filename=self.filename)
