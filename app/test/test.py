from unittest import TestCase, mock
import unittest
import os
from app.flask_server import app


class BaseTestClass(unittest.TestCase):

    def setUp(self) -> None:
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    @mock.patch.dict(os.environ, {"GEO_API_KEY": "1508a9a4840a5574c822d70ca2132032"})
    def test_weather_correct(self):
        response = self.app.get('/weather?city=Bogota&country=CO', follow_redirects=True)
        self.assertEqual(str, type(response.json['location_name']))
        self.assertEqual(10, len(response.json.keys()))
        self.assertEqual(response.status_code, 200)

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
