import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv() # for fetching password from .env replace with password if needed

password = os.getenv('mysql_password')

# con1 = mysql.connector.connect(
#     host='127.0.0.1', # Similar for most servers       
#     user='root',             # similar for most user if not changed manually
#     password=f'{password}',   # different for all and set during installation
# )

# my_cursor1 = con1.cursor()

# my_cursor1.execute("create schema atm_record")

connection = mysql.connector.connect(
    host='127.0.0.1', # Similar for most servers       
    user='root',             # similar for most user if not changed manually
    password=f'{password}',   # different for all and set during installation
    database = 'atm_record' # Enter the schema name created above if mismatched or changed
)
cursor = connection.cursor()
# cursor.execute("create table atm_records(id tinyint auto_increment primary key, atm_no int not null unique, otp int not null, created_at datetime default current_timestamp, balance int not null, password int not null)")
"""
uncomment these lines only for the first time running the code these have to be commected
"""



