from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Verify
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def Gen_home():
 return render_template("splash.html", user=current_user)

@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
 return render_template("homeVa.html", user=current_user)
