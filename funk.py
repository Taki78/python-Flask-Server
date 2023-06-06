from flask import Flask, render_template, request, redirect, url_for, session
from funk import *
import mysql.connector

def f_register():
    if request.method == 'POST':
        # Get form data from the request
        email = request.form['email']
        password = request.form['password']

        # MySQL database configuration
        db_config = {
            'host': 'localhost',
            'user': 'taki',
            'password': 'Tohid.2000',
            'database': 'Tohid_db',
        }

        try:
            # Open a connection to the MySQL database
            cnx = mysql.connector.connect(**db_config)
            cursor = cnx.cursor()

            # Check if the email already exists in the database
            query = "SELECT * FROM users WHERE email = %s"
            cursor.execute(query, (email,))
            existing_user = cursor.fetchone()

            if existing_user:
                # Email already exists, display an error message
                error_message = "Email already taken. Please choose a different email."
                return render_template('register.html', error_message=error_message)

            # Insert the new user into the database
            insert_query = "INSERT INTO users (email, password, create_date, is_active) VALUES (%s, %s, NOW(), %s)"
            user_data = (email, password, True)
            cursor.execute(insert_query, user_data)
            cnx.commit()

            # Close the database connection
            cursor.close()
            cnx.close()

            # Store the user's email in the session
            session['email'] = email

            # Redirect to a home page or any other desired page
            return redirect(url_for('home', email=email))

        except Exception as e:
            # Handle any errors that occur during the database operation
            error_message = "An error occurred: {}".format(str(e))
            return render_template('register.html', error_message=error_message)

    # If the request method is GET, render the registration form
    return render_template('register.html')


def f_login():
    if request.method == 'POST':
        # Get form data from the request
        email = request.form['email']
        password = request.form['password']

        # MySQL database configuration
        db_config = {
            'host': 'localhost',
            'user': 'taki',
            'password': 'Tohid.2000',
            'database': 'Tohid_db',
        }

        try:
            # Open a connection to the MySQL database
            cnx = mysql.connector.connect(**db_config)
            cursor = cnx.cursor()

            # Check if the email and password match in the database
            query = "SELECT * FROM users WHERE email = %s AND password = %s"
            cursor.execute(query, (email, password))
            user = cursor.fetchone()

            if user:
                # Email and password match, store the user's email in the session
                session['email'] = user[1]
                # Redirect to a home page or any other desired page
                return redirect(url_for('home', email=email))
            else:
                # Email and password do not match, display an error message
                error_message = "Invalid email or password."
                return render_template('login.html', error_message=error_message)

        except Exception as e:
            # Handle any errors that occur during the database operation
            error_message = "An error occurred: {}".format(str(e))
            return render_template('login.html', error_message=error_message)

    # If the request method is GET, render the login form
    return render_template('login.html')

def f_logout():
    session.clear()
    return redirect(url_for('home'))