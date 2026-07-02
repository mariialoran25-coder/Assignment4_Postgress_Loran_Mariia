import uuid
import psycopg2
from psycopg2 import Error


HOST = 'localhost' # put your credentials here
USER = 'postgres' # put your credentials here
PASSWORD = '1' # put your credentials here
DATABASE = 'hms' # put your credentials here
PORT = '5432' # put your credentials here


def create_connection():
    """Create a PostgreSQL database connection."""
    try:
        connection = psycopg2.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            dbname=DATABASE,
        )
        print("Connection to PostgreSQL DB successful")
        return connection
    except Error as e:
        print(f"The error '{e}' occurred")
        return None


def execute_query(connection, query, data):
    """Execute a single query."""
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, data)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        connection.rollback()
        print(f"The error '{e}' occurred")


def insert_data():
    connection = create_connection()
    if connection is None:
        return

    hotel_query = """
    INSERT INTO hms.Hotel (Name, City) VALUES (%s, %s)
    """
    hotel_data = [
        ("Grand Palace", "Kyiv"),
        ("Hilton", "Kyiv"),
        ("NEMO", "Odesa"),
        ("Arkadia Beach Hotel", "Odesa"),
        ("Emily Resort", "Lviv"),
    ]
    for data in hotel_data:
        execute_query(connection, hotel_query, data)
    print("Successfully inserted data in hms.Hotel ")


    rooms_query = """
    INSERT INTO hms.Room (IdHotel, room_number, type, cost, status)
    VALUES (%s, %s, %s, %s, %s)
    """
    rooms_data = [
        (1, 101, "Luxe", 2000.00, "Free"),
        (2, 102, "Standard", 100.00, "free"),
        (3, 103, "Luxe", 250.00, "free"),
        (4, 104, "Superior", 150.00, "free"),
        (5, 105, "Deluxe", 555.00, "occupid"),
    ]
    for data in rooms_data:
        execute_query(connection, rooms_query, data)



    guests_query = """
    INSERT INTO hms.Guests (first_name, last_name, email, phone)
    VALUES (%s, %s, %s, %s)
    ON CONFLICT (email) DO NOTHING
    """
    guests_data = [
        ("John", "Doe", "john.doe@example.com", "1-234-567-890"),
        ("Jane", "Smith", "jane.smith@example.com", "098-765-4321"),
        ("Mariia", "Loran", "mariia.loran@example.com", "380-589-458-923"),
        ('James', 'Smith', 'smith.james@example.org', '380-010-998 -888'),
        ('Mary', 'Johnson', 'mjohnson@example.net', "380-010-998 -888"),
        ('Robert', 'Williams', 'robert.w@example.com', "380-333-444-555"),
    ]
    for data in guests_data:
        execute_query(connection, guests_query, data)
    print("Successfully inserted data in hms.Guests ")


    booking_query = """
    INSERT INTO hms.Booking (IDBooking,IDRoom, IDGuest, arrival_date, departure_date, total_sum)
    VALUES (%s, %s, %s, %s, %s, %s)
    ON CONFLICT (id) DO NOTHING
    """
    courses_data = [
        (str(uuid.uuid4()), "CS101", "Introduction to Computer Science", "Basic concepts of computer science", 30, 15),
        (str(uuid.uuid4()), "MATH201", "Advanced Mathematics", "In-depth study of advanced mathematical concepts", 25, 10),
    ]
    for data in courses_data:
        execute_query(connection, courses_query, data)

    review_query = """
    INSERT INTO hms.Review (id, IDGuest, IDHotel, Description, Score)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (id) DO NOTHING
    """

    instructors_data = [
        (str(uuid.uuid4()), "Alice", "Johnson", "alice.johnson@example.com", "1122334455", True),
        (str(uuid.uuid4()), "Bob", "Williams", "bob.williams@example.com", "5544332211", True),
    ]
    for data in instructors_data:
        execute_query(connection, instructors_query, data)

    services_query = """
    INSERT INTO  hms.Services (id, name, cost)
    VALUES (%s, %s, %s)
    ON CONFLICT (id) DO NOTHING
    """
    lessons_schedule_data = [(1, "08:00:00", "09:00:00"), (2, "09:00:00", "10:00:00")]
    for data in lessons_schedule_data:
        execute_query(connection, lessons_schedule_query, data)

    instructors_courses_query = """
    INSERT INTO instructors_courses (instructor_id, course_id)
    VALUES (%s, %s)
    ON CONFLICT (instructor_id, course_id) DO NOTHING
    """
    instructors_courses_data = [(instructors_data[0][0], courses_data[0][0]), (instructors_data[1][0], courses_data[1][0])]
    for data in instructors_courses_data:
        execute_query(connection, instructors_courses_query, data)

    booking_services_query = """
    INSERT INTO hms.Booking_Services (id, IDService)
    VALUES (%s, %s)
    ON CONFLICT (id) DO NOTHING
    """
    students_course_groups_data = [(str(uuid.uuid4()), courses_data[0][0]), (str(uuid.uuid4()), courses_data[1][0])]
    for data in students_course_groups_data:
        execute_query(connection, students_course_groups_query, data)






    #
    # students_course_group_students_query = """
    # INSERT INTO students_course_group_students (student_id, group_id)
    # VALUES (%s, %s)
    # ON CONFLICT (student_id, group_id) DO NOTHING
    # """
    # students_course_group_students_data = [
    #     (students_data[0][0], students_course_groups_data[0][0]),
    #     (students_data[1][0], students_course_groups_data[1][0]),
    # ]
    # for data in students_course_group_students_data:
    #     execute_query(connection, students_course_group_students_query, data)
    #
    # schedule_query = """
    # INSERT INTO schedule (id, course_id, instructor_id, students_course_group_id, week_day, lesson_schedule_id, room_id)
    # VALUES (%s, %s, %s, %s, %s, %s, %s)
    # ON CONFLICT (id) DO NOTHING
    # """
    # schedule_data = [
    #     (1, courses_data[0][0], instructors_data[0][0], students_course_groups_data[0][0], "Monday", 1, rooms_data[0][0]),
    #     (2, courses_data[1][0], instructors_data[1][0], students_course_groups_data[1][0], "Tuesday", 2, rooms_data[1][0]),
    # ]
    # for data in schedule_data:
    #     execute_query(connection, schedule_query, data)

    connection.close()


if __name__ == "__main__":
    insert_data()
