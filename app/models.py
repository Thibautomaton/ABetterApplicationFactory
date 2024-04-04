from app import db


class User(db.Model):
    __tablename__="users"
    name = db.Column(db.String(64), unique=True)
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))


class Role(db.Model):
    __tablename__="roles"
    role_name = db.Column(db.String(64), unique=True)
    id = db.Column(db.Integer, primary_key=True)
    users = db.relationship("User", backref="role")


"""
def init_db():
    db.drop_all()
    db.create_all()
    role_admin = Role(name="Admin", id=1)
    role_member = Role(name="Member", id=2)
    user_john = User(name="John", role=role_admin)
    db.session.add_all([role_admin, role_member, user_john])
    db.session.commit()


if __name__ == "main":
    init_db()
"""