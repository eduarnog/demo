from flask import Blueprint, render_template, redirect, url_for, send_file

blueprint = Blueprint('simple_pages', __name__)

@blueprint.route('/')
def index():
  return render_template('simple_pages/index.html')

@blueprint.route('/dashboard')
def dashboard():
  return render_template('simple_pages/dashboard.html')