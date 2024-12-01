import mysql.connector
import json


def load_config(file_path):
    try:
        with open(file_path, 'r') as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        print(f"Config file {file_path} not found.")
        return {}


def connectionCheckinDb(hostname, username, password, dbname):
    return mysql.connector.connect(
        host=hostname,
        user=username,
        password=password,
        database=dbname
    )


def getLastPlayer(connection):
    try:
        with connection.cursor() as cursor:
            cursor = connection.cursor(dictionary=True)
            sql = "SELECT * FROM customers WHERE customerID = (SELECT customerID FROM checkin ORDER BY id DESC LIMIT 1)"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        cursor.close()
    return result


config = load_config("fa-config.json")
connection = connectionCheckinDb(
    config.get("host"),
    config.get("user"),
    config.get("password"),
    config.get("database")
)
print(getLastPlayer(connection))
connection.close()
