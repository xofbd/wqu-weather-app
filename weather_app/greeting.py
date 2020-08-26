import requests


def greet(ip_address):
    location_data = get_location(ip_address)
    temp_C = get_temperature(location_data['latitude'],
                             location_data['longitude'])
    temp_F = convert_to_fahr(temp_C)

    return f"It's {temp_F :g} F in {location_data['city']}, {location_data['country']} right now."


def get_location(ip_address):
    """Return city, country, latitude, and longitude for a given IP address."""
    response = requests.get(f'https://ipapi.co/{ip_address}/json',
                            headers={'User-Agent': 'wqu_weather_app'})
    data = response.json()
    keys = ('city', 'country', 'latitude', 'longitude')

    return {key: data[key] for key in keys}


def get_temperature(lat, lon):
    url_base = 'https://api.met.no/weatherapi/locationforecast/2.0/compact'

    response = requests.get(url_base, params={'lat': lat, 'lon': lon})
    data = response.json()

    return data['properties']['timeseries'][0]['data']['instant']['details']['air_temperature']


def convert_to_fahr(temp_C):
    """Convert degrees to Celsius to Fahrenheit."""
    return 9 / 5 * temp_C + 32


def get_local_IP_address():
    return requests.get('https://api.ipify.org').text


if __name__ == '__main__':
    import sys

    print(greet(sys.argv[1]))
