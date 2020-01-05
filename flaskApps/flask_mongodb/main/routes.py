from flask import jsonify, render_template

from flask_mongodb.main import bp
from flask_mongodb.models.job import Job

@bp.route('/')
def index():
    """ Main page route. """
    button_text = "Add Job"
    return render_template('main.html', button_text=button_text)

@bp.route('/add_job')
def add_job():
    """Adds job to database."""
    new_job = Job(name = 'job1')
    new_job.insert()
    return ("", 204)