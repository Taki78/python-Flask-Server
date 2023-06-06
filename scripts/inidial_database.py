import mysql.connector

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'taki',
    'password': 'Tohid.2000',
}

# Connect to MySQL server
cnx = mysql.connector.connect(**db_config)
cursor = cnx.cursor()

# Create the database
create_db_query = "CREATE DATABASE IF NOT EXISTS Tohid_db"
cursor.execute(create_db_query)

# Use the database
use_db_query = "USE Tohid_db"
cursor.execute(use_db_query)

# Create the 'users' table
create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        email NVARCHAR(255) NOT NULL,
        password NVARCHAR(255) NOT NULL,
        create_date DATETIME,
        name NVARCHAR(255),
        family NVARCHAR(255),
        phone NVARCHAR(255),
        is_active BOOLEAN
    )
"""
cursor.execute(create_table_query)

# Insert the admin user
insert_query = "INSERT INTO users (email, password, create_date, is_active) VALUES (%s, %s, NOW(), %s)"
admin_user = ('admin@example.com', 'Tohid', True)
cursor.execute(insert_query, admin_user)

# Commit the changes
cnx.commit()

# Close the cursor and the connection
cursor.close()
cnx.close()

