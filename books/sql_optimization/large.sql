1. Полусоединения

Это такое соединение таблиц А и В при котором возвращаются строки из таблицы А, для которых есть хотя бы одно строка из таблицы В.
Хорошо подходит для фильтрации по таблице В, если сами данные из этой таблицы не нужны.

employees(employee_id, name, department_id)
departments(department_id, department_name)

SELECT * FROM employees
WHERE EXISTS (
    SELECT 1 FROM departments
    WHERE employee.department_id = departament.department_id
);

SELECT *
FROM employees
WHERE employees.department_id IN (
    SELECT departament.department_id
    FROM departments
);

То же самое через JOIN

SELECT * FROM employee JOIN (SELECT DISTINCT department_id FROM departament) USING department_id;

2. Антисоединение - то же самое, только с NOT.