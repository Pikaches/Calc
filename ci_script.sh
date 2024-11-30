#!/bin/bash

# ������������� ���� � ������� � ������
PROJECT_DIR="D:/Calc/Calc"
VERSION="1.0.0"  # ������ �������

echo "�������� � �������� � ����������: $PROJECT_DIR"
echo "������: $VERSION"

# ������� � ���������� �������
cd "$PROJECT_DIR" || { echo "������: �� ������� ����� ���������� $PROJECT_DIR"; exit 1; }

# ��� 1: �������� ����������� ��������� � �������
echo "�������� ����������� ��������� � �������..."
git pull origin main || { echo "������: �� ������� �������� �����������!"; exit 1; }

# ��� 2: ������ �������
echo "������ �������..."
python setup.py build || { echo "������: �� ������� ������� ������!"; exit 1; }

# ��� 3: ������ ����-������
echo "������ ����-������..."
python -m unittest unittest.py || { echo "������: ����� �� ��������!"; exit 1; }

# ��� 4: �������� ������������ �����
echo "�������� ������������ �����..."
pyinstaller --onefile main.py || { echo "������: �� ������� ������� ����������� ����!"; exit 1; }

# �������� ������� ����� � ����� dist
if [ ! -f "dist/main.exe" ]; then
  echo "������: ���� main.exe �� ��� ������!"
  exit 1
fi
echo "����������� ���� ������: dist/main.exe"

# ��� 5: �������� ������������� .deb ������
echo "�������� .deb ������..."
DEB_PACKAGE_DIR="deb-package"
mkdir -p "$DEB_PACKAGE_DIR/DEBIAN"
mkdir -p "$DEB_PACKAGE_DIR/usr/local/bin"

# �������� ����������� ���� � ��������� ������
cp dist/main.exe "$DEB_PACKAGE_DIR/usr/local/bin/calculator"

# ������� ���� control ��� ������
cat > "$DEB_PACKAGE_DIR/DEBIAN/control" <<EOF
Package: calculator
Version: $VERSION
Architecture: amd64
Maintainer: Your Name <youremail@example.com>
Description: Simple calculator application
Depends: python3
EOF

dpkg-deb --build "$DEB_PACKAGE_DIR" || { echo "������: �� ������� ������� .deb �����!"; exit 1; }
echo "Deb ����� ������: deb-package.deb"

# ��� 6: ��������� ����������
echo "��������� ����������..."
sudo dpkg -i deb-package.deb || { echo "������: �� ������� ���������� ����������!"; exit 1; }

echo "������� CI �������� �������!"