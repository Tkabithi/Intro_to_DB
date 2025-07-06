
import mysql.connector
from mysql.connector import Error


def create_database():
    """Create the alx_book_store database if it doesn't exist"""
    try:
        # Connect to MySQL server without specifying a database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database if not exists (won't fail if exists)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    finally:
        # Close the connection if it was established
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


if __name__ == "__main__":
    create_database()