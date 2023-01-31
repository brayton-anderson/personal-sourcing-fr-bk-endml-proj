from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from .models import Profile, User, Comment, Like
from . import db

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
@login_required
def home():
    profiles = Profile.query.all()
    return jsonify({"data":{"profiles": profiles, "user": current_user}})


@views.route("/update-profile", methods=['GET', 'POST'])
@login_required
def update_profile():
    if request.method == "POST":
        text = request.json(['text'])

        if not text:
            flash('Profile cannot be empty', category='error')
        else:
            profile = Profile(text=text, author=current_user.id)
            db.session.add(profile)
            db.session.commit()
            flash('Profile created!', category='success')
            return redirect(url_for('views.home'))

    # return render_template('create_profile.html', user=current_user)
    return jsonify({ "data":{"update": profile}})


@views.route("/delete-profile/<id>")
@login_required
def delete_profile(id):
    profile = Profile.query.filter_by(id=id).first()

    if not profile:
        return jsonify({"message":"Profile does not exist.", "category":"error"})
    elif current_user.id != profile.id:
        return jsonify({"message": "You do not have permission to delete this profile.", "category":"error"})
    else:
        db.session.delete(profile)
        db.session.commit()
        return jsonify({"message":"Profile deleted.", "category":"success"})

    return redirect(url_for('views.home'))


@views.route("/profiles/<username>")
@login_required
def profiles(username):
    user = User.query.filter_by(username=username).first()

    if not user:
        flash('No user with that username exists.', category='error')
        return redirect(url_for('views.home'))

    profiles = user.profiles
    return jsonify({"data":{"profiles": profiles, "user": current_user, "username": username}})


@views.route("/create-comment/<profile_id>", methods=['POST'])
@login_required
def create_comment(profile_id):
    text = request.json(['text'])

    if not text:
        return jsonify({"message": "Comment cannot be empty.", "category":"error"})
    else:
        profile = Profile.query.filter_by(id=profile_id)
        if profile:
            comment = Comment(
                text=text, author=current_user.id, profile_id=profile_id)
            db.session.add(comment)
            db.session.commit()
        else:
            return jsonify({"message":"Profile does not exist.", "category":"error"})

    return redirect(url_for('views.home'))


@views.route("/delete-comment/<comment_id>")
@login_required
def delete_comment(comment_id):
    comment = Comment.query.filter_by(id=comment_id).first()

    if not comment:
        return jsonify({'message':'Comment does not exist.', 'category':'error'})
    elif current_user.id != comment.author and current_user.id != comment.profile.author:
        return jsonify({'message':'You do not have permission to delete this comment.', 'category':'error'})
    else:
        db.session.delete(comment)
        db.session.commit()

    return redirect(url_for('views.home'))


@views.route("/like-profile/<profile_id>", methods=['POST'])
@login_required
def like(profile_id):
    profile = Profile.query.filter_by(id=profile_id).first()
    like = Like.query.filter_by(
        author=current_user.id, profile_id=profile_id).first()

    if not profile:
        return jsonify({'error': 'Profile does not exist.'}, 400)
    elif like:
        db.session.delete(like)
        db.session.commit()
    else:
        like = Like(author=current_user.id, profile_id=profile_id)
        db.session.add(like)
        db.session.commit()

    return jsonify({"likes": len(profile.likes), "liked": current_user.id in map(lambda x: x.author, profile.likes)})
