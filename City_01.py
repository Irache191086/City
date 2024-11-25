from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    geocoder = OpenCageGeocode(key)
    query = city
    results = geocoder.geocode(query)
    if results:
        return results[0]['geometry']['lat'], results[0]['geometry']['lng']
    else:
        return "Город не найден"

# Пример использования
key = '628122f6b49b4fe798d95adad797a116'
city = 'Москва'
coordinates = get_coordinates(city, key)
print(f"Координаты города {city}: {coordinates}")

