#RATORI-game
__author__ = 'Матвей'
from modules.Main import Main
from pyautogui import *
game_version = 1 #Запрос версии с интернета

if __name__ == '__main__':
    main = Main()
    msg = 'Обновить версию'
    win = 'Обнавление'
    local_version = main.local_version
    if local_version < game_version:
        print(msg)
        alert(msg, win, button='ОК' )
    else:
        main.game_start()