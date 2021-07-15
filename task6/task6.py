from flask import Flask, g, jsonify
import requests
import sqlite3

# Database Functionality
def db_get():
    if 'db' not in g:
        g.db = sqlite3.connect("task6.db")
    return g.db

def db_close(e = None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def db_store_joke(joke_json):
    STORE_JOKE_SQL = \
    """
    INSERT INTO chuck_jokes (id, joke)
    VALUES (?, ?);
    """
    cursor = db_get().cursor()
    parameters = (joke_json['id'], joke_json['value'])
    cursor.execute(STORE_JOKE_SQL, parameters)
    db_get().commit()

# Used to represent fetched rows as dictionaries, makes
# it easier to jsonify fetched data
def make_dicts(cursor, row):
    return dict((cursor.description[i][0], value)
        for i, value in enumerate(row))

def db_fetch_all_jokes():
    FETCH_ALL_JOKES_SQL = "SELECT * FROM chuck_jokes;"
    db_get().row_factory = make_dicts
    cursor = db_get().cursor()
    cursor.execute(FETCH_ALL_JOKES_SQL)
    return cursor.fetchall()

# Main App
app = Flask(__name__)

# Tell the app to close the database connection on exit
app.teardown_appcontext(db_close)

chuck_api_url = "https://api.chucknorris.io/jokes/random"

@app.route("/")
def home():
    return \
    """
    To save a random chuck norris joke, click <a href='/random_joke'>here<a/>.
    """

@app.route("/random_joke")
def save_random_joke():
    try:
        joke_json = requests.get(chuck_api_url).json()
        db_store_joke(joke_json)
        return \
        """
        A joke has been saved. 
        View all saved jokes <a href='/saved_jokes'>here<a/>
        """
    except:
        return \
        """
        Failed to save a joke. Please try again.
        """

@app.route("/saved_jokes")
def view_saved_jokes():
    return jsonify(db_fetch_all_jokes())

app.run(debug=True)
