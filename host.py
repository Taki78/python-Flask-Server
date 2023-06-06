from flask import Flask, render_template, request, redirect, url_for, session
from funk import *

app = Flask(__name__)
app.secret_key = 'xyz'

# Route for the home page
@app.route('/')
def home():
    if 'email' in session:
        email = session['email']
        return render_template('index.html', email=email)
    else:
        return render_template('index.html')

# Route for the registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    return f_register()

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    return f_login()

# Route for logout
@app.route('/logout')
def logout():
    return f_logout()

# Route for the success page
""" @app.route('/success')
def success():
    if 'email' in session:
        email = session['email']
        return f"User registration successful! Email: {email}"
    else:
        return redirect(url_for('login')) """

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
