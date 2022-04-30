import mysql.connector

cnx=mysql.connector.connect(user='Rimon', password='123456',
                            host='127.0.0.1',
                            database='gs')

cursor=cnx.cursor()

query="SELECT * FROM gs.products"

cursor.execute(query)

for (product_id, name, uom_id, price_per_unit) in cursor:
    print(product_id, name, uom_id, price_per_unit)

cnx.close()