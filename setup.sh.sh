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
outputdir="$srcdir"       # Каталог, куда будет собран .exe

# Печать путей для отладки
echo "Исходная директория: ${srcdir}"
echo "Название проекта: ${projname}"
echo "Версия: ${version}"

# Шаг 1: Обновление репозитория
cd $srcdir || exit
git pull origin main

# Шаг 2: Сборка исполняемого файла с помощью PyInstaller
echo "Создание исполнимого файла с помощью PyInstaller..."
pyinstaller --onefile --distpath "$outputdir" --name "$projname" main.py

# Проверка, был ли создан .exe файл
if [ ! -f "$outputdir/$projname.exe" ]; then
  echo "Ошибка: исполняемый файл .exe не был создан!"
  exit 1
fi

echo "Исполняемый файл создан: $outputdir/$projname.exe"

# Шаг 3: Запуск юнит-тестов
echo "Запуск юнит-тестов..."
python -m unittest discover -s "$srcdir" -p '*test.py'

# Шаг 4: Создание установщика (опционально)
# Здесь можно добавить шаг для создания установщика, например с помощью Inno Setup или упрощённо оставить .exe файл.

echo "Процесс завершен успешно."
