import mysql.connector
print("MySQL Connector imported successfully")

mysql
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="...",
)
mycursor=mydb.cursor()
print("mysql database connected successfully")

'businessdb'
mycursor.execute("CREATE DATABASE IF NOT EXISTS businessdb")
mycursor.execute("USE businessdb")
mycursor.execute("""
CREATE TABLE IF NOT EXISTS sales_data(
    order_id int AUTO_INCREMENT PRIMARY KEY,
    product_name varchar(255),
    category varchar(100),
    quantity int,
    price_per_unit DECIMAL(10,2),
    total_sales DECIMAL(10,2)
 )
 """)
print("Table 'sales_data'created successfully")

sql_query = """
INSERT INTO sales_data(product_name,category,quantity,price_per_unit,total_sales)
VALUES(%s,%s,%s,%s,%s)
"""
records_to_insert = [
    ('Laptop','electronics',2,50000.00,100000.00),
    ('wireless mouse','electronics',5,1000.00,5000.00),
    ('office chair','furniture',3,4500.00,13500.00),
    ('coffee mug','kitchenware',10,300.00,3000.00),
    ('water bottle','kitchenware',8,500.00,4000.00)
 ]
mycursor.executemany(sql_query,records_to_insert)
mydb.commit()
print(f"{mycursor.rowcount}records inserted successfully into'sales_data'table")

import pandas as pd
query="SELECT * FROM sales_data"
df=pd.read_sql(query,mydb)
excel_file_name = "business_sales_report.xlsx"
df.to_excel(excel_file_name,index=False)
print(f"Data exported successfully to {excel_file_name}")
