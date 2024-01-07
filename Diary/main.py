import mysql.connector
from datetime import date
import time

config = {
    'host' : "localhost",
    'user' : "root",
    'password' : "",
    'database' : "diary",

    'debug': True, 
    'other_setting': 'value'
}

def create_connection():
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host = config.get('host'),
            user = config.get('user'),
            password = config.get('password'),
            database = config.get('database')
        )

        if connection.is_connected():
            pass
        return connection  # Return the connection object

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None  # Return None if there's an error

def close_connection(connection, cursor):
    if connection and connection.is_connected():
        cursor.close()
        connection.close()
        print("Connection closed")

# Account Management

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

            if config.get('debug', True):
                print("Data inserted successfully")
            else:
                pass

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            # Close the connection when done
            close_connection(connection, cursor)

def login():
    connection = create_connection()  # Call the create_connection function
    if connection:
        try:
            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            email = input("Enter your Email: ")
            password = input("Enter your Password: ")

            # SQL query for fetching user details
            select_query = "SELECT * FROM users WHERE email = %s"

            # Execute the query with the email
            cursor.execute(select_query, (email,))

            # Fetch the result
            result = cursor.fetchone()

            if result:
                # Check if the entered password matches the password from the result
                if password == result[3]:  # Assuming the password is at index 3
                    print("Login successful")
                    return True
                else:
                    print("Incorrect password")
                    return False
            else:
                print("Email does not exist")
                return False

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False
    else:
        print("Failed to connect to the database")
        return False

def account_management():
    # Create MySQL connection
    while True:  
        print("██████╗░██╗░░░██╗████████╗██╗░░██╗░█████╗░███╗░░██╗  ██████╗░██╗░█████╗░██████╗░██╗░░░██╗")
        print("██╔══██╗╚██╗░██╔╝╚══██╔══╝██║░░██║██╔══██╗████╗░██║  ██╔══██╗██║██╔══██╗██╔══██╗╚██╗░██╔╝")
        print("██████╔╝░╚████╔╝░░░░██║░░░███████║██║░░██║██╔██╗██║  ██║░░██║██║███████║██████╔╝░╚████╔╝░")
        print("██╔═══╝░░░╚██╔╝░░░░░██║░░░██╔══██║██║░░██║██║╚████║  ██║░░██║██║██╔══██║██╔══██╗░░╚██╔╝░░")
        print("██║░░░░░░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚███║  ██████╔╝██║██║░░██║██║░░██║░░░██║░░░")
        print("╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝  ╚═════╝░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░")
        print("")
        print("Loading ...")
        time.sleep(5)
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

# Posts Management

if __name__ == "__main__":
    account_management()
