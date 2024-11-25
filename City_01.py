from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    """ Получает координаты города, используя библиотеку OpenCage. """
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city,language="ru")

        if results:
            # Возвращает первый результат
            return results[0]['geometry']['lat'], results[0]['geometry']['lng']
        else:
            return "Город не найден"
    except Exception as e:
        return f"Общая ошибка: {e}"


# Пример использования
key = '628122f6b49b4fe798d95adad797a116'
city = 'London'
coordinates = get_coordinates(city, key)
print(f"Координаты города {city}: {coordinates}")

