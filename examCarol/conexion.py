import pymysql

host = 'dbflask.ckwbvo3ekhvf.us-east-1.rds.amazonaws.com'
user = 'admin'
password = 'admin1234'
database = 'dbflask'

try:
    # Establish a connection to the database
    connection = pymysql.connect(host=host, user=user, password=password, database=database)

    # Create a cursor object to interact with the database
    with connection.cursor() as cursor:
        # Execute SQL queries or database operations here

        # Example: Execute a SELECT query
        cursor.execute("SELECT * FROM your_table_name")
        results = cursor.fetchall()
        for row in results:
            print(row)

except Exception as e:
    print("Error: {}".format(e))
finally:
   # Close the database connection when done
   connection.close()
