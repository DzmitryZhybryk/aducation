# WEB

# Python

## База

1. Что такое PEP?
    - `Предложения по развитию python. Является основным механизмом для предложения новых возможностей`
2. Что такое PEP8? -
    - `Это style guide того, как должен быть оформлен код, написанный на python`
3. Какие типы данных есть в Python?
    - `В Python есть изменяемые и неизменяемые типы данных. К не изменяемым типам данных относятся (str, bytes, int, float, complex, bool, None, tuple, frozenset). К изменяемым (list, set, dict, bytarroy, memoryview)`
4. Что такое виртуальное окружение? Зачем оно нужно? Какие инструменты для этого используются?
    - `Используется для того, чтобы изолировать локальный Python от глобального`
5. Можно ли изменить элемент в кортеже, если кортеж неизменяемый тип данных?
    - `Можно. test_set = ([], 1), test_set[0].append(2)`
6. Что такое list, set и dict comprehensions?
    - `[i for i in range(5)], {i for i in range(5)}, {key: value ** 2 for key,valye in range(5)}`
7. Какая разница между == и is?
8. Что такое глубокая и поверхностная копия? Зачем нужны? Как сделать?
9. Как работают операторы AND, OR и NOT? Что они возвращают?
    - `NOT` приводит объект к какому-то bool значению: not [] = True, not {1} = False`
    - `AND` если первый операнд False, AND возвращает его. Если True, вернёт второй.
      print([] and 123) вернёт []`
    - `OR` проверяет, что хотя бы один операнд является True. print([] or 123) вернёт 123
10. Как работает расширение пространства имён в Python? Как работает LEGB?
    - `Работает по правило Local,Enclosing, Global, Built-in`
