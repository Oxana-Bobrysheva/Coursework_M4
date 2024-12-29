Получение вакансий
Просмотр вакансии
Поиск по вакансиям
Поиск по вакансиям, похожим на вакансию
Короткое представление вакансии
Смотрите также:


Вакансии для работодателя
Публикация вакансий
Редактирование вакансий
Продление вакансий
Удаление вакансий

Просмотр вакансии
!! Данный метод доступен в OpenAPI


Поиск по вакансиям
!! Данный метод доступен в OpenAPI


Поиск по вакансиям, похожим на вакансию
Запрос
!! Данный метод доступен в OpenAPI


Короткое представление вакансии
{
    "id": "7760476",
    "premium": true,
    "has_test": true,
    "response_url": null,
    "address": null,
    "alternate_url": "https://hh.ru/vacancy/7760476",
    "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=7760476",
    "department": {
        "id": "HH-1455-TECH",
        "name": "HeadHunter::Технический департамент"
    },
    "salary": {
        "to": null,
        "from": 100000,
        "currency": "RUR",
        "gross": true
    },
    "name": "Специалист по автоматизации тестирования (Java, Selenium)",
    "insider_interview": {
        "id": "12345",
        "url": "https://hh.ru/interview/12345?employerId=777"
    },
    "area": {
        "url": "https://api.hh.ru/areas/1",
        "id": "1",
        "name": "Москва"
    },
    "url": "https://api.hh.ru/vacancies/7760476",
    "published_at": "2013-10-11T13:27:16+0400",
    "relations": [],
    "employer": {
        "url": "https://api.hh.ru/employers/1455",
        "alternate_url": "https://hh.ru/employer/1455",
        "logo_urls": {
            "90": "https://hh.ru/employer-logo/289027.png",
            "240": "https://hh.ru/employer-logo/289169.png",
            "original": "https://hh.ru/file/2352807.png"
        },
        "name": "HeadHunter",
        "id": "1455"
    },
    "response_letter_required": false,
    "type": {
        "id": "open",
        "name": "Открытая"
    },
    "archived": "false",
    "working_days": [
        {
            "id": "only_saturday_and_sunday",
            "name": "Работа только по сб и вс"
        }
    ],
    "working_time_intervals": [
        {
            "id": "from_four_to_six_hours_in_a_day",
            "name": "Можно работать сменами по 4-6 часов в день"
        }
    ],
    "working_time_modes": [
        {
            "id": "start_after_sixteen",
            "name": "Можно начинать работать после 16-00"
        }
    ],
    "accept_temporary": false,
    "experience": {
      "id": "noExperience",
      "name": "Нет опыта"
    },
    "employment": {
      "id": "full",
      "name": "Полная занятость"
    },
    "show_logo_in_search": true
}
Описание полей смотрите в выдаче полной вакансии.

url и alternate_url могут принимать значение null в случае, если подробная информация о вакансии недоступна (например, вакансия была удалена).