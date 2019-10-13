@echo off
chcp 1251 >nul

:1

cls
set /p S=¬ведите длинну квадрата: 

echo:
for /L %%X in (1,1,%S%) do <nul set /p =@@
echo:

for /L %%X in (3,1,%S%) do (
<nul set /p =@@
for /L %%X in (3,1,%S%) do <nul set /p =. 
echo @@)

for /L %%X in (1,1,%S%) do <nul set /p =@@

pause>nul
goto 1














