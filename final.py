import sqlite3
from geopy.distance import geodesic

conn = sqlite3.connect('city_coordinates.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS cities (
    name TEXT PRIMARY KEY, latitude REAL, longitude REAL)''')
conn.commit()

def get_city_coordinates(city_name):
    cursor.execute('SELECT latitude, longitude FROM cities WHERE name = ?', (city_name,))
    result = cursor.fetchone()
    return result

def save_city_coordinates(city_name, latitude, longitude):
    cursor.execute('INSERT OR REPLACE INTO cities (name, latitude, longitude) VALUES (?, ?, ?)',(city_name, latitude, longitude))
    conn.commit()

def main():
    while True:
        city1 = input('Enter the first city: ')
        city2 = input('Enter the second city: ')

        coordinates1 = get_city_coordinates(city1)
        coordinates2 = get_city_coordinates(city2)

        if coordinates1 is None:
            latitude = float(input(f'Enter the latitude of {city1}: '))
            longitude = float(input(f'Enter the longitude of {city1}: '))
            save_city_coordinates(city1, latitude, longitude)

        if coordinates2 is None:
            latitude = float(input(f'Enter the latitude of {city2}: '))
            longitude = float(input(f'Enter the longitude of {city2}: '))
            save_city_coordinates(city2, latitude, longitude)

        coordinates1 = get_city_coordinates(city1)
        coordinates2 = get_city_coordinates(city2)

        if coordinates1 and coordinates2:
            distance = round(geodesic(coordinates1, coordinates2).kilometers, 2)
            print(f'The distance between {city1} and {city2} is {distance} kilometers.')

        choice = input('Calculate distance for another pair of cities? (y/n): ')
        if choice.lower() != 'y':
            conn.close()
            break

if __name__ == "__main__":
    main()
