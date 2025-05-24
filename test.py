import unittest
from unittest.mock import patch, MagicMock
import json
from hko_mcp import get_weather_info, get_earthquake_info, Gregorian_Lunar_Calendar_Coversion, rainfall_past_hour_from_station

class TestHKOMCP(unittest.TestCase):
    
    @patch('hko_mcp.requests.get')
    def test_get_weather_info(self, mock_get):
        # Setup mock response for different data types
        mock_response = MagicMock()
        mock_response.json.return_value = {"forecast": "Sunny"}
        mock_response.text = json.dumps({"forecast": "Sunny"})
        mock_get.return_value = mock_response
        
        # Test with different data types
        data_types = ["flw", "fnd", "rhrread", "warnsum", "warningInfo", "swt"]
        languages = ["en", "tc", "sc"]
        
        for data_type in data_types:
            for lang in languages:
                result = get_weather_info(data_type, lang)
                self.assertEqual(result, {"forecast": "Sunny"})
                mock_get.assert_called_with(
                    f"https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType={data_type}&lang={lang}"
                )
    
    @patch('hko_mcp.requests.get')
    def test_get_earthquake_info(self, mock_get):
        # Setup mock response
        mock_response = MagicMock()
        mock_response.json.return_value = {"earthquake": "detected"}
        mock_response.text = json.dumps({"earthquake": "detected"})
        mock_get.return_value = mock_response
        
        # Test with different data types
        data_types = ["qem", "feltearthquake"]
        languages = ["en", "tc", "sc"]
        
        for data_type in data_types:
            for lang in languages:
                result = get_earthquake_info(data_type, lang)
                self.assertEqual(result, {"earthquake": "detected"})
                mock_get.assert_called_with(
                    f"https://data.weather.gov.hk/weatherAPI/opendata/earthquake.php?dataType={data_type}&lang={lang}"
                )
    
    @patch('hko_mcp.requests.get')
    def test_gregorian_lunar_calendar_conversion(self, mock_get):
        # Setup mock response
        mock_response = MagicMock()
        mock_response.text = json.dumps({"LunarYear": 2023, "LunarDate": "8-16"})
        mock_get.return_value = mock_response
        
        # Test with a sample date
        date = "2023-10-01"
        result = Gregorian_Lunar_Calendar_Coversion(date)
        self.assertEqual(result, json.dumps({"LunarYear": 2023, "LunarDate": "8-16"}))
        mock_get.assert_called_with(
            f"https://data.weather.gov.hk/weatherAPI/opendata/lunardate.php??date={date}"
        )
    
    @patch('hko_mcp.requests.get')
    def test_rainfall_past_hour_from_station(self, mock_get):
        # Setup mock response
        mock_response = MagicMock()
        mock_response.json.return_value = {"rainfall": {"Central": 0.5}}
        mock_response.text = json.dumps({"rainfall": {"Central": 0.5}})
        mock_get.return_value = mock_response
        
        # Test with different languages
        languages = ["en", "tc", "sc"]
        
        for lang in languages:
            result = rainfall_past_hour_from_station(lang)
            self.assertEqual(result, {"rainfall": {"Central": 0.5}})
            mock_get.assert_called_with(
                f"https://data.weather.gov.hk/weatherAPI/opendata/hourlyRainfall.php?lang={lang}"
            )

    @patch('hko_mcp.requests.get')
    def test_error_handling(self, mock_get):
        # Setup mock response to raise an exception
        mock_get.side_effect = Exception("API Error")
        
        # Test error handling for each function
        with self.assertRaises(Exception):
            get_weather_info("flw", "en")
        
        with self.assertRaises(Exception):
            get_earthquake_info("qem", "en")
        
        with self.assertRaises(Exception):
            Gregorian_Lunar_Calendar_Coversion("2023-10-01")
        
        with self.assertRaises(Exception):
            rainfall_past_hour_from_station("en")

if __name__ == '__main__':
    unittest.main()