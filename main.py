import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("hko mcp")

@mcp.tool()
def get_weather_info(dataType: str, lang: str = "en"):
    """
    Get weather information from the Hong Kong Observatory.

    Args:
        dataType: The type of weather information to get.
            - flw: Local Weather Forecast
            - fnd: 9-day Weather Forecast
            - rhrread: Current Weather Report
            - warnsum: Weather Warning Summary
            - warningInfo: Weather Warning Information
            - swt: Special Weather Tips
        lang: The language of the weather information.
            - en: English
            - tc: Traditional Chinese
            - sc: Simplified Chinese
    Returns:
        The weather information by JSON format.
    """

    # http get request
    # url = f"https://www.hko.gov.hk/wxinfo/fnd/fnd_{lang}.htm"
    url = f"https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType={dataType}&lang={lang}"
    response = requests.get(url)
    response.raise_for_status()
    html = response.text
    # print(html) # for check the response only

    return response.json()


@mcp.tool()
def get_earthquake_info(dataType: str, lang: str = "en"):
    """
    Get earthquake information from the Hong Kong Observatory.

    Args:
        dataType: The type of earthquake information to get.
            - qem: Quick Earthquake Messages
            - feltearthquake: Locally Felt Earth Tremor Report
        lang: The language of the earthquake information.
            - en: English
            - tc: Traditional Chinese
            - sc: Simplified Chinese
    Returns:
        The earthquake information by JSON format.
    """

    url = f"https://data.weather.gov.hk/weatherAPI/opendata/earthquake.php?dataType={dataType}&lang={lang}"
    response = requests.get(url)
    response.raise_for_status()
    html = response.text
    # print(html) # for check the response only

    return response.json()


@mcp.tool()
def Gregorian_Lunar_Calendar_Coversion(date: str):
    """
    Convert Gregorian date to Lunar date.

    Args:
        date: The Gregorian date to convert.
            - Format: YYYY-MM-DD
    Returns:
        The Lunar date in by JSON format.
    Args:
        LunarYear: The Lunar year.
        LunarDate: The Lunar date.
    """

    url = f"https://data.weather.gov.hk/weatherAPI/opendata/lunardate.php??date={date}"
    response = requests.get(url)
    response.raise_for_status()
    html = response.text
    # print(html) # for check the response only

    return html


@mcp.tool()
def rainfall_past_hour_from_station(lang: str = "en"):
    """
    Get rainfall past hour from the Hong Kong Observatory.

    Args:
        lang: The language of the rainfall information.
            - en: English
            - tc: Traditional Chinese
            - sc: Simplified Chinese
    Returns:
        The rainfall past hour information by JSON format.
    """

    url = f"https://data.weather.gov.hk/weatherAPI/opendata/hourlyRainfall.php?lang={lang}"
    response = requests.get(url)
    response.raise_for_status()
    html = response.text
    # print(html) # for check the response only

    return response.json()


if __name__ == '__main__':
    mcp.run(transport='stdio') 