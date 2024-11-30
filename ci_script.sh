#!/bin/bash

# Устанавливаем путь к проекту и версию
PROJECT_DIR="D:/Calc/Calc"
VERSION="1.0.0"  # Версия проекта

echo "Работаем с проектом в директории: $PROJECT_DIR"
echo "Версия: $VERSION"

# Переход в директорию проекта
cd "$PROJECT_DIR" || { echo "Ошибка: не удалось найти директорию $PROJECT_DIR"; exit 1; }

# Шаг 1: Загрузка актуального состояния с сервера
echo "Загрузка актуального состояния с сервера..."
git pull origin main || { echo "Ошибка: не удалось обновить репозиторий!"; exit 1; }

# Шаг 2: Сборка проекта
echo "Сборка проекта..."
python setup.py build || { echo "Ошибка: не удалось собрать проект!"; exit 1; }

# Шаг 3: Запуск юнит-тестов
echo "Запуск юнит-тестов..."
python -m unittest unittest.py || { echo "Ошибка: тесты не пройдены!"; exit 1; }

# Шаг 4: Создание исполняемого файла
echo "Создание исполняемого файла..."
pyinstaller --onefile main.py || { echo "Ошибка: не удалось создать исполняемый файл!"; exit 1; }

# Проверка наличия файла в папке dist
if [ ! -f "dist/main.exe" ]; then
  echo "Ошибка: файл main.exe не был создан!"
  exit 1
fi
echo "Исполняемый файл создан: dist/main.exe"

# Шаг 5: Создание установочного .deb пакета
echo "Создание .deb пакета..."
DEB_PACKAGE_DIR="deb-package"
mkdir -p "$DEB_PACKAGE_DIR/DEBIAN"
mkdir -p "$DEB_PACKAGE_DIR/usr/local/bin"

# Копируем исполняемый файл в структуру пакета
cp dist/main.exe "$DEB_PACKAGE_DIR/usr/local/bin/calculator"

# Создаем файл control для пакета
cat > "$DEB_PACKAGE_DIR/DEBIAN/control" <<EOF
Package: calculator
Version: $VERSION
Architecture: amd64
Maintainer: Your Name <youremail@example.com>
Description: Simple calculator application
Depends: python3
EOF

dpkg-deb --build "$DEB_PACKAGE_DIR" || { echo "Ошибка: не удалось создать .deb пакет!"; exit 1; }
echo "Deb пакет создан: deb-package.deb"

# Шаг 6: Установка приложения
echo "Установка приложения..."
sudo dpkg -i deb-package.deb || { echo "Ошибка: не удалось установить приложение!"; exit 1; }

echo "Процесс CI завершён успешно!"