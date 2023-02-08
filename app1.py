from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/delete/<int:sno>')
def delete(sno):
    todo = todo.show_all()
    return 'Welcome to delete Buddy!!!'


@app.route('/update')
def update():
    todo = todo.show_all()
    return 'Welcome to Update Buddy!!!'


if __name__ == '__main__':
    app.run(port=5000, debug=True)
