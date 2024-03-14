"""
This file is used to connect MySQL database with
"""
import mysql.connector
from mysql.connector import Error
import datetime

def read_MySQL(table_name):
    records = None
    try:
        connection = mysql.connector.connect(
            host='fdmrjm.mysql.database.azure.com',
            database='buses',
            user='project',
            password='Cloudweek123'
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_info)
            cursor = connection.cursor(dictionary=True)
            cursor.execute(f"SELECT * FROM {table_name};")
            records = cursor.fetchall()
            print("Total number of rows in table: ", cursor.rowcount)

            for row in records:
                # Convert time columns to a human-readable format
                for key, value in row.items():
                    if isinstance(value, datetime.timedelta):
                        hours, remainder = divmod(value.seconds, 3600)
                        minutes, seconds = divmod(remainder, 60)
                        row[key] = "{:02}:{:02}:{:02}".format(hours, minutes, seconds)
                print(row)

    except Error as e:
        print("Error while connecting to MySQL", e)
        # Raise the error to let the calling code handle it
        raise e
    finally:
        if 'connection' in locals() and connection is not None and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    return records

def main():
        table = read_MySQL('buses')
        print(table)

if __name__ == '__main__':
    main()
