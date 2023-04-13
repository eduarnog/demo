from flask import Blueprint, render_template, redirect, url_for, send_file
from flask_login import login_user, login_required

blueprint = Blueprint('simple_pages', __name__)

@blueprint.route('/')
def index():
  return render_template('simple_pages/index.html')

@blueprint.route('/dashboard')
@login_required
def dashboard():
  return render_template('simple_pages/dashboard.html')