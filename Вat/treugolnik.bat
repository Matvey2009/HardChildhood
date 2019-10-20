@echo off
chcp 1251 >nul

:1

cls
set /p S=¬ведите длинну треугольника: 

echo:

for /L %%X in (1,1,%S%) do <nul set /p =@ 
echo @
for /L %%X in (2,1,%S%) do (
	<nul set /p =@
	for /L %%X in (%S%,-1,%%X) do <nul set /p =. 
	echo @
	)
echo @@
echo @
pause>nul
goto 1