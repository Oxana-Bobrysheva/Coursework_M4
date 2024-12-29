import re


class Vacancy:
    """Class to create vacancies"""

    def __init__(
        self,
        id: str,
        name: str,
        link: str,
        salary: str | dict,
        employer: str,
        requirement: str,
        schedule: str,
    ) -> None:
        """Initialization of objects in Vacancy class."""
        salary_from = 0
        salary_to = 0
        if salary is None:
            salary_from, salary_to = 0, 0
        elif type(salary) is dict:
            salary_from, salary_to = Vacancy.__get_salary_data_from_dict(salary)
        elif type(salary) is str:
            salary_from, salary_to = Vacancy.__get_salary_data_from_str(salary)
        self.id: str = id
        self.name: str = name
        self.link: str = link
        self.salary_from: int = int(salary_from)
        self.salary_to: int = int(salary_to)
        self.employer: str = employer
        self.requirement: str = requirement
        self.schedule: str = schedule

    def __eq__(self, other) -> bool:
        """Сравнение вакансий по зарплате: вакансия 1 = вакансия 2."""
        if isinstance(other, Vacancy):
            if self.salary_to > 0 and other.salary_to > 0:
                return self.salary_to == other.salary_to
            elif self.salary_to == 0 and other.salary_from > 0:
                return self.salary_from == other.salary_from
            elif self.salary_to > 0 and other.salary_from == 0:
                return self.salary_from == other.salary_from
            else:
                return True
        else:
            print("Объект сравнения не является объектом класса Vacancy.")
            return False

    def __gt__(self, other) -> bool:
        """Сравнение вакансий по зарплате: вакансия 1 > вакансии 2."""
        if isinstance(other, Vacancy):
            if self.salary_to > 0 and other.salary_to > 0:
                return self.salary_to > other.salary_to
            elif self.salary_to == 0 and other.salary_from > 0:
                return self.salary_from > other.salary_from
            elif self.salary_to > 0 and other.salary_from == 0:
                return self.salary_from > other.salary_from
            else:
                return False
        else:
            print("Объект сравнения не является объектом класса Vacancy.")
            return False

    def __ge__(self, other) -> bool:
        """Сравнение вакансий по зарплате: вакансия 1 >= вакансии 2."""
        if isinstance(other, Vacancy):
            if self.salary_to > 0 and other.salary_to > 0:
                return self.salary_to >= other.salary_to
            elif self.salary_to == 0 and other.salary_from > 0:
                return self.salary_from >= other.salary_from
            elif self.salary_to > 0 and other.salary_from == 0:
                return self.salary_from >= other.salary_from
            else:
                return False
        else:
            print("Объект сравнения не является объектом класса Vacancy.")
            return False

    def __lt__(self, other) -> bool:
        """Сравнение вакансий по зарплате: вакансия 1 < вакансии 2."""
        if isinstance(other, Vacancy):
            if self.salary_to > 0 and other.salary_to > 0:
                return self.salary_to < other.salary_to
            elif self.salary_to == 0 and other.salary_from > 0:
                return self.salary_from < other.salary_from
            elif self.salary_to > 0 and other.salary_from == 0:
                return self.salary_from < other.salary_from
            else:
                return False
        else:
            print("Объект сравнения не является объектом класса Vacancy.")
            return False

    def __le__(self, other) -> bool:
        """Сравнение вакансий по зарплате: вакансия 1 <= вакансии 2."""
        if isinstance(other, Vacancy):
            if self.salary_to > 0 and other.salary_to > 0:
                return self.salary_to <= other.salary_to
            elif self.salary_to == 0 and other.salary_from > 0:
                return self.salary_from <= other.salary_from
            elif self.salary_to > 0 and other.salary_from == 0:
                return self.salary_from <= other.salary_from
            else:
                return False
        else:
            print("Объект сравнения не является объектом класса Vacancy.")
            return False

    def __hash__(self):
        """Метод настройки хеширования объектов класса Vacancy."""
        return hash((self.id, self.name))

    @classmethod
    def cast_to_object_list(cls, data: list) -> list:
        """Класс-метод для создания списка объектов вакансий из
        списка словарей с данными."""

        obj_list = list()

        for item in data:
            # Инициализация объектов класса и добавление их в список объектов
            new_vacancy = cls(
                item["id"],
                item["name"],
                item["alternate_url"],
                item["salary"],
                item["employer"]["name"],
                item["snippet"]["requirement"],
                item["schedule"]["name"],
            )
            obj_list.append(new_vacancy)
        return obj_list

    def object_to_dict(self) -> dict:
        """Метод для преобразования объекта класса в словарь значений."""
        vacancy_dict: dict = dict()
        vacancy_dict["id"] = self.id
        vacancy_dict["name"] = self.name
        vacancy_dict["link"] = self.link
        vacancy_dict["salary_from"] = self.salary_from
        vacancy_dict["salary_to"] = self.salary_to
        vacancy_dict["employer"] = self.employer
        vacancy_dict["requirement"] = self.requirement
        vacancy_dict["schedule"] = self.schedule
        return vacancy_dict

    @staticmethod
    def __get_salary_data_from_dict(salary_data: dict) -> tuple:
        """Определение значений по зарплате из словаря: от, до и диапазон."""
        salary_from = 0
        salary_to = 0

        if salary_data["from"] and salary_data["to"]:
            salary_from = salary_data["from"]
            salary_to = salary_data["to"]

        elif salary_data["from"]:
            salary_from = salary_data["from"]

        elif salary_data["to"]:
            salary_to = salary_data["to"]

        return salary_from, salary_to

    @staticmethod
    def __get_salary_data_from_str(salary_data: str) -> tuple:
        """Определение значений по зарплате из строки: от, до и диапазон."""
        salary_from = 0
        salary_to = 0
        salary_data = salary_data.replace(" ", "")
        if "-" in salary_data:
            salary_from, salary_to = re.findall(r"\d+", salary_data, flags=0)
        elif "До".lower() in salary_data.lower():
            salary_to = re.findall(r"\d+", salary_data, flags=0)[0]
        elif "От".lower() in salary_data.lower():
            salary_from = re.findall(r"\d+", salary_data, flags=0)[0]
        return int(salary_from), int(salary_to)
