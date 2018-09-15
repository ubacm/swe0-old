import os

from flask import abort, redirect, render_template, request, send_file, url_for
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename

from swe0 import app
from . import resumes_blueprint


@resumes_blueprint.route('')
@login_required
def index():
    return render_template('index.html')


@resumes_blueprint.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST' and 'resume' in request.files:
        resume = request.files['resume']
        if resume.filename.lower().endswith('.pdf'):
            resume.save(_get_resume_file_path(current_user))
            return redirect(url_for('.view'))

    return render_template('upload_resume.html')


@resumes_blueprint.route('/view')
@login_required
def view():
    try:
        return send_file(_get_resume_file_path(current_user))
    except FileNotFoundError:
        abort(404)


def _get_resume_file_path(user):
    email_local, email_domain = user.email.split('@')
    filename = '{}@{}'.format(secure_filename(email_local), secure_filename(email_domain + '.pdf'))
    return os.path.join(app.config['UPLOAD_FOLDER'], 'resumes', filename)
