# ЗАПУСК КОДА Python:
# Можно запускать в браузере на сайте https://ideone.com/ и др.
# Запуск с Visual Studio и других IDE при добавлении компонента Python
# Запуск с консоли с патчем:
#   D:\Documents\Program\Python>python HW.py
# Запуск с консоли без патча:
#   D:\Documents\Program\Python>"C:\Program Files (x86)\Python38-32\python.exe" HW.py

# КОМПИЛЯЦИЯ В EXE
# Установка компилятора с консоли:
#   pip install pyinstaller
# Апгрейд pip если надо:
#   C:\Users\Администратор>python -m pip install --upgrade pip
# Компиляция в exe (-f в один файл, -w для графики, -i "путь к иконке" с иконкой):
#   D:\Documents\Program\Python>pyinstaller -f HWplus.py

# Установка библиотек https://pypi.org/:
#   pip install pyside2
#   pip install pygame
#   pip install eel

# Бесплатный дизайн от Qt:
#   designer.exe в папках библиотек
# Конвертация файла *.ui в *.py (-x раньше надо было):
#   pyside2-uic in.ui -o out.py
# а вообще в designer есть пункт меню "Просмотреть в Python", но его надо править, добавив к пути /bin/

# Чтоб не заливать библиотеки витуальной среды, в .gitignore добавляем папку "venv" (должна быть там по шаблону)
# Сохраняем список библиотек (для гитхабовцев):
#   pip freeze > requirements.txt
# Установка библиотек по списку (создание виртуальной среды для проектов с гитахаба) (КАЖЕТСЯ НЕ РАБОТАЕТ):
#   pip install -r requirements.txt

print("см. комментарии в редакторе")
input()