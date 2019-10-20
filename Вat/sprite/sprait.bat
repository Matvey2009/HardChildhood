@echo off
chcp 1251
mode con cols=80 lines=37
setlocal ENABLEDELAYEDEXPANSION
set X=1
:1
FOR /F "usebackq delims=" %%i IN (text.txt) DO (
	echo.%%i
	set /a X=X+1
	if !X! gtr 36 (
		set X=1
		>nul pathping /h 1 /p 40 /q 1 /w 1 127.0.0.1
		cls
		)
	)
goto 1
