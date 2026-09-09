import os
import pyodbc
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

server = os.getenv("SQL_SERVER")
database = os.getenv("SQL_DATABASE")
driver = os.getenv("SQL_DRIVER")
trusted_connection = os.getenv("SQL_TRUSTED_CONNECTION")
trust_server_certificate = os.getenv("SQL_TRUST_SERVER_CERTIFICATE")

connection_string = (
    f"DRIVER={{{driver}}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"Trusted_Connection={trusted_connection};"
    f"TrustServerCertificate={trust_server_certificate};"
)

try:
    connection = pyodbc.connect(connection_string)

    print("Successfully connected to SQL Server!")
    print("Database:", connection.getinfo(pyodbc.SQL_DATABASE_NAME))

    connection.close()

except pyodbc.Error:
    print("Couldn't connect to SQL Server!")