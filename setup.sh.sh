#!/bin/bash

# Проверка аргументов
if [ -z "$1" ]; then
  echo "Не введен первый параметр, отвечающий за путь до директории с исходниками";
  exit 1
fi

if [ -z "$2" ]; then
  echo "Не введен второй параметр, отвечающий за версию проекта";
  exit 1
fi

# Установка переменных
srcdir=$1
version=$2
projname="CalculatorApp"  # Название проекта
outputdir="$srcdir/dist"  # Каталог, куда будет собран исполняемый файл

# Печать путей для отладки
echo "Исходная директория: ${srcdir}"
echo "Название проекта: ${projname}"
echo "Версия: ${version}"

# Шаг 1: Проверка наличия необходимых инструментов
echo "Проверка наличия необходимых инструментов..."
for cmd in git pyinstaller python; do
  if ! command -v $cmd &> /dev/null; then
    echo "Ошибка: $cmd не установлен. Установите его перед запуском скрипта."
    exit 1
  fi
done

# Шаг 2: Обновление репозитория
cd "$srcdir" || exit
if git rev-parse --is-inside-work-tree &> /dev/null; then
  echo "Обновление репозитория..."
  git pull origin main
else
  echo "Предупреждение: каталог $srcdir не является Git-репозиторием. Пропуск обновления."
fi

# Шаг 3: Сборка исполняемого файла с помощью PyInstaller
echo "Создание исполняемого файла с помощью PyInstaller..."
pyinstaller --onefile --distpath "$outputdir" --name "$projname" main.py

# Проверка, был ли создан исполняемый файл
if [ ! -f "$outputdir/$projname" ]; then
  echo "Ошибка: исполняемый файл не был создан!"
  exit 1
fi

echo "Исполняемый файл создан: $outputdir/$projname"

# Шаг 4: Запуск юнит-тестов
echo "Запуск юнит-тестов..."
python -m unittest discover -s "$srcdir" -p '*test.py'

# Шаг 5: Создание архива с проектом (опционально)
echo "Создание архива с проектом..."
tar -czvf "$outputdir/${projname}_v${version}.tar.gz" -C "$outputdir" "$projname"

echo "Процесс завершен успешно."