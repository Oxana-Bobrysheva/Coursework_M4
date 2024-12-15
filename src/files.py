import json
import os
from abc import ABC, abstractmethod

from src.vacancies import Vacancy


class FileWork(ABC):
    """Abstract class to work with files."""

    __file_path: str

    @abstractmethod
    def get_vacancies_from_file(self):
        """Abstract method to get data from file."""
        pass

    @abstractmethod
    def add_vacancy(self, vacancy):
        """Abstract method to add data to the file."""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        """Abstract method to delete data from the file."""
        pass


class JsonFile(FileWork):
    """Class to work with json files that contain info about vacancies."""

    def __init__(self):
        self.__file_path = "date/vacancies.json"

    def get_vacancies_from_file(self):
        """Getting list of vacations from the file JSON."""
        try:
            with open(self.__file_path, "r", encoding="UTF-8") as file:
                vacancy_list = json.load(file)
                return vacancy_list
        except FileNotFoundError:
            print("Файл не найден.")

    def add_vacancy(self, vacancy):
        """Adding data to the object of class Vacancy into file in JSON."""
        # Checking the class status
        if isinstance(vacancy, Vacancy):
            data_to_save: dict = dict()
            data_to_save["items"] = list()
            vacancy_to_add = vacancy.object_to_dict()

            is_duplicate = False
            if os.path.exists(self.__file_path):
                # Try to download data from the file
                data_to_save = self.get_vacancies_from_file()

                # searching the doubled data
                for item in data_to_save["items"]:
                    if item["id"] == vacancy_to_add["id"]:
                        print("Вакансия уже есть в файле.")
                        is_duplicate = True
                        break
                # Rewriting data to the file
                if is_duplicate is False:
                    data_to_save["items"].append(vacancy_to_add)
                    with open(self.__file_path, "w", encoding="UTF-8") as file:
                        json.dump(data_to_save, file, indent=4, ensure_ascii=False)
                        print("Вакансия успешно добавлена.")
            else:
                # Creating file if the one wasn't found
                with open(self.__file_path, "w", encoding="UTF-8") as file:
                    data_to_save["items"].append(vacancy_to_add)
                    json.dump(data_to_save, file, indent=4, ensure_ascii=False)
                    print("Создан файл и успешно добавлена вакансия.")

        else:
            print("Переданный объект не является объектом класса Vacancy.")

    def delete_vacancy(self, vacancy) -> None:
        """Deleting data from the file"""
        # Checking class status
        if isinstance(vacancy, Vacancy):
            data_to_save: dict = dict()
            data_to_save["items"] = list()
            vacancy_to_delete = vacancy.object_to_dict()
            is_found = False
            if os.path.exists(self.__file_path):
                data_to_save = self.get_vacancies_from_file()
                for item in data_to_save["items"]:
                    if item["id"] == vacancy_to_delete["id"]:
                        data_to_save["items"].remove(item)
                        is_found = True

                if is_found:
                    with open(self.__file_path, "w", encoding="UTF-8") as file:
                        json.dump(data_to_save, file, indent=4, ensure_ascii=False)
                        print("Вакансия успешно удалена.")
                else:
                    print("Вакансия не найдена в файле.")
            else:
                print("Файл не найден.")
        else:
            print("Переданный объект не является объектом класса Vacancy.")
