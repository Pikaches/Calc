#!/bin/bash

# �������� ����������
if [ -z "$1" ]; then
  echo "�� ������ ������ ��������, ���������� �� ���� �� ���������� � �����������";
  exit 1
fi

if [ -z "$2" ]; then
  echo "�� ������ ������ ��������, ���������� �� ������ �������";
  exit 1
fi

# ��������� ����������
srcdir=$1
version=$2
projname="CalculatorApp"  # �������� �������
outputdir="$srcdir"       # �������, ���� ����� ������ .exe

# ������ ����� ��� �������
echo "�������� ����������: ${srcdir}"
echo "�������� �������: ${projname}"
echo "������: ${version}"

# ��� 1: ���������� �����������
cd $srcdir || exit
git pull origin main

# ��� 2: ������ ������������ ����� � ������� PyInstaller
echo "�������� ����������� ����� � ������� PyInstaller..."
pyinstaller --onefile --distpath "$outputdir" --name "$projname" main.py

# ��������, ��� �� ������ .exe ����
if [ ! -f "$outputdir/$projname.exe" ]; then
  echo "������: ����������� ���� .exe �� ��� ������!"
  exit 1
fi

echo "����������� ���� ������: $outputdir/$projname.exe"

# ��� 3: ������ ����-������
echo "������ ����-������..."
python -m unittest discover -s "$srcdir" -p '*test.py'

# ��� 4: �������� ����������� (�����������)
# ����� ����� �������� ��� ��� �������� �����������, �������� � ������� Inno Setup ��� ��������� �������� .exe ����.

echo "������� �������� �������."
