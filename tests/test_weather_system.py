import unittest
from processor.data_processor import kelvin_to_celsius

class TestWeatherSystem(unittest.TestCase):
    def test_kelvin_to_celsius(self):
        self.assertEqual(kelvin_to_celsius(300), 26.85)
        self.assertEqual(kelvin_to_celsius(273.15), 0)

if __name__ == "__main__":
    unittest.main()
