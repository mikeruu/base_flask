from flask import Blueprint, render_template, request, redirect, session, url_for, abort, Response,make_response,jsonify

base_app = Blueprint('base_app',__name__)

@base_app.route('/base/')
def index():

    return render_template('base/index.html')
