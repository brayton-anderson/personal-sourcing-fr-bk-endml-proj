from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # content = request.json
        email = request.json(["email"])
        password = request.json(["password"])

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return jsonify({"message":"Logged in!", "category":"success"})
            else:
                return jsonify({"message":"Password is incorrect.", "category":"error"})
        else:
            return jsonify({"message":"Email does not exist.", "category":"error"})

    # return render_template("login.html", user=current_user)
    return jsonify({"message":"not authenticated", "category":"error"})


@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.json(["email"])
        username = request.json(["username"])
        password1 = request.json(["password1"])
        password2 = request.json(["password2"])

        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=username).first()

        if email_exists:
            return jsonify({"message":"Email is already in use.", "category":"error"})
        elif username_exists:
            return jsonify({"message":"Username is already in use.", "category":"error"})
        elif password1 != password2:
            return jsonify({"message":"Password don\'t match!", "category":"error"})
        elif len(username) < 2:
            return jsonify({"message":"Username is too short.", "category":"error"})
        elif len(password1) < 6:
            return jsonify({"message":"Password is too short.", "category":"error"})
        elif len(email) < 4:
            return jsonify({"message":"Email is invalid.", "category":"error"})
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('User created!')
            # return redirect(url_for('views.home'))
            return jsonify({"message":"Signed in", "category":"success"})

    # return render_template("signup.html", user=current_user)
    return jsonify({"message":"not signed up", "category":"error"})

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))
