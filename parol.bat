@echo off
chcp 1251
cls
:1
set /p Pass=пароль:
if %Pass%==1234 (goto 2) else (echo пароль не верный && goto 1)
:2
echo пароль верный
pause >nul