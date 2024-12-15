import re


def filter_vacancies(vacancies_list: list, filter_words: list) -> list:
    """Filtering function for list of vacancies by keyword."""
    filtered_vacancies_set = set()
    for vacancy in vacancies_list:
        for word in filter_words:
            vacancy_dict = vacancy.object_to_dict()
            if (
                word.lower() in vacancy_dict["name"].lower()
                or word.lower() in vacancy_dict["employer"].lower()
            ):
                filtered_vacancies_set.add(vacancy)
            elif (
                vacancy.requirement
                and word.lower() in vacancy_dict["requirement"].lower()
            ):
                filtered_vacancies_set.add(vacancy)
    filtered_vacancies = list(filtered_vacancies_set)
    return filtered_vacancies


def get_vacancies_by_salary(vacancy_list: list, salary_range: str) -> list:
    """Filtering function for list of vacancies by salary."""

    filtered_by_salary = list()
    salary_range = salary_range.replace(" ", "")
    salary_from, salary_to = re.findall(r"\d+", salary_range, flags=0)

    for vacancy in vacancy_list:
        # Adding vacancies
        if vacancy.salary_from and vacancy.salary_to:
            if int(salary_from) <= vacancy.salary_from <= int(salary_to) or int(
                salary_from
            ) <= vacancy.salary_to <= int(salary_to):
                filtered_by_salary.append(vacancy)
        elif vacancy.salary_to and int(salary_from) <= vacancy.salary_to:
            filtered_by_salary.append(vacancy)
        elif vacancy.salary_from and vacancy.salary_from <= int(salary_to):
            filtered_by_salary.append(vacancy)

    return filtered_by_salary


def sort_vacancies(vacancy_list: list) -> list:
    """Sorting function of vacancies by salary."""
    sorted_list = sorted(
        vacancy_list,
        key=lambda x: x.salary_to if x.salary_to else x.salary_from,
        reverse=True,
    )
    return sorted_list


def get_top_vacancies(vacancy_list: list, top_n: int) -> list:
    """Getting the certain top vacancies."""
    return vacancy_list[:top_n]


def print_vacancies(vacancy_list: list) -> None:
    """Printing vacancies into console."""
    if len(vacancy_list) != 0:
        for vacancy in vacancy_list:
            print(
                f"""Вакансия: {vacancy.name},
                зарплата: {vacancy.salary_from} - {vacancy.salary_to},
                работодатель: {vacancy.employer},
                график работы: {vacancy.schedule}."""
            )
    else:
        print("Список вакансий пуст.")
