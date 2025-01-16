import pandas as pd
import mysql.connector

# the CSV file
csv_file_path = "A:/work space/flipkart_oppo_data.csv"
df = pd.read_csv(csv_file_path)



df['product_price'] = df['product_price'].replace({',': ''}, regex=True).astype(float)


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="flipkart_oppo_data"
)

cursor = connection.cursor()


for _, row in df.iterrows():
    sql = """
    INSERT INTO flipkart_oppo_data (product_name, product_price, product_rating)
    VALUES (%s, %s, %s)
    """
    cursor.execute(sql, (row['product_name'], row['product_price'], row['product_rating']))

connection.commit()

print("Data imported successfully!")


cursor.close()
connection.close()
