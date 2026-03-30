from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import YourFormClass  # Replace with your actual form class

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Replace with your DB connection string
app.secret_key = 'your_secret_key'  # Replace with a secure key

db = SQLAlchemy(app)


class YourModel(db.Model):  # Replace with your actual model class
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), nullable=False)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = YourFormClass(request.form)
    if request.method == 'POST' and 'submit' in request.form:
        name = request.form['name'].strip()
        age = request.form['age'].strip()
        email = request.form['email'].strip()

        errors = []
        if not name:
            errors.append('Name field is empty.')
        if not age:
            errors.append('Age field is empty.')
        if not email:
            errors.append('Email field is empty.')

        if errors:
            return render_template('add.html', form=form, errors=errors)

        # Assuming clean input, save to the database
        new_entry = YourModel(name=name, age=age, email=email)
        db.session.add(new_entry)
        db.session.commit()

        return redirect(url_for('success'))  # Redirect to a success page

    return render_template('add.html', form=form)


@app.route('/success')
def success():
    return 'Data added successfully!'


if __name__ == '__main__':
    app.run(debug=True)
