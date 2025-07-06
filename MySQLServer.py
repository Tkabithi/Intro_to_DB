
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

    except mysql.connector. Error as err:
        print(f"Error while connecting to MySQL: {err}")

    finally:
        # Close cursor and connection if open
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    create_database()