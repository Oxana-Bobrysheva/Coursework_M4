import unittest
from unittest.mock import patch
from src.API_interaction import HH

class TestHHClass(unittest.TestCase):

    def test_get_vacancies(self):
        hh_instance = HH()
        keyword = "python"
        with patch('requests.get') as mocked_get:
            mocked_get.return_value.status_code = 200
            mocked_get.return_value.json.return_value = {"items": ["Vacancy1", "Vacancy2"]}
            vacancies = hh_instance.get_vacancies(keyword)
            self.assertEqual(len(vacancies), 40)


if __name__ == '__main__':
    unittest.main()