@echo off
chcp 1251 >nul
title Java
mode con cols=48 lines=16
color 0a

echo %TIME% - Compilation
"C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe" "Hello world.cs"
