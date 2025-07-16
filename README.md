# Hong Kong Observatory MCP Server

A Model Context Protocol (MCP) server that provides weather information of Hong Kong Observatory. 

## Features

- Weather information (forecasts, warnings, current conditions)
- Earthquake information
- Gregorian to Lunar calendar conversion
- Rainfall data from monitoring stations

## Data Source
This project utilizes the official HKO Open Data API:
- Weather Information base URL: https://data.weather.gov.hk/weatherAPI/opendata/weather.php
- Earthquake Information base URL: https://data.weather.gov.hk/weatherAPI/opendata/earthquake.php
- Gregorian-Lunar Calendar Conversion base URL: https://data.weather.gov.hk/weatherAPI/opendata/lunardate.php
- Rainfall in the Past Hour from Automatic Weather Station base URL: https://data.weather.gov.hk/weatherAPI/opendata/hourlyRainfall.php
- [HKO Open Data API Documentation](https://www.hko.gov.hk/en/weatherAPI/doc/files/HKO_Open_Data_API_Documentation.pdf)

## Prerequisites
- Python 3.13 or higher
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

## Installation
1. Install Python

2. Clone this repository:
```bash 
git clone https://github.com/pongiotdevelop/hko_mcp.git
```

## Usage
1. Add the below to your MCP configuration:
```json
{
    "mcpServers": {
        "HKO_MCP": {
            "command": "uv",
            "args": [
                "--directory",
                "<directory of the project>"
                "run",
                "main.py"
            ]
        }    
    }
}
```

2. The server provides several tools that can be used by Language Models to query HKO information:
- `get_weather_info(dataType: str, lang: str = "en")`: Get weather information from the Hong Kong Observatory.
- `get_earthquake_info(dataType: str, lang: str = "en")`: Get earthquake information from the Hong Kong Observatory.
- `Gregorian_Lunar_Calendar_Conversion(date: str)`: Convert Gregorian date to Lunar date.
- `rainfall_past_hour_from_station(lang: str = "en")`: Get rainfall past hour from the Hong Kong Observatory.

## Testing 
Run the test.py for testing the API functions of MCP server:
```bash
python test.py
```

## Dependencies
- `requests`: For HTTP requests
- `fastmcp`: For MCP server implementation

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- Hong Kong Observatory for providing the open data API
- The MCP protocol developers

