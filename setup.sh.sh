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
outputdir="$srcdir/dist"  # �������, ���� ����� ������ ����������� ����

# ������ ����� ��� �������
echo "�������� ����������: ${srcdir}"
echo "�������� �������: ${projname}"
echo "������: ${version}"

# ��� 1: �������� ������� ����������� ������������
echo "�������� ������� ����������� ������������..."
for cmd in git pyinstaller python; do
  if ! command -v $cmd &> /dev/null; then
    echo "������: $cmd �� ����������. ���������� ��� ����� �������� �������."
    exit 1
  fi
done

# ��� 2: ���������� �����������
cd "$srcdir" || exit
if git rev-parse --is-inside-work-tree &> /dev/null; then
  echo "���������� �����������..."
  git pull origin main
else
  echo "��������������: ������� $srcdir �� �������� Git-������������. ������� ����������."
fi

# ��� 3: ������ ������������ ����� � ������� PyInstaller
echo "�������� ������������ ����� � ������� PyInstaller..."
pyinstaller --onefile --distpath "$outputdir" --name "$projname" main.py

# ��������, ��� �� ������ ����������� ����
if [ ! -f "$outputdir/$projname" ]; then
  echo "������: ����������� ���� �� ��� ������!"
  exit 1
fi

echo "����������� ���� ������: $outputdir/$projname"

# ��� 4: ������ ����-������
echo "������ ����-������..."
python -m unittest discover -s "$srcdir" -p '*test.py'

# ��� 5: �������� ������ � �������� (�����������)
echo "�������� ������ � ��������..."
tar -czvf "$outputdir/${projname}_v${version}.tar.gz" -C "$outputdir" "$projname"

echo "������� �������� �������."