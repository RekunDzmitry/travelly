from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from . import db
from .models import Travel
import json


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == "POST":
        travel = request.form.get('travel')
        if len(travel) < 1:
            flash('Travel is too short!', category='error')
        else:
            new_travel = Travel(data=travel, user_id=current_user.id)
            db.session.add(new_travel)
            db.session.commit()
            flash('Travel added!', category='success')
    return render_template("home.html", user=current_user)

@views.route('/delete-travel', methods=['POST'])
def delete_travel():
    travel = json.loads(request.data)
    print(f"trying to delete {travel['travelId']}")
    travelId = travel['travelId']
    travel = Travel.query.get(travelId)
    if travel:
        if travel.user_id == current_user.id:
            db.session.delete(travel)
            db.session.commit()
    return jsonify({})