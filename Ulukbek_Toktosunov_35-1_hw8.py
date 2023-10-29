import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS countries (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL)""")

cursor.execute("INSERT INTO countries (title) VALUES ('USA')")
cursor.execute("INSERT INTO countries (title) VALUES ('Canada')")
cursor.execute("INSERT INTO countries (title) VALUES ('France')")

cursor.execute("""CREATE TABLE IF NOT EXISTS cities (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL,
                  area REAL DEFAULT 0,
                  country_id INTEGER,
                  FOREIGN KEY (country_id) REFERENCES countries(id))""")

cursor.execute("INSERT INTO cities (title, country_id) VALUES ('New York', 1)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Toronto', 2)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Paris', 3)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Los Angeles', 1)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Vancouver', 2)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Marseille', 3)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Chicago', 1)")

cursor.execute("""CREATE TABLE IF NOT EXISTS employees (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  first_name TEXT NOT NULL,
                  last_name TEXT NOT NULL,
                  city_id INTEGER,
                  FOREIGN KEY (city_id) REFERENCES cities(id))""")

cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('John', 'Doe', 1)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Jane', 'Smith', 2)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Robert', 'Johnson', 3)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Sarah', 'Williams', 4)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Michael', 'Brown', 5)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Emma', 'Taylor', 6)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('David', 'Lee', 7)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Ronaldo','Cristiano',5)")


conn.commit()
conn.close()

def display_employees_by_city():
    conn = sqlite3.connect('company.db')
    cursor = conn.cursor()

    while True:
        print("You can display a list of employees by selecting a city ID from the list of cities below. Enter 0 to exit:")
        cursor.execute("SELECT id, title FROM cities")
        cities = cursor.fetchall()

        for city in cities:
            print(f"{city[0]}. {city[1]}")

        city_id = int(input("Enter the city ID: "))

        if city_id == 0:
            break

        cursor.execute("SELECT first_name, last_name FROM employees WHERE city_id = ?", (city_id,))
        employees = cursor.fetchall()

        if not employees:
            print("There are no employees in the selected city.")
        else:
            print(f"Employees in the selected city:")
            for employee in employees:
                print(f"{employee[0]} {employee[1]}")

    conn.close()

if __name__ == "__main__":
    display_employees_by_city()