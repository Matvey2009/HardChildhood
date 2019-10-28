@echo off
chcp 1251 > nul
title Компулятор 'Java' Кода
mode con cols=48 lines=32
color 0a

echo %TIME% - Compilation
"C:\Program Files\Java\jdk-13.0.1\bin\javac.exe" Tetris.java

>nul pathping /h 1 /p 3000 /q 1 /w 1 127.0.0.1

echo %TIME% - Start
"C:\Program Files\Java\jdk-13.0.1\bin\java.exe" Tetris

pause >nul