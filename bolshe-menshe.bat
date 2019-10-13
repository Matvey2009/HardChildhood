@echo off
chcp 1251 >nul

:1
set /a G=1+1000*%RANDOM%/32767
   echo %G%

:2
set /p S=ведите число: 

if %S%==%G% (echo вы победили & goto 1)
if %S% LSS %G% (echo число больше & goto 2)
if %S% GTR %G% (echo число меньше & goto 2)