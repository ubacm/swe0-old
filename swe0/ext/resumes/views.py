import os

from flask import abort, redirect, render_template, request, send_file
from flask_login import current_user, login_required

from swe0 import db
from swe0.auth.models import User
from . import resumes_blueprint
from .models import Resume


@resumes_blueprint.route('')
@login_required
def index():
    resume = Resume.query.filter_by(user=current_user).first()
    return render_template('index.html', resume=resume)


@resumes_blueprint.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST' and 'resume' in request.files:
        file = request.files['resume']
        if file.filename.lower().endswith('.pdf'):
            resume = Resume.query.filter_by(user=current_user).first()
            new_filename = Resume.generate_filename()
            if resume is not None:
                # Delete existing resume.
                os.remove(resume.file_path)
            else:
                # No existing resume, so create a new one.
                resume = Resume(user=current_user)
                db.session.add(resume)
            resume.filename = new_filename
            file.save(resume.file_path)
            db.session.commit()
            return redirect(resume.url_path)
    return render_template('upload_resume.html')


@resumes_blueprint.route('/view')
@login_required
def view_list():
    if not current_user.is_admin:
        abort(403)
    resume_list = Resume.query.join(User, Resume.user).order_by(User.email).all()
    return render_template('resume_list.html', resume_list=resume_list)


@resumes_blueprint.route('/view/<filename>')
@login_required
def view(filename):
    resume = Resume.query.filter_by(filename=filename).first()
    if resume is None:
        abort(404)
    if current_user != resume.user and not current_user.is_admin:
        abort(403)
    return send_file(resume.file_path)
