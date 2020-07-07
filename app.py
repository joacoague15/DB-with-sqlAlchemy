from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:harrypotter9@localhost/sql_store')
connection = engine.connect()
result = connection.execute("INSERT INTO sql_store.customers (first_name, last_name) VALUES ('Franz', 'Kafka');")
result = connection.execute("SELECT * FROM sql_store.customers;")
for row in result:
    name = row['first_name']
    ln = row['last_name']
    print("name:", name, " last name:", ln)

connection.close()
