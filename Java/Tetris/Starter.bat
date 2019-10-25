@echo off
chcp 1251 > nul
title Компулятор 'Java' Кода
mode con cols = 32 lines = 4
color 0a

echo %TIME% - Compilation
"C:\Program Files\Java\jdk-13.0.1\bin\javac.exe" Tetris.java

echo %TIME% - Start
"C:\Program Files\Java\jdk-13.0.1\bin\java.exe" Tetris