11. Как работают операторы global и nonlocal
    - [global_nonlocal.py](https://github.com/DzmitryZhybryk/aducation/blob/main/global_nonlocal.py?plain=1)
12. Функции map, filter, zip, reduce
    - [internal_funcs.py](https://github.com/DzmitryZhybryk/aducation/blob/main/internal_funcs.py?plain=1)
13. Как оценивается сложность алгоритмов и почему? Что такое Big-O notation
    - `Это метод оценки, который определяет как изменяется затраты на выполнение в зависимости от величины входных данных`
14. Какая алгоритмическая сложность основных операций в коллекциях?
15. Что такое функция? Какие преимущества использования функций?
    - `Функция` - это именованный блок кода, к которому можно обратиться из другого места программы. Преимущество -
      повторное использование, избегание повторений блоков кода (DRY)`
16. Какой будет результат выполнения функции, если в нём нет оператора return?
17. Что такое аннотация типов? Зачем они нужны? Когда выполняются аннотации типов?
    - `Это подискаки для IDE, линтеров и других программистов. В рантайме не выполняются`
18. Как в Python передаются аргументы в функцию?
    - `Есть два способа: по ссылки и по значения. Конкретно в Python все аргументы функции передаются по ссылке`
19. Что будет, если использовать значение изменяемого типа в качестве аргумента по умолчанию в функции? Как этого
    избежать?
20. Что такое *args и **kwargs? Какие типы данных для них используются?
    - `*args` - используется для передачи неограниченного количества позиционных аргументов функции`
    - `**kwargs` - используется для передачи неограниченного количества аргументов ключ-значение
21. Что такое lambda функция? Приведи примеры их использования.
    - [internal_funcs.py](https://github.com/DzmitryZhybryk/aducation/blob/main/internal_funcs.py?plain=1)
22. Что такое рекурсия? Какие ограничения есть у рекурсии в Python? Плюсы и минусы рекурсии?
    - `Код относительно просто выглядит`
    - `Использует больше памяти`
    - `Огранические 1000 вызовов. Можно изменить через sys.setrecursionlimit`
    - [factorial.py](https://github.com/DzmitryZhybryk/aducation/blob/main/factorial.py?plain=1)
23. Зачем нужен декоратор property?
    - `Property позволяет создать динамический аттрибут. Очень похожи на аттрибуты, но на самом деле это функции`
    - [property.py](https://github.com/DzmitryZhybryk/aducation/blob/main/property.py?plain=1)
24. Что такое замыкание?
    - `Замыкание` - это механизм, когда одна функция использует переменную из внешней области видимости
    - [decorators.py](https://github.com/DzmitryZhybryk/aducation/blob/main/decorators.py?plain=1)
25. Что такое декоратор? Зачем нужен декоратор?
    - `Декоратор` - это паттерн проектирования. Нужен для того, чтобы изменить поведение функции или класса без
      изменения исходного кода. Канонически реализуется с помощью класса, но в Python есть синтаксический сахар для
      этого
26. Что такое итерируемый объект?
    - `Это объект, который предоставляет возможность поочерёдного прохода по своим элементам iterable`
27. Что такое итератор? Как создать итератор из коллекции?
    - `Разница между iterable и итератор в том, что iterable реализует метод __iter__, а итератор реализует ещё метод __next__. Создать итератор можно так: a = [1,2,3], i = iter(a)`
28. Как сделать класс, который будет поддерживать протокол итератора?
    - [iterator.py](https://github.com/DzmitryZhybryk/aducation/blob/main/iterator.py?plain=1)
29. Что такое генератор? Как написать? Какие преимущества?
    - `Вызывается по требованию`
30. Что такое generator comprehension?
31. Может ли в одном генераторе быть много yield? Как это работает?
32. Зачем нужна конструкция yield from?
    - `Для того, чтобы в одном генераторе вернуть значения другого генератора`
    - [generator.py](https://github.com/DzmitryZhybryk/aducation/blob/main/generator.py?plain=1)
33. Что такое менеджер контекста?
    - `Менеджер контекста` - это конструкция with .. as .., которая позволяет нам обратиться к какому-то объекту,
      получить другой объект и работать внутри его контекста. Если возникнет какое-то исключение, то есть специальный
      код, который может это исключение обработать
34. Как реализовать класс, объект которого может работать в менеджере контекста? Что будет присвоено после as? Какие
    аргументы принимает __exit__?
35. Какие блоки исключений существуют в Python? Когда каждая из них выполняется?
    - `try, except, else, finally`
36. Можно ли одним блоком except ловить много исключений?
37. В чём разница между Except и Except Exception?
    - `except` ловит BaseException
    - `Exception` ловит Exception
38. Как поднять исключение в блоке except?
    - `raise`
39. Зачем нужны классы BaseExceptionGroup и ExceptionGroup
    - `Позволяют кинуть сразу много исключений за раз `
40. В чем разница между except и except*?
    - `Когда мы рейзим ExceptionGroup и отлавливаем в except*, он распакует все exception, которые мы рейзили`
41. Как создать свой тип исключения? Зачем он может быть нужен?
42. Что такое модуль?
    - `Модуль` - это файл с расширением .py, который содержит код на python
43. Что такое пакет?
    - `Пакет` - это некоторая директория, которая содержит python модули
44. Зачем нужен __init__.py?
    - `нужен для того, чтобы указать инструкции, которые будут выполлняться при импорте пакета. Выполняется при первом импорте`
45. Когда возникает проблема циклического импорта? Как это решить?
    - `возникает, когда 2 модуля пытаются импортировать данные друг из друга. Обычно решается с помощью третьего модуля`
46. Что такое Интроспекция?
    - `Интроспекция` - возможность запросить тип и структуру объекта во время выполнения программы
47. Что такое тернарный оператор? Как записывается?
48. Что такое метаклассы? Для чего они используются?
    - `метакласс` - это шаблоны для классов. На основе метаклассов строятся классы. Используются для того, чтобы
      перехватить создание классов. Имеют 4 метода: __prepare__ подготавливает данные, они попадают в __new__ и он
      создаёт класс. __init__ отвечает за его инициализацию, а __call__ за создание объектов класса. Если хотим, чтобы
      от нашего метакласса можно было создать абстрактный класс, наследуем от ABCMeta. В противном случае наследуем от
      type
49. Что такое MRO?
50. Какие есть библиотеки для выполнения код конкурентно?
    - `multiprocessing`
    - `threading`
    - `asyncio`
51. Что такое event loop?
    - `event loop` - это цикл событий, который отслеживает события ввода/вывода и переключает задачи, которые готовы и
      ждут операции ввода/вывода
52. Что такое корутина?
    - `корутина` - это блоки кода, которые работают асинхронно, то есть по очереди. В нужный момент выполнение такого
      блока приостанавливается с сохранением всех его свойств, чтобы запустился другой код. Когда управление
      возвращается к первому блоку, он продолжает работу.
53. Зачем нужна конструкция async/await?
    - `Эта конструкция превращает процедуру в корутину. Она прекращает своё выполнение на время await, дожидается асинхронного события и возобновляет работу`
54. Что такое enumerate в python? Чем отличается от range?
    - `range позволяет получить индексы элементов в списке, а enumerate сразу индекс и значение`

## ООП

1. Что такое класс?
    - `Класс` - это модель для создания объектов определённого типа, описывающая их структуру и поведение
2. Что такое объект класса?
    - `Объект класса` - это некоторая уникальная сущность определённого класса, которая обладает структурой и поведением
3. Как реализовать метод объекта и что такое self?
4. Что такое метод класса и что такое cls?
5. Как реализовать статический метод?
6. Модификаторы доступов в Python?
    - `В Python нет модификаторов доступа и всё по умолчанию public`
7. Как в Python реализуются public, private, protected?
8. Как в классах хранятся аттрибуты и методы?
    - `Во всех класса аттрибуты и методы хранятся в специальном дандер аттрибуте __dict__`
9. Чем отличается аттрибут класса от аттрибута объекта? Возможно ли использовать одинаковое имя для них?
    - `Возможно. Это два разные словаря, которые никак друг другу не мешают. class_name.__dict__ и self.__dict__`
10. Что такое абстрактный класс? Зачем они нужны? Как реализуются в Python?
    - `В Python нет интерфейсов, поэтому вместо них мы используем абстрактные классы. Абстрактные классы определяет интерфейс, который мы должны реализовать в дочерних классах`
11. Какая разница между методами __new__ и __init__? Какой вызывается первым?
    - `В Python конструктор разделён на метод, который создаёт объект и который инициализирует объект`
12. Какая разница между методами __str__ и __repr__? Какой из них использовать?
    - `Оба метода отвечают за строкове представление объекта`
        - `__str__` отвечает за представление, которое ближе к пользователю
        - `__repr__` отвечает за формальное представление, которое ближе к машине
        - `Если мы создадим какой-то объект и принтанём его, по умолчанию отработает __str__. Если его нет, то принт будет искать __repr__. Если и его нет, то отработает стандартный __repr__, который определён в object`
        - `Чтобы обратиться к методы __repr__ есть функция repr(self)`
        - `Для обычных принтов __str__, для логов __repr__`
13. Зачем может быть использована функция super?
    - `Используется для обращения к методу родительского класса`
14. Что такое ООП?
    - `ООП` - методология программирования, основанная на представлении программы в виде совокупности объектов, каждый
      из которого является экземпляром какого-то класса, а классы образуют иерархию наследования
15. Базовые принципы ООП?
    - `Абстракция` - использование только тех характеристик объекта, которые нам нужны
    - `Наследование` - принцип ООП, согласно которому мы можем создать некоторый класс на основе предыдущего класса.
      Дочерний класс будет получать весь функционал родительского класса.
    - `Инкапсуляция` - может пониматься двояко. Если говорим про Python, то это объединение переменных и функций,
      которые привержены общей цели, в классе. Вторая трактовка - разграничение абстракции от реализации. Наружу должен
      торчать только тот функционал, который нужен пользователю
    - `Полиморфизм` - Бывает параметрическим и ad-hoc. Параметрический полиморфизм означает, что выполнение функции не
      зависит от того, какой тип аргумента она принимает. ad-hoc полиморфизм, когда функция может иметь множество
      имплементаций, в зависимости от типа аргумента, который она получает
16. Когда лучше использовать наследование, а когда композицию?
    - `Композиция` - когда мы создаём какой-то класс и некоторый класс используем в качестве части этого класса
    - `Если нужен весь функционал - используем наследование. Если часть - композицию`
17. Что такое Миксин? Чем отличается от обычного класса?
    - `Скорее всего не захотим создавать объект этого класса. Там просто есть некоторая мелкая логика, которую мы можем подмешивать с помощью наследования`

## Best Practices

1. Какие есть Best Practices?
    - `SOLID, KISS, DRY, YAGNI`
2. Что такое SOLID?
    - `single responsibility/принцип единичной ответственности` - каждый класс должен выполнять только те цели, для
      которых он было задумал
    - `open/close` - класс должен быть открыт для расширения и закрыт для модификации
    - `Liskov substitution principle/Принцип подстановки Барбаты Лисков` - это о том, что если у нас есть родительский
      класс, есть его дочерний класс и функция родительского класса, мы в эту функцию можем отправить объект
      дочернего класса и это будет работать
    - `interface segregation principle/принцип разделения интерфейсов` - много интерфейсов, специально предназначенных
      для клиентов, лучше, чем один интерфейс общего назначения
    - `dependency inversion principle/принцип инверсии зависимостей` - зависимости должны быть на абстракциях, а не на
      чем-то конкретном

## Базы данных

1. Какие бывают типы баз данных?
2. Какие NoSQL/SQL базы данных знаешь? С какими работал? Кейсы использования? Плюсы/минусы?
3. Что такое PK и FK?
    - `Primaty key` - это ключ, который однозначно идентифицирует строку в таблице
    - `Foreign key` - нужен для связи разных таблиц?
4. Какие типы связей знаешь?
5. Зачем нужны индексы? Какие виды бывают? Плюсы/Минусы
    - `Если мы по какому-то полю работаем часто, т.е. часто делаем поиск по нему, есть смысл проиндексировать это поле. Работа с этим полем будет быстрее. Однако индексирование увеличивает требования к объёму хранилища, а так же замедление выполнения операция вставки и обновления`
    - `B-дерево` - медленные операции обновлений
    - `Bitmap-индекс` - не подходят для столбцов, где много уникальных значений
    - `Хэш-индекс` - хорошо подходят только для поисков равенства (найти все записи, где столбец А равен значению X). Не
      подходят для селектов диапазонов и сортировок
    - `GiST` - хорошо подходит для БД, содержащих гео-локационные данных
    - `Полнотекстовый индекс` - хорошо подходит для БД, содержащих большие объемы текстовых данных
6. Что такое триггеры?
    - `Триггеры` - это event handler, которые слушают какие-то события и потом по этим событиям можно выполнять какие-то
      действия. Например, слушаем обновление таблицы и когда таблица обновилась поле updated_at меняем на текущую дату
7. Что такое транзакции?
    - `Транзакции` - это какой-то блок операций, в котором будут выполнены либо все операции, либо ни одной. Но есть
      операции, которые неявно делают commit в транзакции, поэтому надо быть аккуратными. К ним относятся например
      DropTable и AlterTable
8. Что такое ACID? BASE?
    - `ACID это про то, что наши транзакции надёжны`
        - `A` - atomicity/атомарность, транзакция не может быть зафиксирована частично
        - `C` - consistency/согласованность, в результате успешного выполнения транзакции база данных переводится из
          одного согласованного состояния в другое
        - `I` - isolate/изолированность, одна транзакция не может вклиниться в другую
        - `D` - durability/надёжность, если транзакция завершена, то результат зафиксирован в системе и никакой внешний
          фактор на это не может повлиять
    - `BASE гибкий подход манипулирования данными в NoSQL`
        - `Basically availably` - базовая доступность, вместо немедленной согласованности обеспечивают доступность
          данных путём распределения и репликации их по узлам кластера базы данных
        - `Soft state` - мягкое состояние, из-за отсутствия согласованности данные могут меняться со временем.
          Делегирует это разработчику
        - `Eventually consistent` - окончательная согласованность, BASE не обеспечивает немедленную согласованность.
          Пока это не произойдет, чтение данных всё ещё возможно (хотя может не отражать реальность)
9. Какие феномены возможны при параллельном выполнении транзакций?
    - `Потерянное обновление` - когда разные транзакции одновременно изменяют одни и те же данные, после фиксации может
      оказаться, что одна транзакция перезаписала данные, обновленные и зафиксированные другой транзакцией.
    - `Грязное чтение` - транзакция читает данные, изменённые параллельной транзакцией, которая ещё не завершилась. Если
      эта параллельная транзакция будет отменена, окажется, что первая транзакция прочитала данные, которых нет в
      системе.
    - `Неповторяющееся чтение` - При повторном чтении тех же самых данных в рамках одной транзакции оказывается, что
      другая транзакция успела изменить и зафиксировать эти данные. В результате тот же самый запрос выдаёт другой
      результат.
    - `Фантомное чтение` - транзакция повторно выбирает множество строк в соответствии с одним и тем же критерием. В
      интервале времени между выполнением этих выборок другая транзакция добавляет новые строки и фиксирует изменения. В
      результате при выполнении повторной выборки в первой транзакции может быть получен другой результат.
    - `Аномалия сериализации` - Результат успешной фиксации группы транзакций, выполняющихся параллельно, не совпадает с
      результатом ни одного из возможных вариантов упорядочения этих транзакций, если бы они выполнялись
      последовательно.
10. Уровни изолированности транзакции (Postgres).
    - `Есть общий SQL стандарт изолированности данных. В Postgres немного более строгий вариант их реализации. Подробнее:`
        - `READ UNCOMMITTED` - низший уровень. Транзакции может читать "грязные" данные. В Postgres это невозможно,
          следовательно, этот уровень транзакции в ней не реализован.
        - `READ COMMITTED` - Не допускает чтение "грязных" (незафиксированных) данных. Таким образом, транзакция видит
          только те незафиксированные данные, которые произведены в ходе выполнения её самой.
        - `REPEATABLE READ` - Не допускается чтение "грязных" данных и неповторяющееся чтение. В Postgres на этом уровне
          так же не допускается фантомное чтение.
        - `SERIALIZABLE` - На этом уровне моделируется последовательное выполнение всех зафиксированных транзакций,
          как если бы транзакции выполнялись одна за другой, последовательно, а не параллельно
11. Как создать таблицу?
    - `CREATE TABLE IF NOT EXIST test_table (first_column INT, second_column VARCHAR(255))`
12. Как изменить таблицу?
    - `ALTER TABLE table_name DROP COLUMN {column_name}`
    - `ALTER TABLE table_name ADD UNIQUE {column_name}`
13. Разные insert
    - `INSERT INTO table_name (clumn_name, column_name) VALUES (value, value)`
14. Разные select
    - `SELECT column_1, column_2 FROM table_name`
    - `SELECT column_1, column_2 FROM table_name ORDER BY column_1` - c сортировкой
    - `SELECT column_1, column_2 FROM table_name GROUP BY column_2 ORDER BY column_1` - c сортировкой и группировкой по
      столбцу
15. Типы JOIN при SELECT?
    - `inner join` - SELECT column_name FROM table_1 INNER JOIN table_2 ON table_1.column_name = table_2.column_name
    - `left join` - SELECT column_name FROM table_1 LEFT JOIN table_2 ON table_1.column_name = table_2.column_name
    - `full join` - SELECT column_name FROM table_1 FULL OUTER JOIN ON table_1.column_name = table_2.column_name WHERE
      condition
16. Отличие REPEATABLE READ от SELECT FOR UPDATE?
    - `REPEATABLE READ` - блокирует чтение. Но другие транзакции тоже могут получить блокировку чтения, что может
      помешать выполнить обновление позже
    - `SELECT FOR UPDATE` - информирует любые другие транзакции, запрашивающие блокировку чтения, о том, что им следует
      подождать, пока вы не закончите обновление записи
17. Виды блокировок базы данных:
    - `Оптимистичная блокировка` - реальная блокировка не происходит. Если во время выполнения транзакции она изменяет
      данные, которые были изменены после её начала, транзакция прерывается с исключением. Для реализации часто
      используется версионирование данных - в таблицу добавляют колонку, которая хранит текущую версию. При выполнении
      update в запросе в секции where передаётся версия данных, которая была забрана на изменение.
    - `Пессимистичная блокировка` - блокировка на уровне базы данных.
18. Что такое нормализация и де-нормализация базы данных?
    - `Нормализация` - это процесс приведения таблиц к нормальным формам, т.е. устранение избыточности
    - `Избыточность` - это когда мы храним данных больше, чем нам нужно, т.е. одни и те же данных хранятся во многих
      местах и создают избыточность. Избыточность это плохо, потому что может возникать рассенхрон данных +
      дополнительный расход места на диске. Индексы - это тоже избыточность.
19. Какие типы нормализации бывают?
    - `Первая нормальная форма`:
        - `нет дублирующихся строк`
        - `все аттрибуты атомарны`
        - `нет повторяющихся аттрибутов с одинаковым смыслом`
    - `Вторая нормальная форма`:
        - `таблица находится в первой нормальной форме`
        - `есть первичный ключ`
        - `все неключевые аттрибуты функционально зависят от ключа целиком, но не от его части`
    - `Первая нормальная форма`:
        - `таблица находится во второй нормальной форме`
        - `неключевые аттрибуты напрямую зависят только от PK, но не от других аттрибутов`
20. Теорема CAP?
    - `Говорит о том, что в распределённых системах нельзя одновременно добиться трёх свойс`:
        - `Consistency` - на всех не отказавших узлах одинаковые (с точки зрения пользователя) данные
        - `Availability` - запросы ко всем не отказавшим узлам возвращают ответ
        - `Partition tolerance` - даже если связь стала нестабильной, но узлы работают, система в целом продолжает
          работать

## Паттерны проектирования

1. Какие бывают паттерны проектирования?
    - `Порождающие`
        - `абстрактная фабрика` - позволяет создать семейства связанных объектов, не привязываясь к конкретным классам
          создаваемых объектов. Для начала создаём интерфейс для каждого объекта, например Chair. Затем создаём
          абстрактную фабрику, общий интерфейс, который содержит методы создания объектов, например createChair: Chair.
          Для каждой вариации продуктов мы создаём свою абстрактную фабрику и реализуем методы create.
        - `фабричный метод` - предлагает создавать объекты не напрямую, а через вызов особого фабричного метода. Все
          возвращаемые объекты должны иметь общий интерфейс, т.е. подклассы смогут производить объекты различных
          классов,
          следующих одному и тому же интерфейсу. Пример: класс Транспорт с методом доставка, который реализуют классы
          Корабль и Грузовик, но по своему
        - `строитель` - позволяет создать сложные объекты пошагово, вместо того, чтобы делать огромный __init__, или
          много наследований. Паттерн предлагает вынести конструирование объекта за пределы его собственного класса.
        - `прототип` - вводит общий интерфейс для копирования объектов
        - `одиночка` - гарантирует, что у класса будет только один экземпляр
    - `Структурные`
        - `адаптер` - помогает связать два интерфейса
        - `фасад` - простой интерфейс для работы со сложной системой. Может иметь урезанный интерфейс, не имеющий всей
          функциональности, которой можно достичь. Но предоставляет только те фичи, которые нужные клиенту, скрывая
          остальное.
        - декоратор
        - `компоновщик`
    - `Поведенческие`
        - `итератор` - позволяет последовательно обходить элементы составных объектов, не раскрывая их внутреннего
          представления
        - `стратегия`
        - `шаблонный метод` - паттерн предлагает разбить некоторый алгоритм на последовательность шагов, описать эти
          шаги в отдельных методах и вызывать их в одном шаблонном методе друг за другом
    - `Репозиторий` - это слой абстракции, который инкапсулирует в себе всю логику хранения данных
    - `UoW` - паттерн, определяющий логическую транзакцию, т.е. синхронизацию изменений в объектах, помещённых в UoW с
      хранилищем
    - `DAO`

2.Какие бывают паттерны проектирования микросервисов?
    - `SAGA`
    - `API Gateway`

## Сетевая модель OSI

1. Что представляет из себя модель OSI
    - `Прикладной уровень` - использует свои протоколы, чтобы пользователь увидел данные. HTTP, SMTP, AMQP
    - `Уровень представления` - преобразование протоколов и кодирование/декодирование данных
    - `Сеансовый уровень` - позволяет приложениям взаимодействовать между собой длительное время. RPC, gRPC
    - `Транспортный уровень` - занимается доставкой пакетов. Представлен TCP и UPD
    - `Сетевой уровень` - предназначен для определения пути передачи данных. Определяет кратчайшие маршруты, отслеживает
      неполадки и заторы в сети
    - `Канальный уровень` - передаёт сообщения по каналам связи. Определяет начало и конец в потоке битов. Обнаружение и
      корректировка ошибок.
    - `Физический уровень` - передача данных в двоичном виде от одного устройства к другому
2. Что такое WebSocker?
    - `WebSocker` - это протокол связи поверх TCP соединения. Предназначен для обмена сообщениями между клиентом и
      сервером, используя постоянное соединение. Интерактивный режим, позволяет создавать приложения реального времени.