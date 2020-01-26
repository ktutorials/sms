import psycopg2
import logging

def get_students():
    connection = ""

    try:
        connection = psycopg2.connect(user="smsadmin",
                                      password="",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="sms")

        cursor = connection.cursor()

        logging.info("Connected to database.")

        table_name = "public.\"Students\""

        std_select_query = """ SELECT * FROM {tn} """.format(tn=table_name)
        cursor.execute(std_select_query)
        count = cursor.rowcount
        logging.info(count, " records in students table")
        rows = cursor.fetchall()
        description = cursor.description
        students = []
        for row in rows:
            student = {}
            for coldesc in description:
                col = coldesc.name
                student[col] = row[coldesc.table_column - 1]
            students.append(student)
        return {'students': students}

    except (Exception, psycopg2.Error) as error :
        logging.error("Failed to select record from students table", error)
        return False, error

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            logging.info("PostgreSQL connection is closed")


def add_student(student):

    connection = ""

    try:
       connection = psycopg2.connect(user="smsadmin",
                                      password="",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="sms")

       cursor = connection.cursor()

       logging.info("Connected to database.")

       table_name = "public.\"Students\""

       std_insert_query = (
           " INSERT INTO {tn}"
           "(\"Name\",\"Age\",\"Grade\",\"IsFunClub\",\"Address\",\"EmergencyContact\",\"ParentContact\",\"Hobbies\")"
           " VALUES (%s,%s,%s,%s,%s,%s,%s,%s)".format(tn=table_name)
       )
       record_to_insert = (student["name"], student["age"],
                           student["grade"], student["funClub"], student["address"],
                           student["emergencyContact"], student["parentContact"],
                           student["hobbies"])

       cursor.execute(std_insert_query, record_to_insert)

       connection.commit()
       count = cursor.rowcount

       logging.info (count, "Record inserted successfully into sudents table")

       if count == 1:
           return True, None
       else:
           return False, None

    except (Exception, psycopg2.Error) as error :
        logging.error("Failed to insert record into students table", error)
        return False, error

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            logging.info("PostgreSQL connection is closed")

    def query():
        '''std_select_query = """ SELECT * FROM {tn} """.format(tn=table_name)
               cursor.execute(std_select_query)
               count = cursor.rowcount
               logging.info(count, " records in students table")

               std_describe_query = """Describe {tn} """.format(tn=table_name)
               cursor.execute(std_select_query)
               desc = cursor.description'''

        # (ID, Name, Age, Grade, IsFunClub, Address, EmergencyContact, ParentContact, Hobbies)


