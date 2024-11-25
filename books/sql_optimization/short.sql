1. Если в запросе используется функция преобразования, то индексы не работают!

SELECT * FROM users WHERE lower(username) = 'some';

SELECT * FROM users WHERE created_at::date BETWEEN '2024-10-10' AND '2024-10-11';

Правильно:

SELECT * FROM users WHERE created_at BETWEEN '2024-10-10' AND '2024-10-11';
SELECT * form users WHERE created_at >= CURRENT_DATE AND created_at < CURRENT_DATE + 1;

Тоже самое со встроенными функциями!

SELECT * FROM users WHERE COALESCE(actual_update_time, schedule_update_time) BETWEEN '2024-10-10' AND '2024-10-11';

Правильно:

SELECT * FROM users WHERE (actual_update_time BETWEEN '2024-10-10' AND '2024-10-11') 
OR
(actual_update_time IS NULL  AND schedule_update_time '2024-10-10' AND '2024-10-11');

Для поиска:

SELECT * FROM users WHERE lower(username) like 'some%';

Правильно создать индекс для поиска по шаблону:

CREATE INDEX account user_last_name_lower_pattern ON users (lower(username) text_pattern_ops);

2. Составные индексы

CREATE INDEX users_name_surname_phone_dep ON users (username, surname, phone_number);

Данный индекс будет поддерживать поиск по столбцу username, username + surname и username + surname + phone_number!

3. Покрывающие индексы

Обычный индекс не содержит в себе всех данных. Если в индексе нет данных, которые нужны для запроса, СУБД будет дополнительно обрадаться к таблице.
Чтобы этого избежать используют покрывающие индексы.

CREATE INDEX users_name_surname_phone_dep ON users (username, surname, phone_number) INCLUDE (email);
 
 4. Частичные индексы

 Если по какому-то полю высокая селективнось, можно создать индекс только по какому-то конерктному значению:

 CREATE INDEX phone_number_is_not_null ON users (phone_number) WHERE phone_number IS NOT NULL;
 CREATE INDEX flight_canceled ON flight (flight_id) WHERE status = 'Canceled' (Хорошо для Enum)