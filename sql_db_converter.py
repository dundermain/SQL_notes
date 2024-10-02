import sqlite3
import os

# Define the directory containing the .sql files
directory = 'database'  # Change this to your directory path

# Function to convert each .sql file to a corresponding .db file
def convert_sql_to_db(sql_file):
    # Create a .db file with the same name as the .sql file
    db_file = os.path.splitext(sql_file)[0] + '.db'
    
    # Connect to the SQLite database (creates a new one if it doesn't exist)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Read the SQL file
    with open(sql_file, 'r') as file:
        sql_script = file.read()
    
    # Execute the SQL script
    cursor.executescript(sql_script)
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print(f"Database {db_file} created successfully from {sql_file}.")

# Search for all .sql files in the specified directory
for filename in os.listdir(directory):
    if filename.endswith('.sql'):
        sql_file_path = os.path.join(directory, filename)
        convert_sql_to_db(sql_file_path)
