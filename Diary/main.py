import mysql.connector
from datetime import date

# Replace these values with your MySQL server information
host = "localhost"
user = "root"
password = ""
database = "diary"

def create_connection():
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            print("Connected to MySQL database")
            return connection  # Return the connection object

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None  # Return None if there's an error

def close_connection(connection, cursor):
    if connection and connection.is_connected():
        cursor.close()
        connection.close()
        print("Connection closed")

def create_account():
    connection = create_connection()  # Call the create_connection function
    if connection:
        try:
            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            email = input("Enter your Email: ")
            firstname = input("Enter your First Name: ")
            lastname = input("Enter your Last Name: ")
            password = input("Enter your Password: ")

            # Example data to be inserted
            data_to_insert = {
                "email": email,
                "first_name": firstname,
                "last_name": lastname,
                "password": password,
                "date_of_creation": date.today()
            }

            # SQL query for insertion
            insert_query = "INSERT INTO users (email, first_name, last_name, password, date_of_creation) VALUES (%s, %s, %s, %s, %s)"

            # Execute the query with the data
            cursor.execute(insert_query, (
                data_to_insert["email"], data_to_insert["first_name"], data_to_insert["last_name"],data_to_insert["password"], data_to_insert["date_of_creation"]
            ))

            # Commit the changes to the database
            connection.commit()

            print("Data inserted successfully")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            # Close the connection when done
            close_connection(connection, cursor)

def login():
    pass  # You can implement the login functionality here

def main():
    # Create MySQL connection
    while True:
        print("Account Management")
        print("[1] Create an Account")
        print("[2] Login to an existing account")
        choice = input("Enter your choice: ")
        match choice:
            case "1"  : 
                create_account()
            case "2" : 
                login()
            case _  : 
                print("Please choose a valid choice!")

if __name__ == "__main__":
    main()
