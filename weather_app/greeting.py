from io import StringIO
import folium
import pandas as pd
import plotly.express as px
import requests
import requests_cache
import wikipedia

FLUSH_PERIOD = 10 * 60  # 10 minutes in seconds
requests_cache.install_cache(expire_after=FLUSH_PERIOD)


def greet(ip_address):
    """Create a message with weather and location-related information.

    Parameters
    ----------
    ip_address: str
        A single IPv4/IPv6 address, or a domain name.

    Returns
    -------
    A dictionary of the weather and location information.
    """
    location = get_location(ip_address)
    temperature_data = get_temperature(location['lat'], location['lon'],
                                       location['timezone'])
    temp_C = temperature_data.iloc[0]  # temperature in deg C
    temp_F = convert_to_fahr(temp_C)

    weather_info = {
        'graphs': plot_forecast(temperature_data),
        'map': draw_map(location['lat'], location['lon']),
        'headline': f"""It's {temp_C :.0f} &deg;C ({temp_F :.0f} &deg;F) in
                    {location['city']}, {location['country']}
                    right now.""",
        'summary': get_wikipedia_info(location['city'], location['country']),
        'ip_address': ip_address
    }
    return weather_info


def get_location(ip_address):
    """Get city, country, latitude, longitude and timezone information for a
     location given an IP address.

    Parameters
    ----------
    ip_address: str
        A single IPv4/IPv6 address, or a domain name.

    Returns
    -------
    A dictionary of location details.
    """
    response = requests.get(f'http://ip-api.com/json/{ip_address}',
                            headers={'User-Agent': 'wqu_weather_app'})
    loc_info = response.json()
    keys = ('city', 'country', 'lat', 'lon', 'timezone')
    return {key: loc_info[key] for key in keys}


def get_temperature(lat, lon, timezone):
    """Get temperature time series data for a given location.

    Parameters
    ----------
    lat, lon: int or float
        Latitude and longitude values, respectively.
    timezone: str
        Time zone information e.g. 'GMT'.

    Returns
    -------
    A timezone-aware pandas Series of temperature values.
    """
    base_url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact'

    response = requests.get(base_url, params={'lat': lat, 'lon': lon},
                            headers={'User-Agent': 'wqu_weather_app'})
    raw_data = response.json()['properties']['timeseries']

    # Create a Series with temperature data from the nested JSON raw_data
    time_info = [entry['time'] for entry in raw_data]
    temp_info = [entry['data']['instant']['details']['air_temperature']
                 for entry in raw_data]
    temp_data = pd.Series(temp_info, index=time_info)

    # Make the index timezone aware
    temp_data.index = pd.to_datetime(temp_data.index).tz_convert(timezone)
    return temp_data


def plot_forecast(data):
    """Get graphs of air temperature forecasts.

    Parameters
    ----------
    data: pd.Series
        Temperature values with a timezone-aware date-time index.

    Returns
    -------
    A line graph of the 24hr forecast, and a bar graph of the 10-day max & min
    temperature forecast, stored in text buffers.
    """
    temp24H = data[:24]
    fig = px.line(y=temp24H, x=temp24H.index.astype(str),
                  title="24 Hour Forecast")
    # Rename axes labels and disable zoom
    fig.update_xaxes(title_text='Time', fixedrange=True)
    fig.update_yaxes(title_text='Air temperature in deg C', fixedrange=True)
    fig.update_layout(paper_bgcolor='azure', plot_bgcolor='azure')
    # Write graph to text buffer
    temp24H_graph = StringIO()
    fig.write_html(temp24H_graph, include_plotlyjs='cdn', full_html=False)

    temp10D = data.resample('1D').agg(['max', 'min'])
    fig2 = px.bar(temp10D, color_discrete_sequence=['orangered', 'cyan'],
                  barmode='group', title="10 Day Forecast")
    # Rename axes labels and disable zoom
    fig2.update_xaxes(title_text='Day', fixedrange=True)
    fig2.update_yaxes(title_text='Air temperature in deg C', fixedrange=True)
    fig2.update_layout(paper_bgcolor='azure', plot_bgcolor='azure')
    # Write graph to text buffer
    temp10D_graph = StringIO()
    fig2.write_html(temp10D_graph, include_plotlyjs='cdn', full_html=False)
    return temp24H_graph, temp10D_graph


def get_wikipedia_info(*location):
    """Get brief details about a location from Wikipedia.

    Parameters
    ----------
    location: str
        Location name(s) to search for.

    Returns
    -------
    Summary text about the location.
    """
    # Search for articles about location(s), and select first result
    wiki_query = wikipedia.search(f"{location}")[0]

    return wikipedia.summary(wiki_query, sentences=5)


def draw_map(lat, lon):
    """Draw the map of a location given latitude and longitude.

    Parameters
    ----------
    lat, lon: int or float
        Latitude and longitude values, respectively.

    Returns
    -------
    A string with HTML code for a map.
    """
    return folium.Map(location=(lat, lon), zoom_start=14)._repr_html_()


def convert_to_fahr(temp_C):
    """Convert temperature from degrees Celsius to Fahrenheit."""
    return 9 / 5 * temp_C + 32


def get_local_IP_address():
    """
    Get the client's IP address via a GET request to an API service.

    Returns
    -------
    An IPv4 or IPv6 address.
    """
    return requests.get('https://api.ipify.org',
                        headers={'User-Agent': 'wqu_weather_app'}).text


if __name__ == '__main__':
    import sys

    print(greet(sys.argv[1]))
