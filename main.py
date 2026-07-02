import psycopg2
import os

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "assignment4",
    "user": "postgres",
    "password": "Maria1209"
}


def import_data():
    conn = None
    cursor = None


    tasks = [
        ("Hotel", "Hotel.csv", None),
        ("Room", "Room.csv", None),
        ("Details", "Details.csv", None),
        ("Guests", "Guests.csv", None),
        ("Services", "Services.csv", None),
        ("Booking", "Booking.csv", "IDBooking, IDRoom, IDGuest, arrival_date, departure_date, total_sum, status"),
        ("Booking_Services", "Booking_Services.csv", None),
        ("Review", "Review.csv", None)
    ]

    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        print("Сonect success!")

        for table, file, cols in tasks:
            if os.path.exists(file):
                with open(file, 'r', encoding='utf-8') as f:

                    cursor.execute(f"TRUNCATE hms.{table} RESTART IDENTITY CASCADE;")

                    col_str = f"({cols})" if cols else ""
                    query = f"COPY hms.{table} {col_str} FROM STDIN WITH (FORMAT CSV, HEADER TRUE)"
                    cursor.copy_expert(query, f)
                    conn.commit()
                    print(f"Таблицю {table} очищено та імпортовано")
            else:
                print(f"Error: file {file} not found")

    except Exception as e:
        print(f"Критична помилка: {e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
        print("Finish!!")


if __name__ == "__main__":
    import_data()