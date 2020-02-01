from projectname import app, db
from flask import render_template

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/config/init/')
def init_database():
    print("Creating tables")
    db.drop_all()
    db.create_all()
    db.session.commit()
    return 'Init complete'
