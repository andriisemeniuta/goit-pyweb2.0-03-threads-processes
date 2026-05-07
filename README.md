### 1. File Sorting (Threading)
File: `task_1.py`
The program takes files from a source folder and copies them to a destination folder, sorting them into subfolders based on their extensions.
- Uses multithreading to speed up file copying and directory scanning.
- Usage: `python task_1.py <source_folder> <destination_folder>`

### 2. Factorization (Multiprocessing)
File: `task_2.py`
The function finds all divisors for a given list of numbers.
- Implements two versions: synchronous and multiprocessing (utilizing all CPU cores).
- Outputs execution time to compare performance.
- Usage: `python task_2.py`







### 1. Сортировка файлов (Потоки)
Файл: `task_1.py`
Программа берет файлы из одной папки и копирует их в другую, сортируя по папкам на основе расширений. 
- Использует многопоточность для ускорения копирования файлов и чтения папок.
- Запуск: `python task_1.py <откуда> <куда>`

### 2. Расчет делителей (Процессы)
Файл: `task_2.py`
Функция ищет все делители для заданных чисел.
- Реализовано два варианта: обычный и многопроцессорный (использует все ядра CPU).
- Выводит время работы для сравнения скорости.
- Запуск: `python task_2.py`