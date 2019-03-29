from bookkeeping.application.db.people import get_employees
from bookkeeping.application.salary import calculate_salary


def main():
    name = get_employees('Козлов Егор') # Получаем имя струдника 1
    name_2 = get_employees('Сидоров Иван') # Получаем имя сотрудника 2
    print(name)
    print(name_2)
    salary_name = calculate_salary(name, 1300, 24)
    # Вводим для сотрудника_1, оклад, сколько дней отработано, получаем зарплату
    salary_name_2 = calculate_salary(name_2, 1450, 20)
    # Вводим для сотрудника_2, оклад, сколько дней отработано, получаем зарплату
    print(salary_name)
    print(salary_name_2)

if __name__ == '__main__':

    main()
