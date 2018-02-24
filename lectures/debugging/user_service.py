from flask import Flask
import logging
import sqlite3
import os
from flask import jsonify, g, request

"""
Derived from flaskr example: http://flask.pocoo.org/docs/0.12/tutorial/
"""

app = Flask(__name__)

logging.getLogger().setLevel(logging.DEBUG)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))

db = sqlite3.connect(app.config['DATABASE'])


@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    logging.info('Initialized the database.')


def init_db():
    """Initializes the database."""
    logging.debug("init_db() ....")
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        sql = f.read()
        db.cursor().executescript(sql)
    db.commit()


def connect_db():
    """Connects to the specific database."""
    logging.info("Connecting to Database")
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    logging.info("g %s, %s", g, hasattr(g, 'sqlite_db'))
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    logging.info("Teardown")
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/users', methods=["POST"])
def create_user():
    """
    {
        "success": true/false,
        "error": {
            "code": 123,
            "message": "An error occurred!"
        }
    }
    """
    name = request.form['name']
    logging.debug("create user:%s", name)
    db = get_db()
    exists = db.execute("select * from USERS where username == ?", (name,)).fetchone()
    if exists:
        return jsonify(
            success=False,
            error={'code': 0, 'message': "exists"}
        )
    else:
        cursor = db.cursor()
        cursor.execute("insert into USERS (username) values (?)", (name,))
        id = cursor.lastrowid
        db.commit()
        return jsonify(
            success=True,
            id=id,
            error={}
        )


@app.route('/users', methods=["GET"])
def list_users():
    """
    {
    "success": true/false,
    "users": { username, username}
    "error": {
        "code": 123,
        "message": "An error occurred!"
        }
    }
    """
    logging.debug("list users ...")
    db = get_db()
    l = list(db.execute("select username from USERS"))
    l = [i[0] for i in l]
    return jsonify(
        success=True,
        users=l
    )


@app.route('/users/count', methods=["GET"])
def count_users():
    """
    {
    "success": true/false,
    "count": number
    "error": {
        "code": 123,
        "message": "An error occurred!"
        }
    }
    """
    logging.debug("count users ...")
    db = get_db()
    rows = db.execute("delete from USERS").rowcount
    db.commit()
    return jsonify(
        success=True,
        count=rows
    )

if __name__ == "__main__":
    logging.info("Starting User Service .....")
    with app.app_context():
        init_db()
    app.run(port=5001)


