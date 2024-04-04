# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import click
import app
from app import db, create_app
from app.models import User, Role

app = create_app(os.getenv('FLASK_CONFIG') or'default')


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)

@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    import unittest

    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)

    else:

        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        role_admin = Role(role_name="Admin", id=1)
        role_member = Role(role_name="Member", id=2)
        user_john = User(name="John", role=role_admin)
        db.session.add_all([role_admin, role_member, user_john])
        db.session.commit()
        app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
