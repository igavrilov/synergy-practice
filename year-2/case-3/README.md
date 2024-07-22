# Кейс-задача № 3
Спроектируйте базу данных «Туризм» (перечень предоставляемых услуг, заказ туров и др.). При проектировании базы данных необходимо создать 4-5 таблиц предметной области: 3-4 таблицы-справочника и 1 таблицу переменной информации. Для всех таблиц создать первичные ключи. Построить связи между таблицами при помощи внешних ключей: атрибуты таблицы переменной информации должны ссылаться на ключевые атрибуты таблиц справочников. 

Когда вы создаете базу данных в MySQL с помощью MySQL Workbench (или любого другого инструмента), вы можете экспортировать схему базы данных в виде скрипта SQL. Этот скрипт SQL содержит определения таблиц, связей, индексов и других структур базы данных, которые вы создали. Или иным удобным для Вас способом.

# Решение

1. **Таблицы-справочники:**
    - **Услуги (Services)**
    - **Туры (Tours)**
    - **Клиенты (Customers)**
    - **Сотрудники (Employees)**

2. **Таблица переменной информации:**
    - **Заказы (Orders)**

## Таблица «Услуги» (Services)

| Поле           | Тип данных   | Описание                   |
|----------------|--------------|----------------------------|
| `service_id`   | INT          | Первичный ключ             |
| `service_name` | VARCHAR(255) | Название услуги            |
| `description`  | TEXT         | Описание услуги            |
| `price`        | DECIMAL(10,2)| Цена за услугу             |

## Таблица «Туры» (Tours)

| Поле           | Тип данных   | Описание                   |
|----------------|--------------|----------------------------|
| `tour_id`      | INT          | Первичный ключ             |
| `tour_name`    | VARCHAR(255) | Название тура              |
| `description`  | TEXT         | Описание тура              |
| `duration_days`| INT          | Продолжительность (дни)    |

## Таблица «Клиенты» (Customers)

| Поле           | Тип данных   | Описание                   |
|----------------|--------------|----------------------------|
| `customer_id`  | INT          | Первичный ключ             |
| `first_name`   | VARCHAR(255) | Имя клиента                |
| `last_name`    | VARCHAR(255) | Фамилия клиента            |
| `email`        | VARCHAR(255) | Электронная почта          |
| `phone`        | VARCHAR(20)  | Телефон                    |

## Таблица «Сотрудники» (Employees)

| Поле           | Тип данных   | Описание                   |
|----------------|--------------|----------------------------|
| `employee_id`  | INT          | Первичный ключ             |
| `first_name`   | VARCHAR(255) | Имя сотрудника             |
| `last_name`    | VARCHAR(255) | Фамилия сотрудника         |
| `position`     | VARCHAR(255) | Должность                  |
| `hire_date`    | DATE         | Дата найма                 |

## Таблица «Заказы» (Orders)

| Поле           | Тип данных   | Описание                   |
|----------------|--------------|----------------------------|
| `order_id`     | INT          | Первичный ключ             |
| `customer_id`  | INT          | Внешний ключ (Клиенты)     |
| `tour_id`      | INT          | Внешний ключ (Туры)        |
| `service_id`   | INT          | Внешний ключ (Услуги)      |
| `employee_id`  | INT          | Внешний ключ (Сотрудники)  |
| `order_date`   | DATE         | Дата заказа                |
| `total_price`  | DECIMAL(10,2)| Общая стоимость            |

## Связи между таблицами

- Таблица «Заказы» содержит внешние ключи для всех справочных таблиц.
- Внешний ключ `customer_id` ссылается на `customer_id` в таблице «Клиенты».
- Внешний ключ `tour_id` ссылается на `tour_id` в таблице «Туры».
- Внешний ключ `service_id` ссылается на `service_id` в таблице «Услуги».
- Внешний ключ `employee_id` ссылается на `employee_id` в таблице «Сотрудники».

## SQL запросы для создания таблиц

```sql
CREATE TABLE Services (
    service_id INT PRIMARY KEY,
    service_name VARCHAR(255),
    description TEXT,
    price DECIMAL(10, 2)
);

CREATE TABLE Tours (
    tour_id INT PRIMARY KEY,
    tour_name VARCHAR(255),
    description TEXT,
    duration_days INT
);

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(20)
);

CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    position VARCHAR(255),
    hire_date DATE
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    tour_id INT,
    service_id INT,
    employee_id INT,
    order_date DATE,
    total_price DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (tour_id) REFERENCES Tours(tour_id),
    FOREIGN KEY (service_id) REFERENCES Services(service_id),
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
);
```
