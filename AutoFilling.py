# in terminal PyCharm
# pip install psycopg2
# pip install names

import psycopg2
import names
import random

try:
    # connect to exist database
    connection = psycopg2.connect(dbname="qa_ddl_33_134",
                                  user="padawan_user_134",
                                  password="148658",
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

    employees_must = 70

    # insert data into a table employees (1st table)
    # 70 random employee_name's
    with connection.cursor() as cursor:
        def count_id_employees():
            cursor.execute(
                """
                SELECT COUNT(*) FROM employees
                """)
            return (cursor.fetchone()[0])

        while count_id_employees() < employees_must:
            for i in range(0, employees_must):
                employee_name = names.get_full_name()
                cursor.execute(
                    """
                    INSERT INTO employees (employee_name)
                    values (%s);
                    """,
                    [employee_name]
                )
                print("[INFO]" + "Insert of " + employee_name + "is added")


    # counter (def), insert data into a table employee_salary (3rd table)
    #   №1-30(z)         random unique employee_id's from massive (1-70)
    #   №30(z)-40(z1)    random unique employee_id's from massive (71-1000)
    #       + random salary_id

    z = 30
    z1 = 40

    with connection.cursor() as cursor:
        def count_employee_salary():
            cursor.execute(
                """
                SELECT COUNT(*) FROM employee_salary
                """)
            return (cursor.fetchone()[0])

        def count_idsalary():
            cursor.execute(
                """
                SELECT COUNT(*) FROM salary
                """)
            return (cursor.fetchone()[0])


        l = random.sample(range(1, count_id_employees()), z)
        print(l)

        counter = count_employee_salary()

        m = 0
        while counter < z:
            employee_id = l[m]
            salary_id = random.randint(1, count_idsalary())
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

        l1 = random.sample(range((count_id_employees()+1), 1000), z1 - z)
        print(l1)

        m = 0
        while counter < z1:
            employee_id = l1[m]
            salary_id = random.randint(1, count_idsalary())
            cursor.execute(
                """
                INSERT INTO employee_salary (employee_id, salary_id)
                values (%s, %s);
                """,
                (employee_id, salary_id)
            )
            print("[INFO]" + "Insert of " + str(employee_id) + " (employee_id) is added")
            m += 1
            counter = count_employee_salary()
        print(counter)

    # insert data into a table roles_employee (5th table)
    #   FOREIGN KEY

    z = 40

    with connection.cursor() as cursor:
        def employees_id():
            cursor.execute(
                """
                SELECT id FROM employees
                """)
            return (cursor.fetchall())


        def role_id():
            cursor.execute(
                """
                SELECT id FROM roles
                """)
            return (cursor.fetchall())


        def count_id_roles_employee():
            cursor.execute(
                """
                SELECT COUNT(*) FROM roles_employee
                """)
            return (cursor.fetchone()[0])


        employees_id_list = []
        for i in employees_id():
            employees_id_list.append(i[0])
        random.shuffle(employees_id_list)

        role_id_list = []
        for i in role_id():
            role_id_list.append(i[0])
        random.shuffle(role_id_list)

        counter = count_id_roles_employee()
        m = 0
        random_index = random.randrange(len(role_id_list))
        while counter < z:
            employee_id = employees_id_list[m]
            role_id = role_id_list[random_index]
            cursor.execute(
                """
                INSERT INTO roles_employee (employee_id, role_id)
                values (%s, %s);
                """,
                (employee_id, role_id)
            )
            print("[INFO]" + "Insert of " + str(employee_id) + " (employee_id) is added")
            m += 1
            counter = count_id_roles_employee()
            random_index = random.randrange(len(role_id_list))

        print(counter)



# error SQL
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL:", _ex)
# close connection
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")
