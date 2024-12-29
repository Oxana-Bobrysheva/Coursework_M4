import unittest
from unittest.mock import patch, mock_open
from src.files import JsonFile, Vacancy
import src.files

class TestJsonFileClass(unittest.TestCase):

    def test_add_vacancy(self):
        json_file = JsonFile()
        vacancy = Vacancy(id="1", name="Software Engineer", link="example.com", salary="100K",
                          employer="ABC Company", requirement="Python experience", schedule="Full-time")

        with patch('builtins.open', mock_open()) as mocked_open:
            json_file.add_vacancy(vacancy)
            mocked_open.assert_called_with('date/vacancies.json', 'w', encoding='UTF-8')

    @patch('builtins.open', new_callable=mock_open)
    def test_delete_vacancy_success(self, mock_open):
        # Setup
        vacancy_to_delete = Vacancy(id="1", name="Software Engineer", link="example.com", salary="100K",
                          employer="ABC Company", requirement="Python experience", schedule="Full-time")
        json_data = {"items": [{"id": "1", "name": "Software Engineer"}]}
        file_path = "date/vacancies.json"

        with patch('src.files.os.path.exists', return_value=True), \
                patch('src.files.JsonFile.get_vacancies_from_file', return_value=json_data):
            json_file = JsonFile()

            # Call the method
            json_file.delete_vacancy(vacancy_to_delete)

            # Assertions
            mock_open.assert_called_with(file_path, "w", encoding="UTF-8")


if __name__ == '__main__':
    unittest.main()