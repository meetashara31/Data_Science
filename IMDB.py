import pandas as pd
import mysql.connector

# the CSV file
csv_file_path = "A:/work space/day 3/IMDB.csv"
df = pd.read_csv(csv_file_path)

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="IMDB"
)

cursor = connection.cursor()


for _, row in df.iterrows():
    sql = """
    INSERT INTO detail (Name_, duration, year_, rating)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(sql, (row['Movies'], row['Hours'], row['Year'],row['Rating']))

connection.commit()

print("Data imported successfully!")


cursor.close()
connection.close()
