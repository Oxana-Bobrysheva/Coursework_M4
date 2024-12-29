from src.vacancies import Vacancy
import unittest


class TestVacancyClass(unittest.TestCase):

    def test_init_with_dict_salary(self):
        # Test initialization with salary as a dictionary
        vacancy = Vacancy("id1", "Job Title", "joblink.com", {"from": 30000, "to": 50000}, "Company", "Requirements",
                          "Full-time")
        self.assertEqual(vacancy.salary_from, 30000)
        self.assertEqual(vacancy.salary_to, 50000)

    def test_comparison_methods(self):
        # Test comparison methods
        vacancy1 = Vacancy("id1", "Job 1", "link1.com", {"from": 30000, "to": 50000}, "Company 1", "Req 1", "Full-time")
        vacancy2 = Vacancy("id2", "Job 2", "link2.com", {"from": 25000, "to": 40000}, "Company 2", "Req 2", "Part-time")

        self.assertFalse(vacancy1 == vacancy2)  # Check equality
        self.assertTrue(vacancy1 >= vacancy2)  # Check greater than or equal
        self.assertFalse(vacancy1 < vacancy2)  # Check less than



if __name__ == '__main__':
    unittest.main()