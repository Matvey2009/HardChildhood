
@echo off      
chcp 1251
cls
title Камень ножницы бумага 
:1
echo:
echo                 _           _   ___________ 
echo                 \\         //  !           !
echo      ЖЖ          \\       //   !           !
echo     ЖЖЖЖЖ         \\     //    !           !
echo    ЖЖЖЖЖЖЖ         \\   //     !           !
echo   ЖЖЖЖЖЖЖЖЖЖ        \\ //      !           !
echo  ЖЖЖЖЖЖЖЖЖЖЖЖ    OOOOO OOOOO   !           !
echo  ЖЖЖЖЖЖЖЖЖЖЖЖ    O   O O   O   !           !
echo   ЖЖЖЖЖЖЖЖЖЖ     OOOOO OOOOO   !___________!
echo:
choice /c 123 /n /m "Нажмите 1(Камень),2(Ножницы) или 3(Бумага) : 
set KNB=%errorlevel%
cls
if %KNB%==1 (echo Вы выбрали       : Камень)
if %KNB%==2 (echo Вы выбрали       : Ножницы)
if %KNB%==3 (echo Вы выбрали       : Бумага)

set /a RND=1+3*%random%/32767

if %RND%==1 (echo Кампьютер выбрал : Камень)
if %RND%==2 (echo Кампьютер выбрал : Ножницы)
if %RND%==3 (echo Кампьютер выбрал : Бумага)

set /a GAME=%GAME%+1

if %KNB%==%RND% (echo Ничья & set /a DRAW=%DRAW%+1)
if %KNB%==1 (if %RND%==2 (echo Вы победили & set /a WIN=%WIN%+1))
if %KNB%==2 (if %RND%==3 (echo Вы победили & set /a WIN=%WIN%+1))
if %KNB%==3 (if %RND%==1 (echo Вы победили & set /a WIN=%WIN%+1))

if %KNB%==1 (if %RND%==3 (echo Вы проиграли & set /a LOSE=%LOSE%+1))
if %KNB%==2 (if %RND%==1 (echo Вы проиграли & set /a LOSE=%LOSE%+1))
if %KNB%==3 (if %RND%==2 (echo Вы проиграли & set /a LOSE=%LOSE%+1))

echo                                                          CЧЁТ %WIN% : %LOSE%
echo Побед:%WIN%
echo Порожений:%LOSE%
echo Ничьих: %DRAW%
echo Всего игр: %GAME%

echo:

goto 1