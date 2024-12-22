import unittest
from src.utils import filter_vacancies, get_vacancies_by_salary
import re

class Vacancy_test:
    def __init__(self, name, employer, requirement, salary_from, salary_to):
        self.name = name
        self.employer = employer
        self.requirement = requirement
        self.salary_from = salary_from
        self.salary_to = salary_to

    def object_to_dict(self):
        return {
            "name": self.name,
            "employer": self.employer,
            "requirement": self.requirement,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to
        }


class TestFilterVacancies(unittest.TestCase):
    def setUp(self):
        # Define test vacancies list and filter words
        self.vacancy1 = Vacancy_test("Software Developer", "ABC Inc.", "Python knowledge required", 2000, 200000)
        self.vacancy2 = Vacancy_test("Data Scientist", "XYZ Corp.", "Machine learning skills needed", 1000, 50000)
        self.vacancies_list = [self.vacancy1, self.vacancy2]
        self.filter_words = ["python", "developer"]

    def test_filter_vacancies(self):
        filtered_vacancies = filter_vacancies(self.vacancies_list, self.filter_words)

        # Add specific assertions based on the expected behavior
        self.assertEqual(len(filtered_vacancies), 1)  # Check if only one vacancy is filtered
        self.assertIn(self.vacancy1, filtered_vacancies)  # Check if the correct vacancy is present in the filtered list


class TestGetVacanciesBySalary(unittest.TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.salary_range = "100-200000"
        self.salary_from = 1000
        self.salary_to = 10000000

    def setUp(self):
        # Define test vacancy list and salary range
        self.vacancy1 = Vacancy_test("Software Engineer", 50000, 80000, 2000, 2000000)
        self.vacancy2 = Vacancy_test("Data Analyst", 60000, 70000, 1000, 10000)
        self.vacancy3 = Vacancy_test("Product Manager", 90000, None, 10000, 250000)
        self.vacancy_list = [self.vacancy1, self.vacancy2, self.vacancy3]


    def test_get_vacancies_by_salary(self):
        filtered_vacancies = get_vacancies_by_salary(self.vacancy_list, self.salary_range)

        # Add specific assertions based on the expected behavior
        self.assertEqual(len(filtered_vacancies), 3)  # Check if correct number of vacancies are filtered
        self.assertIn(self.vacancy1, filtered_vacancies)  # Check if a vacancy with salary range is included
        self.assertIn(self.vacancy2, filtered_vacancies)  # Check if another vacancy with salary range is included


if __name__ == '__main__':
    unittest.main()