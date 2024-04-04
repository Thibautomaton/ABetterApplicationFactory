from . import main
from .forms import NameForm
from ..models import User, Role
from flask import render_template, session, redirect, url_for, flash
from app import db

@main.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        if user is None:
            session["known"]=False
            new_user = User(name=form.name.data, role_id=2)
            db.session.add(new_user)
            db.session.commit()
        else:
            session["known"]=True
            flash("user is alread in database")

        return redirect(url_for('.index'))
    return render_template("index.html", form=form, known=session.get("known"))

@main.route("/admins")
def admins():
    users = Role.query.filter_by(role_name="Admin").first().users
    return render_template("users.html", users=users)

@main.route("/users")
def users():
    users = User.query.all()
    return render_template("users.html", users=users)

