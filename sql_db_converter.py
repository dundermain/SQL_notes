import pandas as pd
import sqlite3

# Function to convert CSV to .db
def csv_to_db(csv_file, db_file, table_name):
    # Read the CSV file
    df = pd.read_csv(csv_file, delimiter=',', quotechar="'")

    # Create a connection to the SQLite database
    conn = sqlite3.connect(db_file)

    # Write the dataframe to a SQLite table
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    # Close the connection
    conn.close()

# Example usage
csv_file = 'database/suppliers.csv'      # path to your CSV file
db_file = 'trial_database.db'           # name of the .db file to create
table_name = 'suppliers'  # name of the table

csv_to_db(csv_file, db_file, table_name)

print(f"CSV data has been successfully written to {db_file} as {table_name}.")

