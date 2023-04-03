# В самом терминале PyCharm предварительно:
#
# pip install psycopg2
# pip install names

import psycopg2
import names

try:
    # connect to exist database
    connection = psycopg2.connect(dbname="qa_ddl_33_134",
                                  user="padawan_user_134",
                                  password="123",
                                  host="159.69.151.133",
                                  port="5056")

    connection.autocommit = True

    # the cursor for perfoming database operations
    # cursor = connection.cursor()

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )

        print(f"Server version: {cursor.fetchone()}")

    # insert data into a table
    with connection.cursor() as cursor:
        for i in range(1, 2):
            employee_name = names.get_full_name()
            cursor.execute(
                """ 
                INSERT INTO employees (employee_name) 
                values (%s);
                """,
                [employee_name]
            )
            print("[INFO]"+"Insert of "+employee_name + "is added")







except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")
