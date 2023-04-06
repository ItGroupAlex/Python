# В самом терминале PyCharm предварительно:
#
# pip install psycopg2
# pip install names

import psycopg2
import names
import random

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





# insert data into a table employees
    #70 random employee_name's
    with connection.cursor() as cursor:
        for i in range(0, 70):
            employee_name = names.get_full_name()
            cursor.execute(
                """
                INSERT INTO employees (employee_name)
                values (%s);
                """,
                [employee_name]
            )
            print("[INFO]"+"Insert of "+employee_name + "is added")

# counter (def), insert data into a table employee_salary
    #   №1-30(z)         random unique employee_id's from massive (1-70)
    #   №30(z)-40(z1)    random unique employee_id's from massive (71-1000)
    #       + random salary_id

    z = 30
    z1 = 40

    with connection.cursor() as cursor:
        def count():
            cursor.execute(
                """
                SELECT COUNT(*) FROM employee_salary
                """)
            return (cursor.fetchone()[0])



        l = random.sample(range(1, 70), z)
        print(l)

        counter = count()

        m = 0
        while counter < z:
            employee_id = l[m]
            salary_id = random.randint(0, 70)
            cursor.execute(
                """
                INSERT INTO employee_salary (employee_id, salary_id)
                values (%s, %s);
                """,
                (employee_id, salary_id)
            )
            print("[INFO]" + "Insert of " + str(employee_id) + " (employee_id) is added")
            m += 1
            counter = count()
        print(counter)


        l1 = random.sample(range(71, 1000), z1-z)
        print(l1)

        m = 0
        while counter < z1:
            employee_id = l1[m]
            salary_id = random.randint(0, 70)
            cursor.execute(
                """
                INSERT INTO employee_salary (employee_id, salary_id)
                values (%s, %s);
                """,
                (employee_id, salary_id)
            )
            print("[INFO]" + "Insert of " + str(employee_id) + " (employee_id) is added")
            m += 1
            counter = count()
        print(counter)





# error SQL
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
# close connection
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")
